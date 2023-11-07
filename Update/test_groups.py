
LMF = {
    "TPTG": {"Optimal <":150, "High Risk >":150},
    "TPCH": {"Optimal <":200, "High Risk >":200},
    "TPA1": None,
    "TPA2": None,
    "TPAB": None,
    "ABA1": {"Optimal <":0.6, "High Risk >":0.8},
    "TBPN": {"Optimal <":1400, "High Risk >":2000},
}

HDL = {
    "HDCH": {"Optimal <":50, "High Risk >":50 },
    "HDFC": None,
}

IDL = {
    "IDAB": {"Optimal <":4, "High Risk >":6},
    "IDCH": {"Optimal <":70, "High Risk >":100},
    "IDTG": {"Optimal <":6, "High Risk >":10},
}

LDL = {
    "LDAB": {"Optimal <":70, "High Risk >":100},
    "LDCH": {"kardiyovasküler hastalığı olanlarda Optimal <":70,
                        "kardiyovasküler hastalığı olmayanlarda Optimal <":100,
                        "High Risk >":130},
    "LDFC": None,
    "LDPN": {"Optimal <":1000, "High Risk >":1300},
    "LDTG": {"Optimal <":24, "High Risk >":28},
    "LDHD": {"Optimal <":2, "High Risk >":5},                                    
}

VLDL = {
    "VLAB": {"Optimal <":6, "High Risk >":10},
    "VLPN": {"Optimal <":120, "High Risk >":180},
    "VLTG": {"Optimal <":60, "High Risk >":90}
}

RATIO = {
    "ldl-serbest kolestrol / ldl-kolestrol": {"Optimal <":0.5,
                                            "High Risk >=": 0.5},
    "hdl-serbest kolestrol / hdl-kolestrol": {"Optimal <":0.5,
                                            "High Risk >=": 0.5}
}

def MONO():
    dct = {"TPTG": {"Optimal <":150, "High Risk >":150},
           "TPCH": {"Optimal <":200, "High Risk >":200},
           "HDCH": {"Optimal <":50, "High Risk >":50 }}
    return dct

def DI():
    dct = {"ABA1": {"Optimal <":0.6, "High Risk >":0.8},
           "TBPN": {"Optimal <":1400, "High Risk >":2000},
           "IDAB": {"Optimal <":4, "High Risk >":6},
           "IDCH": {"Optimal <":70, "High Risk >":100},
           "IDTG": {"Optimal <":6, "High Risk >":10},
           "LDAB": {"Optimal <":70, "High Risk >":100},
           "LDPN": {"Optimal <":1000, "High Risk >":1300},
           "LDTG": {"Optimal <":24, "High Risk >":28},
           "LDHD": {"Optimal <":2, "High Risk >":5},
           "VLAB": {"Optimal <":6, "High Risk >":10},
           "VLPN": {"Optimal <":120, "High Risk >":180},
           "VLTG": {"Optimal <":60, "High Risk >":90}}
    return dct

def MULT():
    dct = {"LDCH": {"kardiyovasküler hastalığı olanlarda Optimal <":70,
                    "kardiyovasküler hastalığı olmayanlarda Optimal <":100,
                    "High Risk >":130}}
    return dct

def NO():
    lst = ["TPA1","TPA2","TPAB","HDFC","LDFC"]
    return lst

# You can also make a class for each having types of charts seperated and turned when needed,
# or returning the sum of all