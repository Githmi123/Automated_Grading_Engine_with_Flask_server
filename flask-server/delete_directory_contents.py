import shutil
import os

def delete_directory_contents(folder_path):
    if not os.path.exists(folder_path):
        print(f"The folder {folder_path} does not exist")
        return
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            os.remove(file_path)

    print(f"Contents of folder {folder_path} have been deleted.")

