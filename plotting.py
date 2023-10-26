import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import test_groups as TG
import seaborn as sns

# Set the custom colormap
cmap_colors = [(0.0000001, 0.3, 0), (0.95, 0.95, 0), (5, 0, 0)]
cmap = mcolors.LinearSegmentedColormap.from_list("custom_color_map", cmap_colors, N=10000)

sns.set()

def generic_chart(patient, lwst, bgst, constant, keylwst, keybgst, document):
    fig, ax = plt.subplots(figsize=(5, 1))

    bars = [(lwst, bgst - lwst), (patient, 0.1)]
    ax.broken_barh(bars, (0, 1), facecolors="None")
    
    ax.set_xlim(abs(lwst - constant), bgst + constant)
    
    ax.yaxis.set_ticklabels([])
    
    x_ticks = [lwst, bgst, patient]
    x_labels = [f"{keylwst[-1]}{lwst}", f"{keybgst[-1]}{bgst}", str(patient)]
    
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_labels, rotation="vertical")
    
    ax.get_xticklabels()[0].set_horizontalalignment('right')
    ax.get_xticklabels()[1].set_horizontalalignment('left')
    
    ax.imshow(np.arange(0, lwst + bgst + 1).reshape(1, -1), cmap=cmap, aspect='auto', extent=[0, lwst + bgst, 0, 1])
    
    ax.add_patch(plt.Rectangle((0, 0), bgst + constant, 1, fill=False, edgecolor='black', linewidth=2))
    
    plt.grid(False)
    plt.savefig(document, format="png")

def decision(patient,lwst, bgst, constant, keylwst, keybgst, keyc, document):
    if lwst == bgst:
    #send to one seperation onew < | onew >
        generic_chart(patient, lwst, bgst, constant, keylwst, keybgst, document)
    elif keyc == 2:
        # send to two seperation onew < | middle | onew >
        # done
        generic_chart(patient, lwst, bgst, constant, keylwst, keybgst, document)
    elif keyc > 2:
        # send to more than two seperation onew < and value == lwst |  | | one w > and value == bgst
        generic_chart(patient, lwst, bgst, constant, keylwst, keybgst, document)

def Leader(group_name, test_name, patient_val, document):
    test = TG.Lead(group_name)[test_name]
    keyc = len(test)
    lwst, bgst, keylwst, keybgst = float('inf'), 0, "", ""
    
    for key, value in test.items():
        if value < lwst:
            lwst, keylwst = value, key
        if value > bgst:
            bgst, keybgst = value, key
    
    constant = 2 * (abs(lwst - bgst)) / 3
    
    decision(patient_val ,lwst, bgst, constant, keylwst, keybgst, keyc, document)
