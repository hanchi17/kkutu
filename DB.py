import os
import json

no_sub = os.listdir("./노인정/")
eo_sub = os.listdir("./어인정/")

no_len = 54
eo_len = len(eo_sub)

for i in range(no_len):
    no_sub[i] = no_sub[i].strip(".txt")
for i in range(eo_len):
    eo_sub[i] = eo_sub[i].strip(".txt")

no_list = []
for i in range(no_len):
    with open(f"./노인정/{no_sub[i]}.txt", "r", encoding="UTF8") as f1:
        lines = [line.strip("\n") for line in f1.readlines()]
    no_list.append(lines)

with open("No_Need.json", "r", encoding="UTF8") as f3:
    data = set(json.load(f3))
no_list_plus = [[k for k in i if k not in data] for i in no_list]

eo_list = []
for i in range(eo_len):
    with open(f"./어인정/{eo_sub[i]}.txt", "r", encoding="UTF8") as f2:
        lines = [line.strip("\n") for line in f2.readlines()]
    eo_list.append(lines)

all_sub = no_sub + eo_sub
all_list = no_list + eo_list
all_list_plus = no_list_plus + eo_list