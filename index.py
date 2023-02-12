import os
import time

#"C:\\Users\НАША\Desktop\kito"
spisok = []

for adress, dirs, files in os.walk("C:\\Users\НАША\Desktop"):
    for dir in dirs:
        full = os.path.join(adress, dir)
        if time.time() - os.path.getctime(full) < 86400:
            spisok.append(full)

print(spisok)

