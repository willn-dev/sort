import os
from pathlib import Path
import shutil


CATEGORIES = {
    "IMAGES": [".png", ".gif", ".bmp", ".jpeg",],
    "VIDEO": [".mp4", ".avi", ".mov", ".mkv",],
    "DOCUMENTS": [".pdf", ".docx", ".txt", ".xlsx",],
    "COMPRESSED": [".zip", ".rar", ".tar", ".gz",],
    "PROGRAMS": [".exe", ".msi", ".bat", ".sh", ".dmg"],

 }

img_pth = Path("~/Downloads/dl-images")
video_pth = Path("~/Downloads/dl-video")
documents_pth = Path("~/Downloads/dl-docs")
compressed_pth = Path("~/Downloads/dl-compressed")
programs_pth = Path("~/Downloads/dl-programs")

pathsource = Path("~/Downloads")


def sort():
    for file in pathsource:
        if file.suffix in CATEGORIES["IMAGES"]:
              shutil.move(pathsource, img_pth)
        elif file.suffix in CATEGORIES["VIDEO"]:
             shutil.move(pathsource, video_pth)
        elif file.suffix in CATEGORIES["DOCUMENTS"]:
             shutil.move(pathsource, documents_pth)
        elif file.suffix in CATEGORIES["COMPRESSED"]:
             shutil.move(pathsource, compressed_pth)
        elif file.suffix in CATEGORIES["PROGRAMS"]:
            shutil.move(pathsource, programs_pth)
        else:
             continue
                     
