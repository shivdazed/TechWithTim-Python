file = open("pythonimportions.txt",'w')

file.write("cool\n")
file.close()
f = []
fil = open("pythonimportions.txt",'r')
for item in fil.readlines():
    f.append(item)

print(f)
