from save_plot import insert_plot as IP
import matplotlib.pyplot as plt

def create_colored_box_image(usename, value, sick, unit = None):
    if sick == True:
        box_color = 'orangered'
    elif sick == False:
        box_color = 'lawngreen'
    elif sick == "noref":
        box_color = 'white'
    else:
        box_color = 'orange'

    usename = usename + "_box"

    fig, ax = plt.subplots(figsize=(2.85, 0.65))

    text = str(value)
    try:
        unit = unit.replace("[","").replace("]","")
    except:
        ax.text(0.5, 0.5, text, color='black', fontsize=20, va='center', ha='center')
    else:
        ax.text(0.5, 0.5, text+" "+unit, color='black', fontsize=20, va='center', ha='center')
    
    rect = plt.Rectangle((0, 0), 2.75, 1, color=box_color)
    ax.add_patch(rect)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    IP(usename,plt)