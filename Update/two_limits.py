import matplotlib.pyplot as plt
import numpy as np

def t_chart(patient, lwst, bgst, keylwst, keybgst, constant):
    x_min = lwst - constant
    x_max = bgst + constant

    x = np.linspace(x_min, x_max, 1000)
    y = np.ones(1000)

    range_values = np.where(x <= lwst, 0, np.where(x > bgst, 1, (x - lwst) / (bgst - lwst)))
    range_values = range_values.reshape(1, -1)

    plt.figure(figsize=(6, 1))

    plt.imshow(range_values, cmap='RdYlGn_r', aspect='auto', extent=[x_min, x_max, 0, 1], alpha=0.7)
    plt.plot(x, y, color='black')

    plt.gca().get_yaxis().set_visible(False)
    plt.gca().get_xaxis().set_visible(False)

    for limit, label in zip([lwst, bgst], [keylwst, keybgst]):
        plt.axvline(x=limit, color='black', linestyle='-', linewidth=1.5)
        plt.text(limit - constant/10, 0.5, label, rotation=90, ha='center', va='center', fontsize=7)

    # Patient
    custom_value = max(x_min, min(patient, x_max))
    linewidth = 2 if x_min < patient < x_max else 5
    plt.axvline(x=custom_value, color='red', linestyle='-', linewidth=linewidth)
    if patient < x_max and patient > x_min:
        plt.text(patient - constant/25, 0.5, patient, rotation=90, ha='center', va='center', fontsize=7, color = "red")
    elif patient <= x_min:
        plt.text(x_min + constant/25, 0.5, patient, rotation=90, ha='left', va='center', fontsize=7, color = "red")
    else:
        plt.text(x_max - constant/25, 0.5, patient, rotation=90, ha='right', va='center', fontsize=7, color = "red")

    return plt

def trial():
    constant = 2 * (abs(27 - 20)) / 3
    fig = t_chart(7, 20, 27, "<", ">", constant)
    plot_file = 'two.png'
    group_name = "Trial"
    from save_plot import insert_plot as IP
    IP(group_name, plot_file, fig)

#trial()
