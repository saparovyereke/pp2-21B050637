import os
x = "C:\git\pp2-21B050637\sis6"
if os.access(x, os.F_OK):
    print("direcroty:", os.path.dirname(x))
    print("name:", os.path.basename(x))
else:
    print("This path does not exist")
