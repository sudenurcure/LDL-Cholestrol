import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

# Set the custom colormap
cmap_colors = [(0.0000001, 0.3, 0), (0.95, 0.95, 0), (5, 0, 0)]
cmap = mcolors.LinearSegmentedColormap.from_list("custom_color_map", cmap_colors, N=1000000)

def b_chart(patient, lwst, bgst, keylwst, keybgst, constant, *extra_limits,):
    limits = [lwst, bgst] + list(remaining_limits.values())
    labels = [keylwst, keybgst] + list(remaining_limits.keys())
    x_min = min(lwst, bgst) - constant
    x_max = max(lwst, bgst) + constant

    if patient < x_min:
        x_min = patient - constant
    if patient > x_max:
        x_max = patient + constant

    x = np.linspace(x_min, x_max, 1000)
    y = np.ones(1000)
    

    range_values = np.where(x <= lwst, 0, np.where(x > bgst, 1, (x - lwst) / (bgst - lwst)))
    range_values = range_values.reshape(1, -1)

    fig, ax = plt.subplots(figsize=(6, 1))
    plt.imshow(range_values, cmap='RdYlGn_r', aspect='auto', extent=[x_min, x_max, 0, 1], alpha=0.7)
    plt.plot(x, y, color='black')
    plt.gca().get_yaxis().set_visible(False)

""" limits = [lwst, bgst]
    tick_labels = [keylwst, keybgst]"""



    #bars = [(patient,bgst-patient), (lwst, bgst - lwst)]

"""    for extra in extra_limits:
        for values in extra.values():
            #bars = bars + [(values, bgst-values)]
            limits = limits + values"""

    for limit, label in zip(limits, tick_labels):
        plt.axvline(x=limit, color='black', linestyle='--', linewidth=1)
        plt.text(limit - 0.2, 0.5, label, rotation=90, ha='center', va='center', fontsize=8)
 """       if limit == lwst:
            plt.text(limit - 0.2, 0.5, label, rotation=90, ha='center', va='center', fontsize=8)
        elif limit == bgst:
            plt.text(limit + 0.2, 0.5, label, rotation=-90, ha='center', va='center', fontsize=8)"""

    ax.broken_barh(bars, (0, 1), facecolors="None")
    
    x_ticks = [lwst, bgst, patient] + [values for values in (values for extra in extra_limits for values in extra.values())]
    x_labels = [keylwst, keybgst, str(patient)] + [f"{limit}" for limit in (values for extra in extra_limits for values in extra.values())]

    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_labels, rotation="vertical")
    
    #ax.imshow(np.arange(0, lwst + bgst + 1).reshape(1, -1), cmap=cmap, aspect='auto', extent=[0, lwst + bgst, 0, 1])
    
    plt.grid(False)
    return fig

def trial():
    x = {"kardiyovasküler hastalığı olanlarda optimal düzey <":7,
                        "kardiyovasküler hastalığı olmayanlarda optimal düzey <":10,
                        "artmış kardiovasküler hastalık riski >":13}
    
    lwst, bgst, keylwst, keybgst = float('inf'), 0, "", "" # define lowest, highest limits and its keys
    
    for key, value in x.items(): # find lowest and highest limits
        if value < lwst:
            lwst, keylwst = value, key
        if value > bgst:
            bgst, keybgst = value, key

    remaining_limits = {k: v for k, v in x.items() if v not in [lwst,bgst]}
    constant = 2 * (abs(lwst - bgst)) / 3

    fig = b_chart(15, lwst, bgst, keylwst, keybgst, constant, remaining_limits)

    plot_file = 'multy.png'
    group_name = "Trial"
    from save_plot import insert_plot as IP
    IP(group_name, plot_file, fig)

trial()