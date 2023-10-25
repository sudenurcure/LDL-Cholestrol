from matplotlib import pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns
import numpy as np
from test_groups import ldl_alt_fraksi̇yonları
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

def generic(patient):
    fig, ax = plt.subplots(figsize=(5, 1))

    # Create a horizontal bar-like chart
    bars = [(lwst, bgst - lwst), (patient, 0.1)]

    # Draw the gradient background using the custom colormap
    ax.imshow(np.arange(0, lwst + bgst + 1).reshape(1, -1), cmap=custom_cmap, aspect='auto', extent=[0, lwst + bgst, 0, 1])

    # Draw the bars with custom markers
    ax.broken_barh(bars, (0, 1), facecolors = "None")

    # Set the x-axis limits
    ax.set_xlim(abs(lwst - constant), bgst + constant)
    ax.tick_params(direction='out', pad=-47, grid_alpha = 1)
    # Remove y-axis ticks and labels
    ax.yaxis.set_ticklabels([])
    
    # Set custom x-axis labels
    ax.set_xticks([lwst, bgst, patient])
    ax.set_xticklabels([keylwst[-1] + str(lwst), keybgst[-1] + str(bgst), str(patient)], rotation="vertical")
    ax.get_xticklabels()[0].set_horizontalalignment('right')
    ax.get_xticklabels()[1].set_horizontalalignment('left')

    plt.grid(False)
    plt.show()


key = "ldl1-partikül sayısı"
"""input("enter testname (ldl1-partikül sayısı):" )"""
patient = 150
"""input("patient value :")"""

if ldl_alt_fraksi̇yonları[key] == None:
    pass
testname = ldl_alt_fraksi̇yonları[key] #prob a lower dict
keyc = len(testname)

#find lwst and bgst
for key,value in testname.items():
    if value < lwst:
        lwst = value
        keylwst = key
    if value > bgst:
        bgst = value
        keybgst = key
const = 2*(abs(lwst-bgst))/3
constant = const
#decide the look of the plot
if lwst == bgst:
    #send to one seperation onew < | onew >
    pass
elif keyc == 2:
    # send to two seperation onew < | middle | onew >
    generic(patient)
elif keyc > 2:
    # send to more than two seperation onew < and value == lwst |  | | one w > and value == bgst
    pass

