import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from save_plot import  insert_plot as IP

def table(df,where):
    lp , test = where.split(" ")

    fig, ax = plt.subplots()
    ax.plot(df.index, df['patient'], marker='o', linestyle='-')
    ax.bar(df.index, df['highest'] - df['lowest'], color='blue', bottom=df['lowest'], alpha=0.3)

    ax.set_ylabel('mg/dL', fontsize=12)
    ax.tick_params(axis='both', which='major', labelsize=14)

    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))

    plt.grid(True)
    IP(f"{test}.png",plt, f"{lp}_SUBF")

def join(hdl, hdl_range, ldl,ldl_range, vldl, vldl_range): #join range with patient value
    hdl_df = pd.DataFrame()
    ldl_df = pd.DataFrame()
    vldl_df = pd.DataFrame()
    for name,data,range in [["hdl",hdl,hdl_range],["ldl",ldl,ldl_range],["vldl",vldl,vldl_range]]:
        placeholder= range.join(data)
        placeholder.columns = ["lowest","highest","patient"]
        placeholder.lowest = placeholder.lowest.astype(float)
        placeholder.highest = placeholder.highest.astype(float)

        if name == "hdl":
            hdl_df = pd.concat([placeholder, hdl_df], axis=1)
        elif name == "ldl":
            ldl_df = pd.concat([placeholder, ldl_df], axis=1)
        else:
            vldl_df = pd.concat([placeholder, vldl_df], axis=1)
    return hdl_df, ldl_df, vldl_df


def Cholestrol(patient):
    hdl = patient.HDL_sub_ch
    ldl = patient.LDL_sub_ch
    vldl = patient.VLDL_sub_ch

    hdl_range = pd.DataFrame({"lowest": [6,4,7,11],"highest": [46,16,19,30]}, index = hdl.index)
    ldl_range = pd.DataFrame({"lowest": [8,2,3,4,5,6],"highest": [59,48,46,49,49,54]}, index = ldl.index)
    vldl_range = pd.DataFrame({"lowest": [1,0,0,1,0],"highest": [35,15,16,15,4]}, index = vldl.index)

    hdl_df, ldl_df, vldl_df = join(hdl, hdl_range, ldl,ldl_range, vldl, vldl_range)
    table(hdl_df,"HDL chol")
    table(ldl_df,"LDL chol")
    table(vldl_df,"VLDL chol")

def FreeCholestrol(patient):
    hdl = patient.HDL_sub_fch
    ldl = patient.LDL_sub_fch
    vldl = patient.VLDL_sub_fch

    hdl_range = pd.DataFrame({"lowest": [1,1,1,2],"highest": [12,5,5,9]}, index = hdl.index)
    ldl_range = pd.DataFrame({"lowest": [2,1,1,1,2,2],"highest": [17,14,13,12,13,12]}, index = ldl.index)
    vldl_range = pd.DataFrame({"lowest": [0,0,0,0,0],"highest": [13,7,8,7,2]}, index = vldl.index)

    hdl_df, ldl_df, vldl_df = join(hdl, hdl_range, ldl,ldl_range, vldl, vldl_range)
    table(hdl_df,"HDL freechol")
    table(ldl_df,"LDL freechol")
    table(vldl_df,"VLDL freechol")

def Phospolipid(patient):
    hdl= patient.HDL_sub_pl
    ldl = patient.LDL_sub_pl
    vldl = patient.VLDL_sub_pl

    hdl_range = pd.DataFrame({"lowest": [8,7,12,20],"highest": [57,27,32,44]}, index = hdl.index)
    ldl_range = pd.DataFrame({"lowest": [6,2,2,3,4,4],"highest": [30,25,24,25,25,28]}, index = ldl.index) 
    vldl_range = pd.DataFrame({"lowest": [1,1,1,2,0],"highest": [32,15,14,13,5]}, index = vldl.index)

    hdl_df, ldl_df, vldl_df = join(hdl, hdl_range, ldl,ldl_range, vldl, vldl_range)
    table(hdl_df,"HDL phospholipid")
    table(ldl_df,"LDL phospholipid")
    table(vldl_df,"VLDL phospholipid")

def Triglycerides(patient):
    hdl = patient.HDL_sub_tg
    ldl = patient.LDL_sub_tg
    vldl = patient.VLDL_sub_tg

    hdl_range = pd.DataFrame({"lowest": [1,1,1,2],"highest": [12,5,5,8]}, index = hdl.index)
    ldl_range = pd.DataFrame({"lowest": [3,1,1,1,1,1],"highest": [14,6,6,8,9,13]}, index = ldl.index)
    vldl_range = pd.DataFrame({"lowest": [6,3,2,3,1],"highest": [212,67,49,28,7]}, index = vldl.index)

    hdl_df, ldl_df, vldl_df = join(hdl, hdl_range, ldl,ldl_range, vldl, vldl_range)
    table(hdl_df,"HDL triglycerides")
    table(ldl_df,"LDL triglycerides")
    table(vldl_df,"VLDL triglycerides")