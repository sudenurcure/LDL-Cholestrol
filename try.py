import matplotlib.pyplot as plt
import numpy as np

# Define colors for each category
colors = ['lightblue', 'lightgreen', 'lightcoral']

def b_chart(patient, lwst, bgst, keylwst, keybgst, constant, *extra_limits):
    fig, ax = plt.subplots(figsize=(5, 1))

    # Define the categories (e.g., patient, lwst, bgst, and extras)
    categories = [patient, lwst, bgst] + [value for extra in extra_limits for value in extra.values()]
    category_names = [str(patient), keylwst, keybgst] + [key for extra in extra_limits for key in extra.keys()]
    colors = ['lightblue', 'lightgreen', 'lightcoral'] * (len(categories) // 3)  # Assign colors to categories

    # Calculate the bar widths based on the category values
    widths = [constant]  # For patient
    for value in categories[1:]:
        widths.append(value - categories[categories.index(value) - 1])

    # Create bars
    bars = []
    left = 0
    for width, color in zip(widths, colors):
        bars.append((width, 0.1, color))
        left += width

    ax.broken_barh(bars, (0, 1), facecolors=[bar[2] for bar in bars])

    ax.set_xlim(0, bgst + constant)
    ax.yaxis.set_ticklabels([])

    ax.set_xticks([0] + [left for left in widths])
    ax.set_xticklabels(category_names, rotation="vertical")

    plt.grid(False)
    return fig

def trial():
    x = {
        "kardiyovasküler hastalığı olanlarda optimal düzey <": 7,
        "kardiyovasküler hastalığı olmayanlarda optimal düzey <": 10,
        "artmış kardiovasküler hastalık riski >": 13
    }

    lwst, bgst, keylwst, keybgst = float('inf'), 0, "", ""  # define lowest, highest limits and their keys

    for key, value in x.items():  # find lowest and highest limits
        if value < lwst:
            lwst, keylwst = value, key
        if value > bgst:
            bgst, keybgst = value, key

    remaining_limits = {k: v for k, v in x.items() if v not in [lwst, bgst]}
    constant = 2 * (abs(lwst - bgst)) / 3

    fig = b_chart(15, lwst, bgst, keylwst, keybgst, constant, remaining_limits)

    plot_file = 'multy.png'
    group_name = "Trial"
    from save_plot import insert_plot as IP
    IP(group_name, plot_file, fig)

trial()
