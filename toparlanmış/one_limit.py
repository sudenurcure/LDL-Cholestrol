import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import seaborn as sns

cmap_colors = [(0.0000001, 0.3, 0), (0.95, 0.95, 0), (5, 0, 0)]
cmap = mcolors.LinearSegmentedColormap.from_list("custom_color_map", cmap_colors, N=10000)

sns.set()

def e_chart(patient, ref, keylwst, keybgst, constant):
    fig, ax = plt.subplots(figsize=(5, 1))

    bars = [(patient, 0.1)]
    ax.broken_barh(bars, (0, 1), facecolors="None")
    
    ax.set_xlim(abs(ref - constant), ref + constant)
    
    ax.yaxis.set_ticklabels([])
    
    x_ticks = [ref, ref, patient]
    x_labels = [f"{keylwst[-1]}{ref}", f"{keybgst[-1]}{ref}", str(patient)]
    
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_labels, rotation="vertical")
    
    ax.get_xticklabels()[0].set_horizontalalignment('right')
    ax.get_xticklabels()[1].set_horizontalalignment('left')
    
    ax.imshow(np.arange(0, 2*ref + 1).reshape(1, -1), cmap=cmap, aspect='auto', extent=[0, 2*ref, 0, 1])
    
    ax.add_patch(plt.Rectangle((0, 0), ref + constant, 1, fill=False, edgecolor='black', linewidth=2))
    
    plt.grid(False)
    return fig