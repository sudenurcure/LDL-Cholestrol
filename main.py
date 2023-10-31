import pandas as pd
import warnings
import re
import test_groups as TG
import sort_fp as SFP



# Ignore FutureWarning for using float on a single-element Series
warnings.simplefilter(action='ignore', category=FutureWarning)

Tests = []

def main():
    data = pd.read_excel("Sample.xlsx", header=0)
    NA_tests= data.loc[data["Sonuç"].isna(), "Test Adı"].unique()

    if len(NA_tests) != 0:
        print("These tests are entered with empty results: ")
        for test in NA_tests:
            print(test)

    data.dropna(axis = 0, inplace = True, subset = ["Sonuç"])
    data['Sonuç'] = pd.to_numeric(data['Sonuç'], errors='coerce')

    DataPrep(data)
    df = WorkingData(data)
    # Make the first control for test group's existence then direct it
    for test in Tests:
        if CTestGExists(test.name):
            Director(test)  

class PrepTests:
    """ Save testname and make a dataframe of test results.
    """
    def __init__(self,name):
        self.name = name.lower().replace(" ", "_")
        self.dataframe = self.make_df()

    def make_df(self,add = False, dta =[]):
        if add:
            # Apply lower and replace operations to string elements
            dta = dta.apply(lambda x: x.lower() if isinstance(x, str) else x)
            self.dataframe = pd.concat([self.dataframe, dta], axis= 1, ignore_index= True)
            return
        else:
            df = pd.DataFrame()
            return df
        
def WorkingData(data):
    df = data.dropna(subset=['Sonuç'])
    return df

def DataPrep(data):
    for index, element in data.iterrows():
        strings = 0
        if pd.isna(element["Sonuç"]):
            strings += 1
            tablename = element['Test Adı'].lower().replace(" ", "_")
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
    given_name = Test.title().replace("_", " ")
    if Test not in TG.tests:
        print(f"{given_name} is not in tests library")
        return False
    return True

def CTestExists(Group, test):
    #Take class.name as Group and df["Test Adı"] as test and check test' existence in Group in test_groups
    #given_tg_name = Group.lower().replace(" ", "_")
    given_test = test.lower().replace(" ", "_")

    test_dict = TG.Lead(Group.lower().replace(" ", "_"))
    try: 
        given_test in test_dict.keys()
    except:
        print(f"{given_test} is not in tests library.")
        return False
    return True

def CUnit(test, birim):
    #Take data.loc[data["Test Adı"] == "Trigliserid", "Birim"] as given Unit and check test_groups equivalance
    empty_unit = ["ldl serbest kolestrol","hdl serbest kolestrol",
             "ldl-serbest kolestrol / ldl-kolestrol",
             "hdl-serbest kolestrol / hdl-kolestrol"]
    given_test = test.lower()

    if given_test in empty_unit:
        print(f"{test} does not have a unit.")
        return True
    
    if any(item == "mg/dl" for item in birim):
        if not given_test in TG.units["mg/dl"]:
            print(f"{test} has a wrong unit.")
            return False
    elif any(item == "nmol/l" for item in birim):
        if not given_test in TG.units["nmol/l"]:
            print(f"{test} has a wrong unit.")
            return False
    return True 

def CRef(Group, test, references):
    #Take data.loc[data["Test Adı"] == "Trigliserid", "Referans Değer"] as given Reference and check test_groups equivalance 
    """
    data.loc[data["Test Adı"] == "Trigliserid", "Referans Değer"]
    """
    givenref = {}

    references = references.str.lower()

    if test.lower().replace(" ","_") in ["apolipoprotein_a1","apolipoprotein_a2","apolipoprotein_b100",
        "ldl_serbest_kolestrol", "hdl_serbest_kolestrol"]:
        print(f"{test} does not have a reference value.")
        return False

    string_parts = references.apply(lambda x: re.split(r'([<>]=?)', x))
    string_parts = string_parts.apply(lambda x: [s.strip() for s in x if s.strip()])

    for string_part in string_parts:
        for x in range(0, len(string_part)):
            if x % 2 == 0:
                numeric_pattern = r'[-+]?\d*\.\d+|\d+'
                mainstr = string_part[x + 1]
                numerical_values = re.findall(numeric_pattern, mainstr)
                numerical_values = [int(num) if num.isnumeric() else float(num) for num in numerical_values]
                mainstr = re.sub(numeric_pattern, '', mainstr).strip() + " " + string_part[x]
                givenref[mainstr] = numerical_values[0]

    #compare givenref  with the test_group now
    refexists = TG.Lead(Group).get(test, "NaN")

    if refexists != "NaN":
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
def Director(test_class):
    GroupName = test_class.name
    df = test_class.dataframe
    testnames = df["Test Adı"]

    for testname in testnames:
        references = df.loc[df["Test Adı"] == testname, "Referans Değer"]
        birim = df.loc[df["Test Adı"] == testname, "Birim"]
        pvalue = df.loc[df["Test Adı"] == testname, "Sonuç"]
        pvalue = float(pvalue)
        if CTestExists(GroupName, testname) and CUnit(testname, birim) and CRef(GroupName, testname, references):
            SFP.Sorter(GroupName, testname, pvalue)
        

main()
    