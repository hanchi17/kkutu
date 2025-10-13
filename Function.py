from itertools import groupby, chain
import json

def find_front(where, how):
    word = input("\n시작 단어 >> ")
    
    if any(isinstance(i, list) for i in where):
        temp = {k for i in where for k in i if k.startswith(word)}
    else:
        temp = {i for i in where if i.startswith(word)}

    result = sorted(temp)
    if how == "2":
        result = sorted(result, key=len, reverse=True)

    f = open("result.txt", "w", encoding="UTF8")
    for i in range(len(result)):
        f.write(result[i] + "\n")
    f.close()


def find_back(where, how):
    word = input("\n끝 단어 >> ")

    if any(isinstance(i, list) for i in where):
        temp = {k for i in where for k in i if k.endswith(word)}
    else:
        temp = {i for i in where if i.endswith(word)}

    result = sorted(temp)
    if how == "2":
        result = sorted(result, key=len, reverse=True)

    f = open("result.txt", "w", encoding="UTF8")
    for i in range(len(result)):
        f.write(result[i] + "\n")
    f.close()


def find_inclusion(where, how):
    word = input("\n포함 단어 >> ")
    
    if any(isinstance(i, list) for i in where):
        temp = {k for i in where for k in i if word in k}
    else:
        temp = {i for i in where if word in i}

    result = sorted(temp)
    if how == "2":
        result = sorted(result, key=len, reverse=True)

    f = open("result.txt", "w", encoding="UTF8")
    for i in range(len(result)):
        f.write(result[i] + "\n")
    f.close()


def find_all(where, how):
    if any(isinstance(i, list) for i in where):
        temp = {k for i in where for k in i}
    else:
        temp = {i for i in where}

    result = sorted(temp)
    if how == "2":
        result = sorted(result, key=len, reverse=True)

    f = open("result.txt", "w", encoding="UTF8")
    for i in range(len(result)):
        f.write(result[i] + "\n")
    f.close()


def find_long(where):
    if any(isinstance(i, list) for i in where):
        temp = {k for i in where for k in i}
    else:
        temp = {i for i in where}
    temp = sorted(temp, key=lambda x: (x[0], -len(x)))

    result = []
    for key, group in groupby(temp, key=lambda x: x[0]):
        group = list(group)[:10]
        group[-1] += "\n"
        result.append(f"<{key}>")
        result.extend(group)
    result[-1] = result[-1][:-1]

    f = open("result.txt", "w", encoding="UTF8")
    for i in range(len(result)):
        f.write(result[i] + "\n")
    f.close()


def find_mission(where):
    if any(isinstance(i, list) for i in where):
        word = input("\n시작 단어 >> ")

        temp = {k for i in where for k in i if k.startswith(word)}
        temp = sorted(temp, key=lambda x: (x[0], -len(x)))
    else:
        word = ""
        temp = sorted(where, key=lambda x: (-len(x), x[0]))

    result = []
    for i in "가나다라마바사아자차카타파하":
        dic = {}
        for k in temp:
            cnt = k.count(i)
            if cnt:
                dic.setdefault(cnt, []).append(k)

        if dic:
            temp2 = sorted(dic.items(), key=lambda x: -x[0])
            temp2 = [v for _, value in temp2 for v in value]
            temp2[-1] += "\n"
            result.append(f"<{word}{i}>")
            result.extend(temp2)
    result[-1] = result[-1][:-1]

    f = open("result.txt", "w", encoding="UTF8")
    for i in range(len(result)):
        f.write(result[i] + "\n")
    f.close()


def make_SWB(where):
    if any(isinstance(i, list) for i in where):
        temp = {k for i in where for k in i}
        temp = sorted(temp, key=lambda x: (x[0], -len(x), x))
    else:
        temp = sorted(where, key=lambda x: (x[0], -len(x), x))

    result = []
    for key, group in groupby(temp, key=lambda x: x[0]):
        group = list(group)
        group_cp = group.copy()
        group = group[:10]

        if len(group) == 1:
            result.append(f"({key}) // {group[0]} // null&&")
        else:
            result.append(f"({key}) // {group[0]}")
            group.pop(0)
            group[-1] += " // &&"
            group = list(chain(*[["", i] for i in group]))
            result.extend(group)

        for i in "가나다라마바사아자차카타파하":
            dic = {}
            for k in group_cp:
                cnt = k.count(i)
                if cnt:
                    dic.setdefault(cnt, []).append(k)
                    
            if dic:
                group_cp2 = sorted(dic.items(), key=lambda x: -x[0])
                group_cp2 = [v for _, value in group_cp2 for v in value][:10]
                group_cp2[-1] += "\n"

                if len(group_cp2) == 1:
                    result.append(f"({key}{i}) // {group_cp2[0]} // null&&")
                else:
                    result.append(f"({key}{i}) // {group_cp2[0]}")
                    group_cp2.pop(0)
                    group_cp2[-1] += " // &&"
                    group_cp2 = list(chain(*[["", i] for i in group_cp2]))
                    result.extend(group_cp2)      

    f = open("result.txt", "w", encoding="UTF8")
    for i in range(len(result)):
        f.write(result[i] + "\n")
    f.close()


def extraction(word):
    with open("Alphabet.json", "r", encoding="UTF8") as f:
        data = json.load(f)
    
    temp = ord(word) - 44032
    return word, data["initial"][temp // 588], data["medial"][(temp % 588) // 28]


def duum(word, ini, med):
    if (ini == "ㄴ") and (med in {"ㅕ", "ㅛ", "ㅠ", "ㅣ"}):
        return chr(ord(word) + 5292)
    elif (ini == "ㄹ"):
        if med in {"ㅑ", "ㅕ", "ㅖ", "ㅛ", "ㅠ", "ㅣ"}:
            return chr(ord(word) + 3528)
        elif med in {"ㅏ", "ㅐ", "ㅗ", "ㅚ", "ㅜ", "ㅡ"}:
            return chr(ord(word) - 1764)
    else:
        return(word)


def kill_word(where):
    temp = {k for i in where for k in i if (len(k) != 1) and (k!="(경기도/동두천시 부터)")}

    first_word = {i[0] for i in temp}
    last_word = {i[-1] for i in temp}

    result = []
    for i in last_word:
        if i not in first_word:
            if duum(*extraction(i)) not in first_word:
                result.append(i)
    
    print(sorted(result))