import os

print("exist:", os.access("sis6", os.F_OK))
print("read:", os.access("sis6", os.R_OK))
print("write:", os.access("sis6", os.W_OK))
print("execute:", os.access("sis6", os.X_OK))
