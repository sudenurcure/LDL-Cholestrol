from matplotlib import pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns
import numpy as np
import test_groups as TG
sns.set()

lwst = 999999
keylwst=""
bgst = 0
keybgst=""
constant = 2*(lwst-bgst)/3


# Create a custom colormap that transitions from green to red
colors = [(0.0000001, 0.3, 0), (0.95, 0.95, 0), (5, 0, 0)]
n_bins = 10000
cmap_name = "custom_color_map"
custom_cmap = plt.cm.colors.LinearSegmentedColormap.from_list(cmap_name, colors, N=n_bins)

def generic(patient,lwst, bgst, constant, keylwst, keybgst, document):
    fig, ax = plt.subplots(figsize=(5, 1))

    bars = [(lwst, bgst - lwst), (patient, 0.1)]
    ax.broken_barh(bars, (0, 1), facecolors = "None")
    ax.set_xlim(abs(lwst - constant), bgst + constant)
    
    #Labels
    ax.yaxis.set_ticklabels([])
    ax.set_xticks([lwst, bgst, patient])
    ax.tick_params(direction='out', pad=-47, grid_alpha = 1)
    ax.set_xticklabels([keylwst[-1] + str(lwst), keybgst[-1] + str(bgst), str(patient)], rotation="vertical")
    
    ax.get_xticklabels()[0].set_horizontalalignment('right')
    ax.get_xticklabels()[1].set_horizontalalignment('left')
    
    #Aesthetic
    ax.imshow(np.arange(0, lwst + bgst + 1).reshape(1, -1), cmap=custom_cmap, aspect='auto', extent=[0, lwst + bgst, 0, 1])
    ax.add_patch(plt.Rectangle((0,0), bgst + constant, 1, fill=False, edgecolor='black', linewidth=2))

    plt.grid(False)
    plt.show()
    plt.savefig(document, format="png")

def Decision(patient,lwst, bgst, constant, keylwst, keybgst, keyc, document):
    if lwst == bgst:
    #send to one seperation onew < | onew >
        pass
    elif keyc == 2:
        # send to two seperation onew < | middle | onew >
        generic(patient, lwst, bgst, constant, keylwst, keybgst, document)
    elif keyc > 2:
        # send to more than two seperation onew < and value == lwst |  | | one w > and value == bgst
        pass


def Direct(group_name, test_name, patient_val, document):
    """
    Take Test Group Name, the test in it, the patient value and direct document to save the images.
    """
    test = TG.Lead(group_name)[test_name]
    keyc = len(test)
    lwst = 999999
    bgst = 0
    keylwst=""
    keybgst=""

    #find lwst and bgst
    for key,value in test.items():
        if value < lwst:
            lwst = value
            keylwst = key
        if value > bgst:
            bgst = value
            keybgst = key

    constant = 2*(abs(lwst-bgst))/3

    Decision(patient_val ,lwst, bgst, constant, keylwst, keybgst, keyc, document)

