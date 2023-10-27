import test_groups as TG
from save_plot import insert_plot as IP
from two_limits import tk_chart as TL
from one_limit import e_chart as OL
from mult_limits import b_chart as ML


def Sorter(group_name, test_name, patient_val):
    test = TG.Lead(group_name)[test_name] # references that we are gonna use, dictionary
    lwst, bgst, keylwst, keybgst = float('inf'), 0, "", "" # define lowest, highest limits and its keys
    
    for key, value in test.items(): # find lowest and highest limits
        if value < lwst:
            lwst, keylwst = value, key
        if value > bgst:
            bgst, keybgst = value, key
    
    l_remaining_limits = len(test) -2 # check how many reference limit we have left
    remaining_limits = test.copy()
    remaining_limits = [remaining_limits.pop(x) for x in [lwst, bgst]]

    if lwst == bgst:
        ref = lwst
        constant = (3.5*ref)/7

        for key in test.keys():
            if key.find("<") == -1:
                bgst == key
            else:
                lwst == key
        fig = OL(patient_val, ref, keylwst, keybgst, constant)
        plot_file = f'{test_name}.png'
        IP(group_name, plot_file, fig)
    elif l_remaining_limits > 0:
        constant = 2 * (abs(lwst - bgst)) / 3
        fig = ML(patient_val, lwst, bgst, keylwst, keybgst, constant, remaining_limits)
        IP(group_name, plot_file, fig)
        # send to >2 limit, needs *extra_limits
    else:
        # send to two limits, has a constant
        constant = 2 * (abs(lwst - bgst)) / 3
        fig = TL(patient_val, lwst, bgst, keylwst, keybgst, constant)
        plot_file = f'{test_name}.png'
        IP(group_name, plot_file, fig)
    


