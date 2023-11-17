'''
Dictionary of Refernce Ranges of NMR Lipoproteins.
'''

#for float referenge values

def float_range(start, stop, step):
    while start < stop:
        yield float(start)
        start += step


#classes of tests

class HDL:
    HDCH = {
        "Unit": "mg/dL",
        "RoM": list(range(35, 97)),
        "Optimal": [">", 50],
        "Risk": ["<", 50]
    }

    HDFC = {
        "Unit": "mg/dL",
        "RoM": list(range(7, 28)),
        "Optimal": None,
        "Risk": None
    }

class IDL:
    IDAB = {
        "Unit": "mg/dL",
        "RoM": list(range(2, 18)),
        "Optimal": ["<", 4],
        "Risk": [">", 6]
    }

    IDPN = {
        "Unit": "nmol/L",
        "RoM": list(range(36, 317)),
        "Optimal": ["<", 70],
        "Risk": [">", 100]
    }

    IDCH = {
        "Unit": "mg/dL",
        "RoM": list(range(4, 51)),
        "Optimal": None,
        "Risk": None
    }

    IDTG = {
        "Unit": "mg/dL",
        "RoM": list(range(5, 101)),
        "Optimal": ["<", 6],
        "Risk": [">", 10]
    }

class LDL:
    LDAB = {
        "Unit": "mg/dL",
        "RoM": list(range(42, 142)),
        "Optimal": ["<", 70],
        "Risk": [">", 100]
    }

    LDCH = {
        "Unit": "mg/dL",
        "RoM": list(range(55, 228)),
        "OptimalnCD": ["<", 70],
        "OptimalCD": ["<", 100],
        "Risk": [">", 130]
    }

    LDFC = {
        "Unit": "mg/dL",
        "RoM": list(range(17, 64)),
        "Optimal": None,
        "Risk": None
    }

    LDPN = {
        "Unit": "nmol/L",
        "RoM": list(range(760, 2561)),
        "Optimal": ["<", 1000],
        "Risk": [">", 1300]
    }

    LDTG = {
        "Unit": "mg/dL",
        "RoM": list(range(12, 46)),
        "Optimal": ["<", 24],
        "Risk": [">", 28]
    }

class VLDL:
    VLAB = {
        "Unit": "mg/dL",
        "RoM": list(range(3, 27)),
        "Optimal": ["<", 6],
        "Risk": [">", 10]
    }

    VLPN = {
        "Unit": "nmol/L",
        "RoM": list(range(50, 474)),
        "Optimal": ["<", 120],
        "Risk": [">", 180]
    }

    VLTG = {
        "Unit": "mg/dL",
        "RoM": list(range(21, 337)),
        "Optimal": ["<", 60],
        "Risk": [">", 90]
    }

class CALCULATED:
    ABA1 = {
        "Unit": None,
        "RoM": list(float_range(0.30, 1.71, 0.01)),
        "Optimal": ["<", 0.6],
        "Risk": [">", 0.8]
    }

    LDHD = {
        "Unit": None,
        "RoM": list(float_range(0.98, 4.08, 0.01)),
        "Optimal": ["<", 2],
        "Risk": [">=", 5]
    }

    LFLC = {
        "Unit": None,
        "RoM": None,
        "Optimal": ["<", 2],
        "Risk": [">=", 5]
    }

    HFHC = {
        "Unit": None,
        "RoM": None,
        "Optimal": ["<", 0.5],
        "Risk": [">=", 0.5]
    }

class TotalProtein:
    TPTG = {
        "Unit": "mg/dL",
        "RoM": list(range(53, 491)),
        "Optimal": ["<" , 150],
        "Risk": [">", 150]
    }

    TPCH = {
        "Unit": "mg/dL",
        "RoM": list(range(140, 341)),
        "Optimal": ["<" , 200],
        "Risk": [">", 200]
    }

    TPA1 = {
        "Unit": "mg/dL",
        "RoM": list(range(112, 218)),
        "Optimal": None,
        "Risk": None
    }

    TPA2 = {
        "Unit": "mg/dL",
        "RoM": list(range(24, 49)),
        "Optimal": None,
        "Risk": None
    }

    TPAB = {
        "Unit": "mg/dL",
        "RoM": list(range(48, 160)),
        "Optimal": None,
        "Risk": None
    }
