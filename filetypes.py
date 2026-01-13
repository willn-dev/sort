from pathlib import Path



CATEGORIES = {
    
    "IMAGES":{ 
        "ext": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg", ".webp",
                 ".tiff", ".tif", ".ico", ".heic", ".heif", ".raw", ".cr2",
                   ".nef", ".orf", ".sr2", ".psd", ".ai", ".eps", ".indd", ".xcf", ".aseprite"],
        "folder": "images"
              
     },

     "VIDEO": {
         "ext": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".m4v", ".mpg",
                  ".mpeg", ".3gp", ".3g2", ".ogv", ".m2ts", ".mts", ".vob", ".ts", ".f4v"],
         "folder": "video"
     },

     "DOCUMENTS": {
         "ext": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".tex", ".wpd", ".pages", 
                 ".md", ".markdown", ".csv", ".xls", ".xlsx", ".xlsm", ".ods", ".ppt", ".pptx",
                   ".pps", ".odp", ".key", ".epub", ".mobi", ".azw", ".djvu"],

         "folder": "docs"
     },

     "COMPRESSED": {
         "ext": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".tar.gz", ".tgz", ".tar.bz2",
                    ".tbz2", ".tar.xz", ".txz", ".zipx", ".iso", ".deb", ".rpm"],
         "folder": "compressed"
     },
    
     "PROGRAMS":{
         "ext": [".exe", ".msi", ".app", ".dmg", ".deb", ".rpm", ".apk",
                  ".ipa", ".jar", ".bat", ".sh", ".command", ".run", ".bin", ".pkg", ".appimage"],
         "folder": "programs"
     }

 }

folders = ["images", "video", "docs", "compressed", "programs"]