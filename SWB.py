from Function import make_SWB
from DB import all_list_plus

f = open("./어인정/냥코대전쟁.txt", "r", encoding="UTF8")
lines = [line.strip("\n") for line in f.readlines()]
f.close()

make_SWB(all_list_plus)