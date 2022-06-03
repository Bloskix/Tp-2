file = open("archivo.txt","w")
file.write("pablo\n")
file.close()
file = open("archivo.txt","a")
file.write("maxi\n""jose")
file.close()
file = open("archivo.txt","r")
list = file.readlines()
print(list)
new_list = []
for i in list:
    i = i.strip("\n")
    new_list.append(i)
print(new_list)

