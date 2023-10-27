import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import io 
import os
import test_groups as TG
import seaborn as sns
from docx import Document


# Set the custom colormap
cmap_colors = [(0.0000001, 0.3, 0), (0.95, 0.95, 0), (5, 0, 0)]
cmap = mcolors.LinearSegmentedColormap.from_list("custom_color_map", cmap_colors, N=10000)

sns.set()

def create_date_folder(group_name):
    folder_name = group_name
    folder_path = os.path.join("Tüm Belgeler", folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    return folder_path

def tk_chart(patient, lwst, bgst, constant, keylwst, keybgst, test_name):
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

    return plt

def e_chart(patient, limit, constant, keylwst, keybgst, test_name):
    fig, ax = plt.subplots(figsize=(5, 1))

    bars = [(patient, 0.1)]
    #(lwst, bgst - lwst), 
    ax.broken_barh(bars, (0, 1), facecolors="None")
    
    ax.set_xlim(abs(limit - constant), limit + constant)
    
    ax.yaxis.set_ticklabels([])
    
    x_ticks = [limit, limit, patient]
    x_labels = [f"{keylwst[-1]}{limit}", f"{keybgst[-1]}{limit}", str(patient)]
    
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_labels, rotation="vertical")
    
    ax.get_xticklabels()[0].set_horizontalalignment('right')
    ax.get_xticklabels()[1].set_horizontalalignment('left')
    
    ax.imshow(np.arange(0, 2*limit + 1).reshape(1, -1), cmap=cmap, aspect='auto', extent=[0, 2*limit, 0, 1])
    
    ax.add_patch(plt.Rectangle((0, 0), limit + constant, 1, fill=False, edgecolor='black', linewidth=2))
    
    plt.grid(False)
    plot_bytes = io.BytesIO()  # Create a BytesIO buffer to save the plot
    plt.savefig(plot_bytes, format="png")  # Save the plot as bytes

    # Write the bytes to the document
    document.write(plot_bytes.getvalue())

def b_chart(patient, lwst, opt, bgst, keylwst, keybgst, test_name,  *extra_limits):
    fig, ax = plt.subplots(figsize=(5, 1))

    # Ensure there are at least three limits
    if len(extra_limits) < 1:
        raise ValueError("At least three limits (lowest, optimum, highest) must be provided.")
    
    # Calculate the width for each bar
    bar_widths = [opt - lwst, bgst - opt] + [extra_limits[i + 1] - extra_limits[i] for i in range(0, len(extra_limits), 2)]
    
    # Create a list of bars with their widths
    bars = [(lwst, bar_widths[0], 0.1), (opt, bar_widths[1], 0.1)] + [(extra_limits[i], bar_widths[i+2], 0.1) for i in range(0, len(extra_limits), 2)]
    
    ax.broken_barh(bars, (0, 1), facecolors="None")
    
    min_limit = min(lwst, *extra_limits)
    max_limit = max(bgst, *extra_limits)
    
    ax.set_xlim(min_limit, max_limit)
    
    ax.yaxis.set_ticklabels([])
    
    x_ticks = [lwst, opt, bgst] + list(extra_limits)
    x_labels = [f"{str(limit)}" for limit in x_ticks]
    
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_labels, rotation="vertical")
    
    ax.get_xticklabels()[0].set_horizontalalignment('right')
    ax.get_xticklabels()[-1].set_horizontalalignment('left')
    
    ax.imshow(np.arange(0, max_limit - min_limit + 1).reshape(1, -1), cmap=cmap, aspect='auto', extent=[0, max_limit - min_limit, 0, 1])
    
    ax.add_patch(plt.Rectangle((0, 0), max_limit - min_limit, 1, fill=False, edgecolor='black', linewidth=2))
    
    plt.grid(False)
    plt.savefig(document, format="png")

def decision(patient,lwst, bgst, constant, keylwst, keybgst, keyc, test_name, *extra_limits):
    if lwst == bgst:
    #send to one seperation onew < | onew >
        plt = e_chart(patient, lwst, constant, keylwst, keybgst, test_name)
        chart_file = f"{test_name}.png"
        plt.savefig(os.path.join(folder_path, chart_file), bbox_inches="tight")
    elif keyc == 2:
        # send to two seperation onew < | middle | onew >
        # done
        tk_chart(patient, lwst, bgst, constant, keylwst, keybgst, test_name)
    elif keyc > 2:
        # send to more than two seperation onew < and value == lwst |  | | one w > and value == bgst
        b_chart(patient, lwst, opt, bgst, constant, keylwst, keybgst, test_name, *extra_limits)

def Leader(group_name, test_name, patient_val):
    test = TG.Lead(group_name)[test_name]
    keyc = len(test)
    lwst, bgst, keylwst, keybgst = float('inf'), 0, "", ""
    # keys for lwst and bgst isnt distinct when lwst == bgst
    for key, value in test.items():
        if value < lwst:
            lwst, keylwst = value, key
        if value > bgst:
            bgst, keybgst = value, key
    # const == 0 for lwst == biggest, fix it
    constant = 2 * (abs(lwst - bgst)) / 3
    
    decision(patient_val ,lwst, bgst, constant, keylwst, keybgst, keyc, test_name, *extra_limits)

def create_or_open_docx(docx_file):
    doc = Document()
    if docx_file and os.path.exists(docx_file):
        doc = Document(docx_file)
    doc.save(docx_file)


Leader("nmr_lipoporotein_profili", "trigliserid", 17)