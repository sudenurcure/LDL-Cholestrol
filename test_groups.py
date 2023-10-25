
"""def Checks(lists):
    if lists == tests:
        return ["nmr_lipoporotein_profili","ldl_alt_fraksi̇yonları","aterojeni̇k_li̇poprotei̇nlerde_apo_b100_ve_tri̇gli̇seri̇d",
            "li̇poprotei̇n_kolestrol_esteri̇fi̇kasyonu"]
    elif lists == nits:


"""

tests = ["nmr_lipoporotein_profili","ldl_alt_fraksi̇yonları","aterojeni̇k_li̇poprotei̇nlerde_apo_b100_ve_tri̇gli̇seri̇d",
            "li̇poprotei̇n_kolestrol_esteri̇fi̇kasyonu"]

units = {
    "mg/dL" : ["trigliserid","kolestrol, total","kolestrol, ldl","kolestrol, hdl","kolestrol, ldl/ kolestrol, hdl oranı",
               "apolipoprotein a1","apolipoprotein a2","ldl-apo-b100","idl-apo-b100","vldl-apo-b100","ldl-trigliserid",
               "idl-trigliserid","vldl-trigliserid"],
    "nmol/L" : ["apolipoprotein b100","apo-b100 / apo-a1 oranı","total apob taşıyan partikül sayısı, total apob-p",
                "ldl partikül sayısı, ldl-p","idl partikül sayısı, idl-p","vldl partikül sayısı, vldl-p",
                "ldl1-partikül sayısı","ldl2-partikül sayısı","ldl3-partikül sayısı","ldl4-partikül sayısı",
                "ldl5-partikül sayısı","ldl6-partikül sayısı"]
    # no units for li̇poprotei̇n kolestrol esteri̇fi̇kasyonu
}

NLP = {
    "trigliserid": {"optimal düzey <":15, 
                    "artmış kardiovasküler hastalık riski >":15},
    "kolestrol, total": {"optimal düzey <":20,
                        "artmış kardiovasküler hastalık riski >":20},
    "kolestrol, ldl": {"kardiyovasküler hastalığı olanlarda optimal düzey <":7,
                        "kardiyovasküler hastalığı olmayanlarda optimal düzey <":10,
                        "artmış kardiovasküler hastalık riski >":13},
    "kolestrol, hdl": {"optimal düzey <":5,
                        "artmış kardiovasküler hastalık riski >":5 },
    "kolestrol, ldl/ kolestrol, hdl oranı": {"optimal düzey <":2,
                                            "artmış kardiovasküler hastalık riski >":5},
    "apolipoprotein a1": None,
    "apolipoprotein a2": None,
    "apolipoprotein b100": None,
    "apo-b100 / apo-a1 oranı": {"optimal düzey <":0.6,
                                "artmış kardiovasküler hastalık riski >":0.8},
    "total apob taşıyan partikül sayısı, total apob-p": {"optimal düzey <":140,
                                                        "artmış kardiovasküler hastalık riski >":200},
    "ldl partikül sayısı, ldl-p": {"optimal düzey <":100,
                                    "artmış kardiovasküler hastalık riski >":130},
    "idl partikül sayısı, idl-p": {"optimal düzey <":7,
                                    "artmış kardiovasküler hastalık riski >":10},
    "vldl partikül sayısı, vldl-p": {"optimal düzey <":12,
                                    "artmış kardiovasküler hastalık riski >":18}
}

LAF = {
    "ldl1-partikül sayısı": {"optimal düzey <": 140,
                            "artmış kardiovasküler hastalık riski >":190},
    "ldl2-partikül sayısı": {"optimal düzey <": 150,
                            "artmış kardiovasküler hastalık riski >":200},
    "ldl3-partikül sayısı": {"optimal düzey <": 190,
                            "artmış kardiovasküler hastalık riski >":260},
    "ldl4-partikül sayısı": {"optimal düzey <": 230,
                            "artmış kardiovasküler hastalık riski >":330},
    "ldl5-partikül sayısı": {"optimal düzey <": 290,
                            "artmış kardiovasküler hastalık riski >":400},
    "ldl6-partikül sayısı": {"optimal düzey <": 300,
                            "artmış kardiovasküler hastalık riski >": 450}
}

ALAT = {
    "ldl-apo-b100": {"optimal düzey <":7,
                    "artmış kardiovasküler hastalık riski >":10},
    "idl-apo-b100": {"optimal düzey <":4,
                    "artmış kardiovasküler hastalık riski >":6},
    "vldl-apo-b100": {"optimal düzey <":6,
                    "artmış kardiovasküler hastalık riski >":1},
    "ldl-trigliserid": {"optimal düzey <":24,
                    "artmış kardiovasküler hastalık riski >":28},
    "idl-trigliserid": {"optimal düzey <":6,
                    "artmış kardiovasküler hastalık riski >":1},
    "vldl-trigliserid": {"optimal düzey <":6,
                    "artmış kardiovasküler hastalık riski >":9}
}

LKE = {
    "ldl serbest kolestrol": None,
    "hdl serbest kolestrol": None,
    "ldl-serbest kolestrol / ldl-kolestrol": {"optimal düzey <":0.5,
                                            "artmış kardiovasküler hastalık riski":[">=",0.5]},
    "hdl-serbest kolestrol / hdl-kolestrol": {"optimal düzey <":0.5,
                                            "artmış kardiovasküler hastalık riski":[">=",0.5]}
}

def Lead(group_name):
    if group_name == "nmr_lipoporotein_profili":
        return NLP
    elif group_name == "ldl_alt_fraksi̇yonları":
        return LAF
    elif group_name == "aterojeni̇k_li̇poprotei̇nlerde_apo_b100_ve_tri̇gli̇seri̇d":
        return ALAT
    elif group_name == "li̇poprotei̇n_kolestrol_esteri̇fi̇kasyonu":
        return LKE
