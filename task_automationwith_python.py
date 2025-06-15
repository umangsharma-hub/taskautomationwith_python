import os
import shutil

# Change this to the folder you want to organize
SOURCE_FOLDER = "C:/Users/YourName/Downloads"

# File type mappings
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Documents": [".pdf", ".docx", ".txt", ".xls", ".xlsx"],
    "Music": [".mp3", ".wav", ".aac"],
    "Python": [".py"],
    "Archives": [".zip", ".rar", ".7z"],
    "Executables": [".exe"],
}

def organize_files(folder):
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)

        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)[1].lower()

            moved = False
            for category, extensions in FILE_TYPES.items():
                if file_ext in extensions:
                    dest_folder = os.path.join(folder, category)
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest_folder, file))
                    moved = True
                    break

            if not moved:
                other_folder = os.path.join(folder, "Others")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, file))

    print("✅ Files organized successfully!")