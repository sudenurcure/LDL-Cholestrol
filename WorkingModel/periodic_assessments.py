import numpy as np
import matplotlib.pyplot as plt
from save_plot import insert_plot as IP

def periodic(df):
    ex = df["LDPN [nmol/L]"] #current result

    low = 1000
    moderate = 1299
    bhigh = 1599
    high = 2000

    constant = 2 * (abs(high - low)) / 7

    axlow = low - constant
    axhigh = high + constant

    x = np.linspace(axlow, axhigh, 1000)
    y = np.ones(1000)

    fig, ax = plt.subplots(figsize=(10, 0.5))

    ax.set_xlim(axlow, axhigh)
    ax.set_ylim(0,1)
    # Define colors for each range
    colors = {'#008000': (axlow, low),
            '#22B20F': (low, moderate),
            '#F9AB06': (moderate, bhigh),
            '#EA0A0A': (bhigh, high),
            '#B80000': (high, axhigh)}

    # Create rectangles with specified colors
    for color, (start, end) in colors.items():
        rect = plt.Rectangle((start, 0), end - start, 1, facecolor=color, alpha=1)
        ax.add_patch(rect)

    ax.plot(x, y, color='white')

    ax.get_yaxis().set_visible(False)
    ax.get_xaxis().set_visible(False)

    prev = axlow
    for title, limit in [["Low",low], ["Moderate",moderate], ["Borderline High",bhigh], ["High",high]]:
        ax.axvline(x=limit, color='white', linestyle='-', linewidth=1.5)
        if limit == low:
            ax.text((prev + limit) / 2, +0.45, "< " + str(limit), ha='center', va='center', fontsize=14, color = "white")
            ax.text((prev + limit) / 2, -0.4, title, ha='center', va='center', fontsize=12, color = "black")
        elif limit == high:
            ax.text((prev + limit) / 2, +0.45, str(prev + 1) + " - " + str(limit), ha='center', va='center', fontsize=14, color = "white")
            ax.text((prev + limit) / 2, -0.4, title, ha='center', va='center', fontsize=12, color = "black")
            ax.text((limit + axhigh) / 2, +0.45, "> " + str(limit), ha='center', va='center', fontsize=14, color = "white")
            ax.text((limit + axhigh) / 2, -0.4, "Very High", ha='center', va='center', fontsize=12, color = "black")
        else:
            if prev == low:
                ax.text((prev + limit) / 2, +0.45, str(prev) + " - " + str(limit), ha='center', va='center', fontsize=14, color = "white")
                ax.text((prev + limit) / 2, -0.4, title, ha='center', va='center', fontsize=12, color = "black")
            else:
                ax.text((prev + limit) / 2, +0.45, str(prev + 1) + " - " + str(limit), ha='center', va='center', fontsize=14, color = "white")
                ax.text((prev + limit) / 2, -0.4, title, ha='center', va='center', fontsize=12, color = "black")
        prev = limit

    # Patient results at different dates
    dates = ["22.10.2023", "24.7.2020", "09.07.2023"]
    results = [ex, 3000, 800]

    count = 0
    for date, result in zip(dates, results):
        custom_value = max(axlow, min(result, axhigh))
        linewidth = 2 if axlow < result < axhigh else 5

        ax.annotate(str(result) + " nmol/L" + "\n" + date, xy=(custom_value, 1), xytext=(custom_value, 1.7 + count),
                    ha='center', va='center', fontsize=10,
                    arrowprops=dict(facecolor='black', arrowstyle="->",linewidth=1.4))
        count += 0.7

    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white') 
    ax.spines['right'].set_color('white')
    ax.spines['left'].set_color('white')

    IP("timelyldlpn",plt)