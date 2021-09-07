import os

createDirs = [
    "myData",
    "myData/chromeProfile",
]

createFiles = [
    "myData/chromeProfie.exe is this.txt",
    "myData/emailTarget.txt"
]

for path in createDirs:
    if not os.path.exists(path):
        os.makedirs(path)

for path in createFiles:
    if not os.path.exists(path):
        with open(path, mode="w", encoding="utf-8")as f:
            f.write("")
            if path =="myData/emailTarget.txt":
                f.write("email,password")



