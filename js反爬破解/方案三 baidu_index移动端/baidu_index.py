# - * - coding: utf-8 - * -

ptbk_param = "QPc,g2MA6UOGuSk+95.8163,7%-042"
obj_data = "Uk2SM6UuM2S6UkAMS6cMcAU6M2UMS6UuMcg6USA2M6UgPM26UckS26MSSSM6cMUAM6MUASg6Uk22c6USAuS6USSUk6MMUPc6cPkug6MUSug6MgAAg6UMkgk6MMMgk6MSkMA6UcAUk6UMcSS6UAUSg6UMUMS6ggcg26gUMPA6UScMk6gk2MP6USA2k6USPku6UUkPu6UgMUA6gSMkP6UMMcU6Ug2Mu6UkMck6U2ggP6gUugP6gkPSu6gkkk26UgUcA6PcSMM6gA22M6g2c2c6UPcUS6gAucu6gSASg6gk2Uu6gucPU6UMPPc6gAMkk6Ucg2c6gPM2S6gUkU26PukSA6PkuUg6gkkSS6Ug2uc6guukc6UUP2M6MgMP26UPkSU6USPcc6P2cMP6UMgSg6Mu2Uk6UScUA6MUUuc6cM2Ac6cMSkg6SS2UA6ASPgM6AkcSg6Aku226AUMcU6AguAP6AckcS6kgSPg6kgcUU6kUuM26kPPMc6Au2Sc6S2AkM6AUA2A6kUugk6kUASc6kPuP26Akucu"

def Parse_baidu(ptbk_param, obj_data):
    x = list(ptbk_param)
    M = list(obj_data)
    b = {}
    S = []
    _len = x.__len__() / 2
    for _ in range(_len):
        b[x[_]] = x[_len + _]

    Alen = M.__len__()
    for A in range(Alen):
        S.append(b[M[A]])
    return "".join(S)
if __name__ == '__main__':
    print Parse_baidu(ptbk_param, obj_data)
