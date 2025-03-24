from DB import all_sub, all_list
from Function import find_front, find_back, find_inclusion, find_all, find_long, find_mission


subject = input("<주제 범위>\n| 1. 전체 | 2. 노인정만 | 3. 어인정만 | 4. 특정 주제 |\n >> ")
while subject not in ["1", "2", "3", "4"]:
    subject = input("다시 입력 >> ")
if subject == "4":
    detail = input("<주제 입력>\n >> ")
    while detail not in all_sub:
        detail = input("다시 입력 >> ")

if subject == "1":
    where = all_list
elif subject == "2":
    where = all_list[:54]
elif subject == "3":
    where = all_list[54:]
else:
    where = [all_list[all_sub.index(detail)]]


what = input("\n<목적>\n| 1. ~로 시작하는 단어 | 2. ~로 끝나는 단어 | 3. ~를 포함하는 단어 |\
            \n| 4. 전체              | 5. 장문            | 6. 미션              |\n >> ")
while what not in ["1", "2", "3", "4", "5", "6"]:
    what = input("다시 입력 >> ")

if what in ["1", "2", "3", "4"]:
    how = input("\n<배열 방식>\n| 1. 사전순 | 2. 길이순 |\n >> ")
    while how not in ["1", "2"]:
        how = input("다시 입력 >> ")


if what == "1":
    find_front(where, how)
elif what == "2":
    find_back(where, how)
elif what == "3":
    find_inclusion(where, how)
elif what == "4":
    find_all(where, how)
elif what == "5":
    find_long(where)
else:
    find_mission(where)