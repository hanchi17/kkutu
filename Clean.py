from DB import eo_sub

for i in eo_sub:
    if i == "하스스톤":
        continue
    
    f = open(f"./어인정/{i}.txt", "r", encoding="UTF8")
    words = f.readlines()
    f.close()

    words = sorted(set(words))

    f = open(f"./어인정/{i}.txt", "w", encoding="UTF8")
    for k in words:
        f.write(k)
    f.close()