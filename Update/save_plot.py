import os
import matplotlib.pyplot as plt

ALL_FILES_FOLDER = "all_files"

def create_all_files_folder():
    os.makedirs(ALL_FILES_FOLDER, exist_ok=True)

def create_date_folder(folder_name):
    create_all_files_folder()
    folder_path = os.path.join(ALL_FILES_FOLDER, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    return folder_path

def insert_plot(plot_file, fig, group_name=None):
    create_all_files_folder()
    
    if group_name is not None:
        folder_path = create_date_folder(group_name)
    else:
        folder_path = ALL_FILES_FOLDER

    file_path = os.path.join(folder_path, plot_file)
    fig.savefig(file_path, bbox_inches='tight', dpi=300)
    plt.close()