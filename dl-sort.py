#!/usr/bin/env python3
from filetypes import CATEGORIES, folders
import os
from pathlib import Path
import shutil
import sys

absolute_path = Path.cwd()


def sort():
    for file in absolute_path.iterdir():
          if file.is_file():
               for category in CATEGORIES:
                    if file.suffix in CATEGORIES[category]["ext"]:
                         shutil.move(file, absolute_path / CATEGORIES[category]["folder"])
                         break
                         

def folder_check_make():
    for folder in folders:
         folderpath = absolute_path / folder
         folderpath.mkdir(exist_ok=True)

if __name__ == "__main__":
    folder_check_make()
    sort() 