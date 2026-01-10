from pathlib import Path



CATEGORIES = {
    "IMAGES": [".png", ".gif", ".bmp", ".jpeg",],
    "VIDEO": [".mp4", ".avi", ".mov", ".mkv",],
    "DOCUMENTS": [".pdf", ".docx", ".txt", ".xlsx",],
    "AUDIO": [".mp3", ".wav", ".aac", ".flac",],
    "COMPRESSED": [".zip", ".rar", ".tar", ".gz",],
    "PROGRAMS": [".exe", ".msi", ".bat", ".sh",],

 }

def checktype():
    for file in pathsource: