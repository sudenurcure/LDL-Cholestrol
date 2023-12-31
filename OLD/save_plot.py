import os
import matplotlib

def create_date_folder(group_name):
    folder_name = group_name
    folder_path = os.path.join("all_files", folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    return folder_path

def insert_plot(group_name, plot_file, fig):
    folder_path = create_date_folder(group_name)
    fig.savefig(os.path.join(folder_path, plot_file),bbox_inches='tight', dpi=300)
    matplotlib.pyplot.close()