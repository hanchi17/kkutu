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
    f = open(f"./노인정/{no_sub[i]}.txt", "r", encoding="UTF8")
    lines = [line.strip("\n") for line in f.readlines()]
    f.close()
    no_list.append(lines)

with open("No_Need.json", "r", encoding="UTF8") as f:
    data = set(json.load(f))
no_list_plus = [[k for k in i if k not in data] for i in no_list]

eo_list = []
for i in range(eo_len):
    f = open(f"./어인정/{eo_sub[i]}.txt", "r", encoding="UTF8")
    lines = [line.strip("\n") for line in f.readlines()]
    f.close()
    eo_list.append(lines)

all_sub = no_sub + eo_sub
all_list = no_list + eo_list
all_list_plus = no_list_plus + eo_list