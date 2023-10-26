import pandas as pd
import re
import test_groups as TG

Tests = []

def main():
    data = pd.read_excel("Sample.xlsx", header=0)
    #data = data.drop(columns= "Referans Değer")
    DataPrep(data)

    for test in Tests:
        if CTestGExists(test.name):
            Director(test)  

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
    #given_tg_name = Group.lower().replace(" ", "_")
    given_test = test.lower()
    test_dict = TG.Lead(Group.lower())
    try: 
        given_test in test_dict.keys()
    except:
        print(f"{test} is not in tests library.")
        return False
    return True

def CUnit(test, birim):
    #Take data.loc[data["Test Adı"] == "Trigliserid", "Birim"] as given Unit and check test_groups equivalance
    empty = ["ldl serbest kolestrol","hdl serbest kolestrol",
             "ldl-serbest kolestrol / ldl-kolestrol",
             "hdl-serbest kolestrol / hdl-kolestrol"]
    given_test = test.lower()

    if given_test in empty:
        return False

    if birim == "mg/dL":
        if not given_test in TG.units["mg/dL"]:
            print(f"{test} has a wrong unit.")
            return False
    elif birim == "nmol/L":
        if not given_test in TG.units["nmol/L"]:
            print(f"{test} has a wrong unit.")
            return False
    return True 

def CRef(Group, test, references):
    #Take data.loc[data["Test Adı"] == "Trigliserid", "Referans Değer"] as given Reference and check test_groups equivalance 
    """
    data.loc[data["Test Adı"] == "Trigliserid", "Referans Değer"]
    """
    givenref = {}

    references= references.lower()
    string_parts = re.split(r'([<>]=?)', references)
    string_parts = [s.strip() for s in string_parts if s.strip()]
    
    for x in range(0, len(string_parts)):
        if x%2 == 0:
            numeric_pattern = r'[-+]?\d*\.\d+|\d+'
            mainstr = string_parts[x+1]
            numerical_values = re.findall(numeric_pattern, mainstr)
            numerical_values = [int(num) if num.isnumeric() else float(num) for num in numerical_values]
            mainstr = re.sub(numeric_pattern, '', mainstr).strip() + " " +string_parts[x]
            givenref[mainstr] = numerical_values[0]

    #compare givenref  with the test_group now
    refexists = TG.Lead(Group).get(test, None)
    if refexists is not None:
        try:
            refexists == givenref
        except:
            print(f"Reference of {test} is different than known reference for this test.")
            return False
        return True
    else:
        print(f"No reference found for test: {test}")
        return False


#Prep Chart
"""
Give information of:
    PrepTest.name
    df["Test Name"]
    data.loc[data["Test Adı"] == "Test Name", "Sonuç"]

to plotting.py
"""
def Director(CClass):
    GroupName = CClass.name
    df = CClass.df
    testnames = df["Test Adı"]
    fp = open(f'{GroupName}.txt',"w")

    for testname in testnames:
        references = df.loc[df["Test Adı"] == testname, "Referans Değerleri"]
        birim = df.loc[df["Test Adı"] == testname, "Birim"]
        pvalue = df.loc[df["Test Adı"] == testname, "Sonuç"]

        if CTestExists(GroupName, testname) and CUnit(testname, birim) and CRef(GroupName, testname, references):
            fp.write(testname+" "+ pvalue +"\n")
            TG.Leader(GroupName, testname, pvalue, fp)
        

main()
    