from DB import no_sub

for i in no_sub:
    if i == "하스스톤":
        continue
    
    f = open(f"./노인정/{i}.txt", "r", encoding="UTF8")
    words = [i.strip("\n") for i in f.readlines()]
    f.close()

    words = sorted(set(words))

    f = open(f"./노인정/{i}.txt", "w", encoding="UTF8")
    for k in words:
        f.write(k + "\n")
    f.close()