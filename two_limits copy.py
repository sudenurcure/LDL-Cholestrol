import matplotlib.pyplot as plt
import numpy as np

def one_limit(patient, ref, keylwst, keybgst, constant):
    x_min = ref - constant
    x_max = ref + constant

    x = np.linspace(x_min, x_max, 1000)
    y = np.ones(1000)

    # Adjust the x-axis limits if the patient value is outside the range
    if patient < x_min:
        x_min = patient - constant
    if patient > x_max:
        x_max = patient + constant

    # Creating a gradient background for healthy and sick individuals within the specified x-range
    range_values = np.where(x <= ref, 0, np.where(x > ref, 1, (x - ref) / (ref - ref)))
    range_values = range_values.reshape(1, -1)  # Reshaping for broadcasting

    plt.figure(figsize=(6, 1))

    plt.imshow(range_values, cmap='RdYlGn_r', aspect='auto', extent=[x_min, x_max, 0, 1], alpha=0.7)
    plt.plot(x, y, color='black')

    plt.gca().get_yaxis().set_visible(False)

    tick_labels = [keylwst, keybgst]

    plt.axvline(x=ref, color='black', linestyle='--', linewidth=1)

    plt.text(ref - 0.2, 0.5, keylwst, rotation=90, ha='center', va='center', fontsize=8)
    plt.text(ref + 0.2, 0.5, keybgst, rotation=-90, ha='center', va='center', fontsize=8)

    # Constant value
    custom_value = max(x_min, min(patient, x_max))
    plt.axvline(x=custom_value, color='red', linestyle='-', linewidth=2)
    return plt

def trial():
    constant = (3.5*150)/7
    fig = one_limit(170, 150, "optimal düzey <", "artmış kardiovasküler hastalık riski >", constant)
    plot_file = 'two.png'
    group_name = "Trial"
    from save_plot import insert_plot as IP
    IP(group_name, plot_file, fig)

trial()