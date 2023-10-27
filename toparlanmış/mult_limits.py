import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import seaborn as sns

# Set the custom colormap
cmap_colors = [(0.0000001, 0.3, 0), (0.95, 0.95, 0), (5, 0, 0)]
cmap = mcolors.LinearSegmentedColormap.from_list("custom_color_map", cmap_colors, N=10000)

sns.set()

def b_chart(patient, lwst, opt, bgst, *extra_limits, document):
    fig, ax = plt.subplots(figsize=(5, 1))

    # Ensure there are at least three limits
    if len(extra_limits) < 1:
        raise ValueError("At least three limits (lowest, optimum, highest) must be provided.")
    
    # Calculate the width for each bar
    bar_widths = [opt - lwst, bgst - opt] + [extra_limits[i + 1] - extra_limits[i] for i in range(0, len(extra_limits), 2)]
    
    # Create a list of bars with their widths
    bars = [(lwst, bar_widths[0], 0.1), (opt, bar_widths[1], 0.1)] + [(extra_limits[i], bar_widths[i+2], 0.1) for i in range(0, len(extra_limits), 2)]
    
    ax.broken_barh(bars, (0, 1), facecolors="None")
    
    min_limit = min(lwst, *extra_limits)
    max_limit = max(bgst, *extra_limits)
    
    ax.set_xlim(min_limit, max_limit)
    
    ax.yaxis.set_ticklabels([])
    
    x_ticks = [lwst, opt, bgst] + list(extra_limits)
    x_labels = [f"{str(limit)}" for limit in x_ticks]
    
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_labels, rotation="vertical")
    
    ax.get_xticklabels()[0].set_horizontalalignment('right')
    ax.get_xticklabels()[-1].set_horizontalalignment('left')
    
    ax.imshow(np.arange(0, max_limit - min_limit + 1).reshape(1, -1), cmap=cmap, aspect='auto', extent=[0, max_limit - min_limit, 0, 1])
    
    ax.add_patch(plt.Rectangle((0, 0), max_limit - min_limit, 1, fill=False, edgecolor='black', linewidth=2))
    
    plt.grid(False)
    return fig