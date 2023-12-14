class HDL():
    """HDL"""
    re_HDL = r"^HD+"
    re_HDL_subf = r"H\d+"
    re_HDL_apo = r"H1A\d"
    re_HDL_lipo = r"HD+"

    """IDL"""
    re_IDL = r"^ID+"
    re_IDL_lipo = r"ID+"

    """LDL"""
    re_LDL = r"^LD+"
    re_LDL_subf = r"L\d+"
    re_LDL_apo = r"L\dAB"
    re_LDL_lipo = r"LD+"

    """VLDL"""
    re_VLDL =r"^VL+"
    re_VLDL_subf =r"V\d+"
    re_VLDL_lipo =r"VL+"


    def __init__(self, tests) -> None:
        self.tests = tests
        self.findHDLGroups()
        pass

    def findHDLGroups(self):
        self.HDL_mains = self.tests[self.tests.str.contains(self.re_HDL)]
        self.HDL_subf = self.tests[self.tests.str.contains(self.re_HDL_subf)]
        self.HDL_apo = self.tests[self.tests.str.contains(self.re_HDL_apo)]
        self.HDL_lipo = self.tests[self.tests.str.contains(self.re_HDL_lipo)]