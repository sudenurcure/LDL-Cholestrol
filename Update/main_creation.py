import ReferenceDictionary as dd
from colored_box_image import create_colored_box_image as cbox
from range_charts import t_chart
from save_plot import insert_plot as IP

def conditional(df, dfdict):    
    output = open("problem_output.txt","w")

    for test , pval in dfdict.items():
        #get name and unit of the test seperately
        usename = test.replace(" [mg/dL]", "").replace(" [nmol/L]", "").replace(" [-/-]", "")
        if "[mg/dL]" in test:
            unit =  "[mg/dL]"
        elif "[nmol/L]" in test:
            unit = "[nmol/L]"
        else:
            unit = None

        #check the test's existence
        try:
            attribute = getattr(dd.TESTS(),usename)
        except:
            output.write(f"{test} is not in tests dictionary.\n")
        else:
            try:
                    attribute["Optimal"]
            except:
                try:
                    attribute["OptimalnCD"] #Do these exist?
                    attribute["OptimalCD"]
                except:
                    print("Problem")
                    pass
                else: # more than two reference values
                    while True:
                        past = input("History of any Cardiovascular Events? y/n ")
                        if past == "n":
                            optval = float(attribute["OptimalnCD"][2:].strip())
                            riskval = float(attribute["Risk"][2:].strip())
                            constant = 2 * (abs(optval - riskval)) / 3
                            
                            fig = t_chart(df[test], optval, riskval, attribute["OptimalnCD"] ,attribute["Risk"], constant)
                            plot_file = f'{usename}.png'
                            IP(plot_file, fig)
                            
                            cbox(usename, df[test], "noref", unit)
                            break
                        elif past == "y":
                            optval = float(attribute["OptimalCD"][2:].strip())
                            riskval = float(attribute["Risk"][2:].strip())
                            constant = 2 * (abs(optval - riskval)) / 3

                            fig = t_chart(df[test], optval, riskval, attribute["OptimalCD"] ,attribute["Risk"], constant)
                            plot_file = f'{usename}.png'
                            IP(plot_file, fig)

                            cbox(usename, df[test], "noref", unit)
                            break
                        else:
                            print("Wrong input.")
            else:
                if attribute["Optimal"] is None and attribute["Risk"] is None: #check for no reference
                    cbox(usename, pval, "noref", unit)
                elif attribute["Optimal"][2:].strip() == attribute["Risk"][2:].strip(): #check for one reference value
                    condition = f"{pval} {attribute}"
                    if pval == attribute["Optimal"][2:].strip():
                        cbox(usename, pval, "not boolean", unit)
                    elif eval(f"{pval} {attribute['Optimal']}"): # pval > or < Optimal w
                        cbox(usename, pval, False, unit)
                    else:
                        cbox(usename, pval, True, unit)
                        
                else: #two reference value
                    optval = float(attribute["Optimal"][2:].strip())
                    riskval = float(attribute["Risk"][2:].strip())
                    constant = 2 * (abs(optval - riskval)) / 3

                    fig = t_chart(df[test], optval, riskval, attribute["Optimal"] ,attribute["Risk"], constant) # or "Optimal" , "Risk" as line names
                    plot_file = f'{usename}.png'
                    IP(plot_file, fig)

                    cbox(usename, df[test], "noref", unit)
    output.close()

def calculated_LFLC(df):
    db = dd.TESTS.LFLC
    cLFLC = round(df["LDFC [mg/dL]"]/df["LDCH [mg/dL]"],2)

    optval = float(db["Optimal"][2:].strip())
    riskval = float(db["Risk"][2:].strip())
    constant = 2 * (abs(optval - riskval)) / 3

    fig = t_chart(cLFLC, optval, riskval, db["Optimal"] ,db["Risk"], constant)
    plot_file = 'LFLC.png'
    IP(plot_file, fig)

    cbox(plot_file.replace(".png",""), cLFLC, "noref")

def calculated_HFHC(df):
    db = dd.TESTS.HFHC
    cHFHC = round(df["HDFC [mg/dL]"]/df["HDCH [mg/dL]"],2)

    if eval(f"{cHFHC} {db['Optimal']}"):
        cbox("HFHC", cHFHC, False)
    else:
        cbox("HFHC", cHFHC, True)
