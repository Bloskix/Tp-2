import os
import re
contenido = os.listdir(r"C:\Users\pablo\OneDrive\Escritorio\SecretKey")
print(contenido)
list = []
for i in contenido:
    string = re.sub(r"[0-9]+","",i)
    os.chdir(r"C:\Users\pablo\OneDrive\Escritorio\SecretKey")
    os.rename(i,string)
