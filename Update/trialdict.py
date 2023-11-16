class LDL():
    "LDHD": {2 : "Optimal <", 5 :"High Risk >"}

    def __init__(self) -> None:
        pass

    def LDAB(self):
        self.LDAB.Unit = "mg/dL"
        self.LDAB.RoM = range[3,27]
        self.LDAB.Optimal = ["<", 70]
        self.LDAB.Risk = [">", 100]
        return 0
    
    def LDCH(self):
        self.LDCH.Unit = "mg/dL"
        self.LDCH.RoM = range[5,78]
        self.LDCH.OptimalnCD = ["<", 70]
        self.LDCH.OptimalCD = ["<", 100]
        self.LDCH.Risk = [">", 130]
        return 0
    
    def LDFC(self):
        self.LDFC.Unit = "mg/dL"
        self.LDFC.RoM = range[17,64]
        self.LDFC.Optimal = None
        self.LDFC.Risk = None
        return 0
    
    def LDPN(self):
        self.LDPN.Unit = "mg/dL"
        self.LDPN.RoM = range[3,27]
        self.LDPN.Optimal = ["<", 1000]
        self.LDPN.Risk = [">", 1300]
        return 0
    
    def LDTG(self):
        self.LDTG.Unit = "mg/dL"
        self.LDTG.RoM = range[12,46]
        self.LDTG.Optimal = ["<", 24]
        self.LDTG.Risk = [">", 28]
        return 0
    
    def LDHD(self):
        self.LDHD.Unit = None
        self.LDHD.RoM = range[0.98,4.08]
        self.LDHD.Optimal = ["<", 2]
        self.LDHD.Risk = [">", 5]
        return 0
    