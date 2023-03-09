import os

if os.path.exists("sis6/files/file_for_delete.txt"):
    os.remove("sis6/files/file_for_delete.txt")
else:
    print("file does not exist")
