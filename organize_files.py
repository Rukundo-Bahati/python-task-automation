import os
import shutil
from pathlib import Path

# File type categories
FILE_TYPES = {
    "Images": [".jpeg", ".jpg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Others": []
}

# Function to organize files
def organize_files(src_dir):
    for item in os.listdir(src_dir):
        item_path = Path(src_dir) / item
        if item_path.is_file():
            file_extension = item_path.suffix.lower()
            moved = False

            # Categorize files and move
            for category, extensions in FILE_TYPES.items():
                if file_extension in extensions:
                    category_dir = Path(src_dir) / category
                    if not category_dir.exists():
                        category_dir.mkdir()
                    shutil.move(str(item_path), str(category_dir / item))
                    moved = True
                    break

            if not moved:
                other_dir = Path(src_dir) / "Others"
                if not other_dir.exists():
                    other_dir.mkdir()
                shutil.move(str(item_path), str(other_dir / item))
