import pandas as pd 
import Subfractions
import main_creation
from periodic_assessments import periodic
from NMRLipoprotein import NMRLipoprotein as NMR

maindata = pd.read_csv("lipo_result_file_1.csv")
maindata.drop(["Directory","name","date","type"],axis = 1, inplace=True)

#Work with every patient one by one. 
for i in range(0,len(maindata)):
    df = maindata.iloc[i] #Put one patient in a dataframe.
    patient= NMR(df) #Classify results
    dfdict = df.to_dict()

    Subfractions.Cholestrol(patient)
    Subfractions.FreeCholestrol(patient)
    Subfractions.Phospolipid(patient)
    Subfractions.Triglycerides(patient)

    main_creation.conditional(df,dfdict)
    main_creation.calculated_LFLC(df)

    periodic(df)




