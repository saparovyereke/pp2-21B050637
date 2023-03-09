import os

print("exist:", os.access("tsis6", os.F_OK))
print("read:", os.access("tsis6", os.R_OK))
print("write:", os.access("tsis6", os.W_OK))
print("execute:", os.access("tsis6", os.X_OK))
