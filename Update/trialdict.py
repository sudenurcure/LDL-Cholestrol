class HDL():
    def __init__(self) -> None:
        pass

    def HDCH(self):
        self.HDCH.Unit = "mg/dL"
        self.HDCH.RoM = range[35,97]
        self.HDCH.Optimal = [">", 50]
        self.HDCH.Risk = ["<", 50]
        return 0
    
    def HDFC(self):
        self.HDFC.Unit = "mg/dL"
        self.HDFC.RoM = range[7,28]
        self.HDFC.Optimal = None
        self.HDFC.Risk = None
        return 0
    

class IDL():
    def __init__(self) -> None:
        pass

    def IDAB(self):
        self.IDAB.Unit = "mg/dL"
        self.IDAB.RoM = range[2,18]
        self.IDAB.Optimal = ["<", 4]
        self.IDAB.Risk = [">", 6]
        return 0
    
    def IDPN(self):
        self.IDPN.Unit = "nmol/L"
        self.IDPN.RoM = range[36,317]
        self.IDPN.Optimal = ["<", 70]
        self.IDPN.Risk = [">", 100]
        return 0
    
    def IDCH(self):
        self.IDCH.Unit = "mg/dL"
        self.IDCH.RoM = range[4,51]
        self.IDCH.Optimal = None
        self.IDCH.Risk = None
        return 0
    
    def IDTG(self):
        self.IDTG.Unit = "mg/dL"
        self.IDTG.RoM = range[5,101]
        self.IDTG.Optimal = ["<", 6]
        self.IDTG.Risk = [">", 10]
        return 0

    
class LDL():
    def __init__(self) -> None:
        pass

    def LDAB(self):
        self.LDAB.Unit = "mg/dL"
        self.LDAB.RoM = range[42,142]
        self.LDAB.Optimal = ["<", 70]
        self.LDAB.Risk = [">", 100]
        return 0
    
    def LDCH(self):
        self.LDCH.Unit = "mg/dL"
        self.LDCH.RoM = range[55,228]
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
        self.LDPN.Unit = "nmol/L"
        self.LDPN.RoM = range[760,2561]
        self.LDPN.Optimal = ["<", 1000]
        self.LDPN.Risk = [">", 1300]
        return 0
    
    def LDTG(self):
        self.LDTG.Unit = "mg/dL"
        self.LDTG.RoM = range[12,46]
        self.LDTG.Optimal = ["<", 24]
        self.LDTG.Risk = [">", 28]
        return 0
    
    
class VLDL():
    def __init__(self) -> None:
        pass

    def VLAB(self):
        self.VLAB.Unit = "mg/dL"
        self.VLAB.RoM = range[3,27]
        self.VLAB.Optimal = ["<", 6]
        self.VLAB.Risk = [">", 10]
        return 0
    
    def VLPN(self):
        self.VLPN.Unit = "nmol/L"
        self.VLPN.RoM = range[50,474]
        self.VLPN.Optimal = ["<", 120]
        self.VLPN.Risk = [">", 180]
        return 0
    
    def VLTG(self):
        self.VLTG.Unit = "mg/dL"
        self.VLTG.RoM = range[21,337]
        self.VLTG.Optimal = ["<", 60]
        self.VLTG.Risk = [">", 90]
        return 0
    
class CALCULATED():
    def __init__(self) -> None:
        pass

    def HFHC(self):
        self.ABA1.Unit = None
        self.ABA1.RoM = range[0.30,1.71]
        self.ABA1.Optimal = ["<", 0.6]
        self.ABA1.Risk = [">", 0.8]
    
    def LDHD(self):
        self.LDHD.Unit = None
        self.LDHD.RoM = range[0.98,4.08]
        self.LDHD.Optimal = ["<", 2]
        self.LDHD.Risk = [">", 5]
    
    def LFLC(self):
        self.LFLC.Unit = None
        self.LFLC.RoM = None
        self.LFLC.Optimal = ["<", 2]
        self.LFLC.Risk = [">=", 5]
    
    def HFHC(self):
        self.HFHC.Unit = None
        self.HFHC.RoM = None
        self.HFHC.Optimal = ["<", 0.5]
        self.HFHC.Risk = [">=", 0.5]

class TotalProtein():
    def __init__(self) -> None:
        pass

    def TPTG(self):
        self.TPTG.Unit = "mg/dL"
        self.TPTG.RoM = range[53,491]
        self.TPTG.Optimal = ["<" , 150]
        self.TPTG.Risk = [">", 150]

    def TPCH(self):
        self.TPCH.Unit = "mg/dL"
        self.TPCH.RoM = range[140,341]
        self.TPCH.Optimal = ["<" , 200]
        self.TPCH.Risk = [">", 200]

    def TPA1(self):
        self.TPAB.Unit = "mg/dL"
        self.TPAB.RoM = range[112,218]
        self.TPAB.Optimal = None
        self.TPAB.Risk = None

    def TPA2(self):
        self.TPAB.Unit = "mg/dL"
        self.TPAB.RoM = range[24,49]
        self.TPAB.Optimal = None
        self.TPAB.Risk = None

    def TPAB(self):
        self.TPAB.Unit = "mg/dL"
        self.TPAB.RoM = range[48,160]
        self.TPAB.Optimal = None
        self.TPAB.Risk = None