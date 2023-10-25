
tests = ["nmr_lipoporotein_profili","ldl_alt_fraksi̇yonları","aterojeni̇k_li̇poprotei̇nlerde_apo_b100_ve_tri̇gli̇seri̇d",
            "li̇poprotei̇n_kolestrol_esteri̇fi̇kasyonu"]

nmr_lipoporotein_profili = {
    "trigliserid": {"optimal düzey": ["<",150], 
                    "artmış kardiovasküler hastalık riski":[">",150]},
    "kolestrol, total": {"optimal düzey": ["<",200],
                        "artmış kardiovasküler hastalık riski":[">",200]},
    "kolestrol, ldl": {"kardiyovasküler hastalığı olanlarda optimal düzey": ["<",70],
                        "kardiyovasküler hastalığı olmayanlarda optimal düzey": ["<",100],
                        "artmış kardiovasküler hastalık riski":[">",130]},
    "kolestrol, hdl": {"optimal düzey": ["<",50],
                        "artmış kardiovasküler hastalık riski":[">",50] },
    "kolestrol, ldl/ kolestrol, hdl oranı": {"optimal düzey": ["<",2],
                                            "artmış kardiovasküler hastalık riski":[">",5]},
    "apolipoprotein a1": None,
    "apolipoprotein a2": None,
    "apolipoprotein b100": None,
    "apo-b100 / apo-a1 oranı": {"optimal düzey": ["<",0.6],
                                "artmış kardiovasküler hastalık riski":[">",0.8]},
    "total apob taşıyan partikül sayısı, total apob-p": {"optimal düzey": ["<",1400],
                                                        "artmış kardiovasküler hastalık riski":[">",2000]},
    "ldl partikül sayısı, ldl-p": {"optimal düzey": ["<",1000],
                                    "artmış kardiovasküler hastalık riski":[">",1300]},
    "idl partikül sayısı, idl-p": {"optimal düzey": ["<",70],
                                    "artmış kardiovasküler hastalık riski":[">",100]},
    "vldl partikül sayısı, vldl-p": {"optimal düzey": ["<",120],
                                    "artmış kardiovasküler hastalık riski":[">",180]}
}

ldl_alt_fraksi̇yonları = {
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

aterojeni̇k_li̇poprotei̇nlerde_apo_b100_ve_tri̇gli̇seri̇d = {
    "ldl-apo-b100": {"optimal düzey": ["<",70],
                    "artmış kardiovasküler hastalık riski":[">",100]},
    "idl-apo-b100": {"optimal düzey": ["<",4],
                    "artmış kardiovasküler hastalık riski":[">",6]},
    "vldl-apo-b100": {"optimal düzey": ["<",6],
                    "artmış kardiovasküler hastalık riski":[">",10]},
    "ldl-trigliserid": {"optimal düzey": ["<",24],
                    "artmış kardiovasküler hastalık riski":[">",28]},
    "idl-trigliserid": {"optimal düzey": ["<",6],
                    "artmış kardiovasküler hastalık riski":[">",10]},
    "vldl-trigliserid": {"optimal düzey": ["<",60],
                    "artmış kardiovasküler hastalık riski":[">",90]}
}

li̇poprotei̇n_kolestrol_esteri̇fi̇kasyonu = {
    "ldl serbest kolestrol": None,
    "hdl serbest kolestrol": None,
    "ldl-serbest kolestrol / ldl-kolestrol": {"optimal düzey": ["<",0.5],
                                            "artmış kardiovasküler hastalık riski":[">=",0.5]},
    "hdl-serbest kolestrol / hdl-kolestrol": {"optimal düzey": ["<",0.5],
                                            "artmış kardiovasküler hastalık riski":[">=",0.5]}
}

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