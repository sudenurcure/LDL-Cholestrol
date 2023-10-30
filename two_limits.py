import matplotlib.pyplot as plt
import numpy as np

def two_limits(patient, lwst, bgst, keylwst, keybgst, constant):
    x_min = min(lwst, bgst) - constant  # Adjust the minimum x-axis value
    x_max = max(lwst, bgst) + constant  # Adjust the maximum x-axis value

    x = np.linspace(x_min, x_max, 1000)  # Adjust x range based on limits
    y = np.ones(1000)  # Constant y values

    # Adjust the x-axis limits if the patient value is outside the range
    if patient < x_min:
        x_min = patient - constant
    if patient > x_max:
        x_max = patient + constant

    # Creating a gradient background for healthy and sick individuals within the specified x-range
    range_values = np.where(x <= lwst, 0, np.where(x > bgst, 1, (x - lwst) / (bgst - lwst)))
    range_values = range_values.reshape(1, -1)  # Reshaping for broadcasting

    plt.figure(figsize=(6, 1))  # Set the figure size for a wider display

    plt.imshow(range_values, cmap='RdYlGn_r', aspect='auto', extent=[x_min, x_max, 0, 1], alpha=0.7)
    plt.plot(x, y, color='black')  # Add a line representing y = 1

    plt.gca().get_yaxis().set_visible(False)  # Hide the y-axis ticks

    # Define specific x-axis ticks and draw vertical lines at those points
    limits = [lwst, bgst]  # Set the positions of the ticks

    tick_labels = [keylwst, keybgst]  # Initial labels for the ticks

    for limit, label in zip(limits, tick_labels):
        plt.axvline(x=limit, color='black', linestyle='--', linewidth=1)
        if limit == lwst:
            plt.text(limit - 0.2, 0.5, label, rotation=90, ha='center', va='center', fontsize=8)
        else:
            plt.text(limit + 0.2, 0.5, label, rotation=-90, ha='center', va='center', fontsize=8)

    # Constant value represented as a highlighted vertical line, ensuring it's within the x-axis limits
    custom_value = max(x_min, min(patient, x_max))
    plt.axvline(x=custom_value, color='red', linestyle='-', linewidth=2)
    return plt

def trial():
    constant = 2 * (abs(5 - 10)) / 3
    fig = two_limits(7, 5, 10, "optimal düzey <", "artmış kardiovasküler hastalık riski >", constant)
    plot_file = 'two.png'
    group_name = "Trial"
    from save_plot import insert_plot as IP
    IP(group_name, plot_file, fig)

trial()