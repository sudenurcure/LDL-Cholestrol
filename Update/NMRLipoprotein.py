import pandas as pd

class NMRLipoprotein():
    ldl_labels = ["LDL-1","LDL-2","LDL-3","LDL-4","LDL-5","LDL-6"]
    hdl_labels = ["HDL-1","HDL-2","HDL-3","HDL-4"]
    vldl_labels = ["VLDL-1","VLDL-2","VLDL-3","VLDL-4","VLDL-5"]

    def __init__(self, df) -> None:
        self.df = df
        self.MainGroups()
        self.Subfractions()
        pass

    def MainGroups(self):
        self.HDL_mains = self.df[self.df.index.str.contains("^HD+")]
        self.HDL_mains = pd.to_numeric(self.HDL_mains, errors="coerce")

        self.IDL_mains = self.df[self.df.index.str.contains("^ID+")]
        self.IDL_mains = pd.to_numeric(self.IDL_mains, errors="coerce")

        self.LDL_mains = self.df[self.df.index.str.contains("^LD+")]
        self.LDL_mains = pd.to_numeric(self.LDL_mains, errors="coerce")

        self.VLDL_mains = self.df[self.df.index.str.contains("^VL+")]
        self.VLDL_mains = pd.to_numeric(self.VLDL_mains, errors="coerce")

    
    def Subfractions(self):
        self.HDL_sub_ch=  self.df[self.df.index.str.contains("H\d+CH")]
        self.HDL_sub_ch = pd.to_numeric(self.HDL_sub_ch, errors="coerce")
        self.HDL_sub_ch.index= self.hdl_labels

        self.HDL_sub_fch=  self.df[self.df.index.str.contains("H\d+FC")]
        self.HDL_sub_fch = pd.to_numeric(self.HDL_sub_fch, errors="coerce")
        self.HDL_sub_fch.index= self.hdl_labels

        self.HDL_sub_pl=  self.df[self.df.index.str.contains("H\d+PL")]
        self.HDL_sub_pl = pd.to_numeric(self.HDL_sub_pl, errors="coerce")
        self.HDL_sub_pl.index= self.hdl_labels

        self.HDL_sub_tg=  self.df[self.df.index.str.contains("H\d+TG")]
        self.HDL_sub_tg = pd.to_numeric(self.HDL_sub_tg, errors="coerce")
        self.HDL_sub_tg.index= self.hdl_labels


        self.LDL_sub_ch=  self.df[self.df.index.str.contains("L\d+CH")]
        self.LDL_sub_ch = pd.to_numeric(self.LDL_sub_ch, errors="coerce")
        self.LDL_sub_ch.index= self.ldl_labels

        self.LDL_sub_fch=  self.df[self.df.index.str.contains("L\d+FC")]
        self.LDL_sub_fch = pd.to_numeric(self.LDL_sub_fch, errors="coerce")
        self.LDL_sub_fch.index= self.ldl_labels

        self.LDL_sub_pl=  self.df[self.df.index.str.contains("L\d+PL")]
        self.LDL_sub_pl = pd.to_numeric(self.LDL_sub_pl, errors="coerce")
        self.LDL_sub_pl.index= self.ldl_labels

        self.LDL_sub_tg=  self.df[self.df.index.str.contains("L\d+TG")]
        self.LDL_sub_tg = pd.to_numeric(self.LDL_sub_tg, errors="coerce")
        self.LDL_sub_tg.index= self.ldl_labels


        self.VLDL_sub_ch=  self.df[self.df.index.str.contains("V\d+CH")]
        self.VLDL_sub_ch = pd.to_numeric(self.VLDL_sub_ch, errors="coerce")
        self.VLDL_sub_ch.index= self.vldl_labels

        self.VLDL_sub_fch=  self.df[self.df.index.str.contains("V\d+FC")]
        self.VLDL_sub_fch = pd.to_numeric(self.VLDL_sub_fch, errors="coerce")
        self.VLDL_sub_fch.index= self.vldl_labels

        self.VLDL_sub_pl=  self.df[self.df.index.str.contains("V\d+PL")]
        self.VLDL_sub_pl = pd.to_numeric(self.VLDL_sub_pl, errors="coerce")
        self.VLDL_sub_pl.index= self.vldl_labels

        self.VLDL_sub_tg=  self.df[self.df.index.str.contains("V\d+TG")]
        self.VLDL_sub_tg = pd.to_numeric(self.VLDL_sub_tg, errors="coerce")
        self.VLDL_sub_tg.index= self.vldl_labels
