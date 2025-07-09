from DB import eo_sub

for i in eo_sub:
    with open(f"./어인정/{i}.txt", "r", encoding="UTF8") as f:
        words = [i.strip("\n") for i in f.readlines()]

    words = sorted(set(words))

    with open(f"./어인정/{i}.txt", "w", encoding="UTF8") as f:
        for k in words:
            f.write(k + "\n")