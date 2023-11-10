import matplotlib.pyplot as plt
import numpy as np

def t_chart(patient, lwst, bgst, keylwst, keybgst, constant):
    x_min = min(lwst, bgst) - constant
    x_max = max(lwst, bgst) + constant

    x = np.linspace(x_min, x_max, 1000)
    y = np.ones(1000)

    # Adjust the x-axis limits if the patient value is outside the range
    if patient < x_min:
        x_min = patient - constant
    if patient > x_max:
        x_max = patient + constant

    # Creating a gradient background for healthy and sick individuals within the specified x-range
    range_values = np.where(x <= lwst, 0, np.where(x > bgst, 1, (x - lwst) / (bgst - lwst)))
    range_values = range_values.reshape(1, -1)  # Reshaping for broadcasting

    plt.figure(figsize=(6, 1))

    plt.imshow(range_values, cmap='RdYlGn_r', aspect='auto', extent=[x_min, x_max, 0, 1], alpha=0.7)
    plt.plot(x, y, color='black')

    plt.gca().get_yaxis().set_visible(False)

    limits = [lwst, bgst]

    tick_labels = [keylwst, keybgst]

    for limit, label in zip(limits, tick_labels):
        plt.axvline(x=limit, color='black', linestyle='-', linewidth=2)
        plt.text(limit - constant/10, 0.5, label, rotation=90, ha='center', va='center', fontsize=8)


    # Constant value
    custom_value = max(x_min, min(patient, x_max))
    plt.axvline(x=custom_value, color='red', linestyle='-', linewidth=2)
    return plt

def trial():
    constant = 2 * (abs(20 - 7)) / 3
    fig = t_chart(7, 20, 27, "optimal düzey <", "artmış kardiovasküler hastalık riski >", constant)
    plot_file = 'two.png'
    group_name = "Trial"
    from save_plot import insert_plot as IP
    IP(group_name, plot_file, fig)

trial()