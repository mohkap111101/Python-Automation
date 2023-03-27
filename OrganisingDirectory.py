import os
from pathlib import Path

Subdirectories = {
    "Documents": [".pdf", ".txt", ".rtf"],
    "Audio": [".m4a", ".mfb", ".mp3"],
    "Video": [".mov", ".avi", ".mp4"],
    "Images": [".jpg", ".png", ".jpeg"],
    "Programming": [".py", ".cpp", ".ino", ".m"],
    "Solidworks": [".slddrw", ".sldprt"],
    "Microsoft Office Docs": [".docx", ".odt", ".ods", ".xlsx", ".pptx"]
    }

def PickDirectory(ext):
    for category, extensions in Subdirectories.items():
        for extension in extensions:
            if extension == ext:
                return category
    return "Miscellaneous"


def OrganiseDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        fileExt = filePath.suffix.lower()
        directory = PickDirectory(fileExt)
        dirPath = Path(directory)
        if dirPath.is_dir() != True:
            dirPath.mkdir()
        filePath.rename(dirPath.joinpath(filePath))
        
    
OrganiseDirectory()
