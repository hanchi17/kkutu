from itertools import groupby, chain

def find_front(where, how):
    word = input("\n시작 단어 >> ")
    
    temp = {k for i in where for k in i if k.startswith(word)}

    result = sorted(temp)
    if how == "2":
        result = sorted(result, key=len, reverse=True)

    f = open("result.txt", "w", encoding="UTF8")
    for i in range(len(result)):
        f.write(result[i] + "\n")
    f.close()


def find_back(where, how):
    word = input("\n끝 단어 >> ")
    
    temp = {k for i in where for k in i if k.endswith(word)}

    result = sorted(temp)
    if how == "2":
        result = sorted(result, key=len, reverse=True)

    f = open("result.txt", "w", encoding="UTF8")
    for i in range(len(result)):
        f.write(result[i] + "\n")
    f.close()


def find_inclusion(where, how):
    word = input("\n포함 단어 >> ")
    
    temp = {k for i in where for k in i if word in k}

    result = sorted(temp)
    if how == "2":
        result = sorted(result, key=len, reverse=True)

    f = open("result.txt", "w", encoding="UTF8")
    for i in range(len(result)):
        f.write(result[i] + "\n")
    f.close()


def find_all(where, how):
    temp = {k for i in where for k in i}

    result = sorted(temp)
    if how == "2":
        result = sorted(result, key=len, reverse=True)

    f = open("result.txt", "w", encoding="UTF8")
    for i in range(len(result)):
        f.write(result[i] + "\n")
    f.close()


def find_long(where):
    temp = {k for i in where for k in i}
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
    word = input("\n시작 단어 >> ")

    temp = {k for i in where for k in i if k.startswith(word)}
    temp = sorted(temp, key=lambda x: (x[0], -len(x)))

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
        temp = sorted(temp, key=lambda x: (x[0], -len(x)))
    else:
        temp = sorted(where, key=lambda x: (x[0], -len(x)))

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