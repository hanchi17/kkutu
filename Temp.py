import re

lst = []
f = open(f"./list.txt", "r", encoding="UTF8")
line = f.readline()
f.close()
lst.extend(re.findall(r'word">(.*?)<', line))

f = open("temp.txt", "w", encoding="UTF8")
for i in range(len(lst)):
    f.write(lst[i] + "\n")
f.close()