import pandas as pd
import test_groups as TG
from save_plot import insert_plot as IP
from one_limit import o_chart as OL
from two_limits_old import t_chart as TL
from mult_limits import m_chart as ML
from worder import WordPreparation


def Sorter(group_name, test_name, patient_val):
    #patient_val = patient_val.values[0] if isinstance(patient_val, pd.Series) else patient_val
    test = TG.Lead(group_name)[test_name]  # References that we are going to use, a dictionary
    lwst, bgst = min(test.values()), max(test.values())
    keylwst, keybgst = [key for key, val in test.items() if val == lwst][0], [key for key, val in test.items() if val == bgst][0]

    if lwst == bgst:
        remaining_limits = {}
        l_remaining_limits = 0
    else:
        l_remaining_limits = len(test) - 2  # Check how many reference limits we have left
        remaining_limits = test.copy()
        remaining_limits.pop(keylwst)
        remaining_limits.pop(keybgst)

    if lwst == bgst:
        ref = lwst
        constant = (3.5*ref)/7
        
        for key in test.keys():
            if key.find("<") == -1:
                keybgst = key
            else:
                keylwst = key
        fig = OL(patient_val, ref, keylwst, keybgst, constant)
        plot_file = f'{test_name.lower().replace(" ","_").replace("/","%")}.png'
        IP(group_name, plot_file, fig)

    elif l_remaining_limits > 0:
        constant = 2 * (abs(lwst - bgst)) / 3
        fig = ML(patient_val, lwst, bgst, keylwst, keybgst, constant, remaining_limits)
        plot_file = f'{test_name.lower().replace(" ","_").replace("/","%")}.png'
        IP(group_name, plot_file, fig)
        # send to >2 limit, needs *extra_limits
    else:
        # send to two limits, has a constant
        constant = 2 * (abs(lwst - bgst)) / 3
        fig = TL(patient_val, lwst, bgst, keylwst, keybgst, constant)
        plot_file = f'{test_name.lower().replace(" ","_").replace("/","%")}.png'
        IP(group_name, plot_file, fig)
    


