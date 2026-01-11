import os
from pathlib import Path
import shutil



CATEGORIES = {
    
    "IMAGES":{ 
        "ext": [".png", ".gif", ".bmp", ".jpeg", ".jpg", ".aseprite", ".heic" ],
        "destination": Path("~/Downloads/dl-images").expanduser(),
              
     },

     "VIDEO": {
         "ext": [".mp4", ".avi", ".mov", ".mkv",],
         "destination": Path("~/Downloads/dl-video").expanduser() 
     },

     "DOCUMENTS": {
         "ext": [".pdf", ".docx", ".txt", ".xlsx", ".rtf", ".md"],
         "destination": Path("~/Downloads/dl-docs").expanduser()
     },

     "COMPRESSED": {
         "ext": [".zip", ".rar", ".tar", ".gz",],
         "destination": Path("~/Downloads/dl-compressed").expanduser()
     },
    
     "PROGRAMS":{
         "ext": [".exe", ".msi", ".bat", ".sh", ".dmg", ".app"],
         "destination": Path("~/Downloads/dl-programs").expanduser()
     }

 }


pathsource = Path("~/Downloads").expanduser()

def sort():
    for file in pathsource.iterdir():
          if file.is_file():
               for category in CATEGORIES:
                    if file.suffix in CATEGORIES[category]["ext"]:
                         shutil.move(file, CATEGORIES[category]["destination"])
                         break
                         


if __name__ == "__main__":
    sort()