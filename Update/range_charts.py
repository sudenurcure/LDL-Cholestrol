import matplotlib.pyplot as plt
import numpy as np

def t_chart(patient, lwst, bgst, keylwst, keybgst, constant):
    x_min = lwst - constant
    x_max = bgst + constant

    x = np.linspace(x_min, x_max, 1000)
    y = np.ones(1000)

    range_values = np.where(x <= lwst, 0, np.where(x > bgst, 1, (x - lwst) / (bgst - lwst)))
    range_values = range_values.reshape(1, -1)

    fig, ax = plt.subplots(figsize=(6, 0.5))

    ax.imshow(range_values, cmap='RdYlGn_r', aspect='auto', extent=[x_min, x_max, 0, 1], alpha=0.7)

    ax.plot(x, y, color='black')

    ax.get_yaxis().set_visible(False)
    ax.get_xaxis().set_visible(False)

    for limit, label in zip([lwst, bgst], [keylwst, keybgst]):
        ax.axvline(x=limit, color='black', linestyle='-', linewidth=1.5)
        ax.annotate(str(limit), xy =(limit, 0), 
             xytext =(limit, -0.50), ha='center', va='center', fontsize = 14,
             arrowprops = dict(facecolor ='black',headwidth=7, headlength=6))

    # Patient
    custom_value = max(x_min, min(patient, x_max))
    linewidth = 2 if x_min < patient < x_max else 5
    ax.axvline(x=custom_value, color='red', linestyle='-', linewidth=linewidth)

    if patient < x_max and patient > x_min:
        ax.annotate(str(patient), xy =(patient, 1), 
            xytext =(patient, 1.45), ha='center', va='center', fontsize = 14,
            arrowprops = dict(facecolor ='red',headwidth=7, headlength=6))
    elif patient <= x_min:
        ax.annotate(str(patient), xy =(x_min + constant/25, 1), fontsize = 14,
            xytext =(x_min + constant/25, 1.45), ha='center', va='center',
            arrowprops = dict(facecolor ='red',headwidth=7, headlength=6))
    else:
        ax.annotate(str(patient), xy =(x_max - constant/25, 1), fontsize = 14,
                xytext =(x_max - constant/25, 1.45), ha='center', va='center',
                arrowprops = dict(facecolor ='red',headwidth=7, headlength=6))

    #plt.show()
    return plt

def trial():
    constant = 2 * (abs(27 - 20)) / 3
    t_chart(7, 20, 27, "<", ">", constant)

#trial()

