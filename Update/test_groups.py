
LMF = {
    "TPTG": {150 : "Optimal <", 150 :"High Risk >"},
    "TPCH": {200 : "Optimal <", 200 :"High Risk >"},
    "TPA1": None,
    "TPA2": None,
    "TPAB": None,
    "ABA1": {0.6 : "Optimal <", 0.8 :"High Risk >"},
    "TBPN": {1400 : "Optimal <", 2000 :"High Risk >"},
}

HDL = {
    "HDCH": {50 : "Optimal <", 50 :"High Risk >"},
    "HDFC": None,
}

IDL = {
    "IDAB": {4 : "Optimal <", 6 :"High Risk >"},
    "IDCH": None,
    "IDTG": {6 : "Optimal <", 10 :"High Risk >"},
}

LDL = {
    "LDAB": {70 : "Optimal <", 100 :"High Risk >"},
    "LDCH": {"kardiyovasküler hastalığı olanlarda Optimal <":70,
                        "kardiyovasküler hastalığı olmayanlarda Optimal <":100,
                        130 :"High Risk >"},
    "LDFC": None,
    "LDPN": {1000 : "Optimal <", 1300 :"High Risk >"},
    "LDTG": {24 : "Optimal <", 28 :"High Risk >"},
    "LDHD": {2 : "Optimal <", 5 :"High Risk >"},                                    
}

VLDL = {
    "VLAB": {6 : "Optimal <", 10 :"High Risk >"},
    "VLPN": {120 : "Optimal <", 180 :"High Risk >"},
    "VLTG": {60 : "Optimal <", 90 :"High Risk >"}
}

RATIO = {
    "ldl-serbest kolestrol / ldl-kolestrol": {0.5 : "Optimal <",
                                            "High Risk >=": 0.5},
    "hdl-serbest kolestrol / hdl-kolestrol": {0.5 : "Optimal <",
                                            "High Risk >=": 0.5}
}

def MONO():
    dct = {"TPTG": {"High Risk":150, "when" : ">"},
           "TPCH": {"High Risk":200,"when" : ">"},
           "HDCH": {"High Risk":50,"when" : ">"}}
    return dct

def DI():
    dct = {"ABA1": {0.6: "Optimal <", 0.8:"High Risk >"},
           "TBPN": {1400: "Optimal <", 2000 : "High Risk >"},
           "IDAB": {4 : "Optimal <", 6 :"High Risk >"},
           "IDCH": {70: "Optimal <", 100 :"High Risk >"},
           "IDTG": {6 : "Optimal <", 10 :"High Risk >"},
           "LDAB": {70 : "Optimal <", 100 :"High Risk >"},
           "LDPN": {1000 : "Optimal <", 1300 :"High Risk >"},
           "LDTG": {24 : "Optimal <", 28 :"High Risk >"},
           "LDHD": {2 : "Optimal <", 5 :"High Risk >"},
           "VLAB": {6 : "Optimal <", 10 :"High Risk >"},
           "VLPN": {120 : "Optimal <", 180 :"High Risk >"},
           "VLTG": {60 : "Optimal <", 90 :"High Risk >"}}
    return dct

def MULT():
    dct = {"LDCH": {"kardiyovasküler hastalığı olanlarda Optimal <":70,
                    "kardiyovasküler hastalığı olmayanlarda Optimal <":100,
                    130 :"High Risk >"}}
    return dct

def NO():
    lst = ["TPA1","TPA2","TPAB","HDFC","LDFC"]
    return lst

# You can also make a class for each having types of charts seperated and turned when needed,
# or returning the sum of all