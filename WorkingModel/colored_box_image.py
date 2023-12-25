from save_plot import insert_plot as IP
import matplotlib.pyplot as plt

def create_colored_box_image(usename, value, sick, unit = None):
    if sick == True:
        box_color = '#EA0A0A'
    elif sick == False:
        box_color = '#22B20F'
    elif sick == "noref":
        box_color = 'white'
    else:
        box_color = '#F9AB06'

    usename = usename + "_box"

    fig, ax = plt.subplots(figsize=(2.85, 0.65))

    text = str(value)
    try:
        unit = unit.replace("[","").replace("]","")
    except:
        if sick == "noref":
            ax.text(0.5, 0.5, text, color='black', fontsize=20, va='center', ha='center')
        else:
            ax.text(0.5, 0.5, text, color='white', fontsize=20, va='center', ha='center')
    else:
        if sick == "noref":
            ax.text(0.5, 0.5, text+" "+unit, color='black', fontsize=20, va='center', ha='center')
        else:
            ax.text(0.5, 0.5, text+" "+unit, color='white', fontsize=20, va='center', ha='center')
    
    """rect = plt.Rectangle((0, 0), 2.75, 1, edgecolor=box_color, fill=False, linewidth=5, facecolor="none")"""
    rect = plt.Rectangle((0, 0), 2.75, 1, color=box_color)
    
    ax.add_patch(rect)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    IP(usename,plt)