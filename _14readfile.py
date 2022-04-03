file = open("pythonimportions.txt",'r')

print(file.readable())

f = []
for item in file.readlines():
    f.append(item)

print(f)