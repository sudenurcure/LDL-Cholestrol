import pandas as pd
import test_groups as TG

Tests = []

def main():
    data = pd.read_excel("Sample.xlsx", header=0)
    #data = data.drop(columns= "Referans Değer")
    DataPrep(data)

class PrepTests:
    """ Save testname and make a dataframe of test results.
    """
    def __init__(self,name):
        self.name = name
        self.dataframe = self.make_df()

    def make_df(self,add = False, dta =[]):
        if add:
            self.dataframe = pd.concat([self.dataframe, dta], axis= 1, ignore_index= True)
            return
        else:
            df = pd.DataFrame()
            return df
        
def DataPrep(data):
    for index, element in data.iterrows():
        strings = 0
        if isinstance(element["Sonuç"], str) and element["Sonuç"] != "None":
            strings += 1
            tn = f"Test {element['Test Adı']}"
            tablename = element['Test Adı']
            #tablename= data.iloc[index,0]
            tn =  PrepTests(tablename)
            Tests.append(tn)
        else:
            Tests[-1].make_df(add = True, dta = data.iloc[index])

    for test in Tests:
        test.dataframe = test.dataframe.transpose()


##Control Data 
"""
Control reference against test_groups
Control mg/dL and nmol/L
Control any remaining NaN
"""

def CTestGExists(Test):
    #Take given test_groups name from class.name and check existence in test_groups
    given_tg_name = Test.lower().replace(" ", "_")
    if given_tg_name not in TG.tests():
        print(f"{Test} is not in tests library")
        return False
    return True

def CTestExists(Group, test):
    #Take class.name as Group and df["Test Adı"] as test and check test' existence in Group in test_groups
    given_tg_name = Group.lower().replace(" ", "_")
    given_test = test.lower().replace(" ", "_")
    
    try: 
        test_dict = TG.Lead(given_test)
        return test_dict
    except:
        print(f"{test} is not in tests library.")

def CUnit():
    #Take df["Test Adı"]["Birim"] as given Unit and check test_groups equivalance
    
    return 

def CRef(Test):
    #Take df["Test Adı"]["Referans Değer"] as given Reference and check test_groups equivalance 
    """
    data.loc[data["Test Adı"] == "Trigliserid", "Referans Değer"]
    """
    return


#Prep Chart
"""
Give information of:
    PrepTest.name
    df["Test Name"]
    data.loc[data["Test Adı"] == "Test Name", "Sonuç"]

to plotting.py
"""



#Main
main()
    