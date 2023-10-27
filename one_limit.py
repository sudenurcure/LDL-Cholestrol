import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import seaborn as sns

cmap_colors = [(0.0000001, 0.3, 0), (0.95, 0.95, 0), (5, 0, 0)]
cmap = mcolors.LinearSegmentedColormap.from_list("custom_color_map", cmap_colors, N=10000)

sns.set()

def e_chart(patient, ref, keylwst, keybgst, constant):
    fig, ax = plt.subplots(figsize=(5, 1))

    bars = [(ref, 0.1),(patient, 0.1)]
    ax.broken_barh(bars, (0, 1), facecolors = "None")
    #, edgecolors = "purple"
    
    ax.set_xlim(abs(ref - constant), ref + constant)
    
    ax.yaxis.set_ticklabels([])
    
    x_ticks = [ref, ref, patient]
    x_labels = [f"{keylwst}{ref}", f"{keybgst}{ref}", str(patient)]

    """ax.text(x=x1 + x2/2, 
                    y=i,
                    s=r[1]["Event"].values[0], 
                    ha='center', 
                    va='center',
                    color='white',
                   )"""
    
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_labels, rotation="vertical")
    
    ax.get_xticklabels()[0].set_horizontalalignment('right')
    ax.get_xticklabels()[1].set_horizontalalignment('left')
    
    ax.imshow(np.arange(0, 2*ref + 1).reshape(1, -1), cmap=cmap, aspect='auto', extent=[0, 2*ref, 0, 1])
    
    plt.grid(False)
    return fig

def trial():
    constant = (3.5*150)/7
    fig = e_chart(170, 150, "optimal düzey <", "artmış kardiovasküler hastalık riski >", constant)
    plot_file = 'one.png'
    group_name = "Trial"
    from save_plot import insert_plot as IP
    IP(group_name, plot_file, fig)

trial()