import matplotlib.pyplot as plt
import numpy as np
# One box look
def o_chart(patient, ref, constant):
    
    x = np.linspace(x_min, x_max, 1000)
    y = np.ones(1000)

    # Adjust the x-axis limits if the patient value is outside the range
    if patient < ref:
        x_min = patient - constant
    if patient > ref:
        x_max = patient + constant

    # Creating a gradient background from lowest to highest x, changing at the reference point
    range_values = (x - x_min) / (x_max - x_min)
    range_values = range_values.reshape(1, -1)  # Reshaping for broadcasting

    plt.figure(figsize=(6, 1))

    plt.imshow(range_values, cmap='RdYlGn_r', aspect='auto', extent=[x_min, x_max, 0, 1], alpha=0.7)
    plt.plot(x, y, color='black')

    plt.gca().get_yaxis().set_visible(False)

    plt.axvline(x=ref, color='black', linestyle='-', linewidth=2)

    #plt.text(ref - constant/10, 0.5, keylwst, rotation=90, ha='center', va='center', fontsize=8)
    #plt.text(ref + constant/10, 0.5, keybgst, rotation=-90, ha='center', va='center', fontsize=8)

    # Constant value
    custom_value = max(x_min, min(patient, x_max))
    plt.axvline(x=custom_value, color='red', linestyle='-', linewidth=2)
    
    return plt

def trial():
    constant = (3.5*150)/7
    fig = o_chart(170, 150, "optimal düzey <", "artmış kardiovasküler hastalık riski >", constant)
    plot_file = 'one.png'
    group_name = "Trial"
    from save_plot import insert_plot as IP
    IP(group_name, plot_file, fig)

#trial()