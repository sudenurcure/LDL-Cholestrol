import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from range_charts import t_chart
from save_plot import insert_plot as IP
import ReferenceDictionary as dd

maindata = pd.read_csv("lipo_result_file_1.csv")
maindata.drop(["Directory","name","date","type"],axis = 1, inplace=True)

#Work with every patient one by one. 
for i in range(0,len(maindata)):
    df = maindata.iloc[i] #Put one patient in a dataframe.
    tests = pd.Series(df.index) #Put tests done in tests series