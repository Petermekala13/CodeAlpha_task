import os
import shutil

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".csv"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Others": []  
}

def organize_directory(directory_path, file_name):
    """
    Organizes the specified file in the specified directory by file type.
    """
    file_path = os.path.join(directory_path, file_name)

    if not os.path.exists(directory_path):
        print("The specified directory does not exist.")
        return
    
    if not os.path.isfile(file_path):
        print("The specified file does not exist in the directory.")
        return

    for folder in file_types.keys():
        folder_path = os.path.join(directory_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    file_extension = os.path.splitext(file_name)[1].lower()

    moved = False
    for folder, extensions in file_types.items():
        if file_extension in extensions:
            folder_path = os.path.join(directory_path, folder)
            shutil.move(file_path, os.path.join(folder_path, file_name))
            moved = True
            print(f"Moved {file_name} to {folder} folder.")
            break

    if not moved:
        folder_path = os.path.join(directory_path, "Others")
        shutil.move(file_path, os.path.join(folder_path, file_name))
        print(f"Moved {file_name} to Others folder.")

directory = input("Please enter the directory path: ")
file_name = input("Please enter the file name (with extension) to organize: ")

organize_directory(directory, file_name)

