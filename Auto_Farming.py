import os
import glob
import re
from DB import all_sub, no_sub

files = glob.glob("./파밍/*.kkt")
for name in files:
    src = os.path.splitext(name)
    os.rename(name, src[0] + '.txt')

farming = os.listdir("./파밍/")

new_word = []
for i in farming:
    f = open(f"./파밍/{i}", "r", encoding="UTF8")
    line = f.readline()
    f.close()
    new_word.extend(re.findall(r'wer":"(.*?)"', line))

subject = input("파밍한 주제 >> ")
while subject not in all_sub:
    subject = input("다시 입력 >> ")

if subject in no_sub:
    where = "노인정"
else:
    where = "어인정"

f = open(f"./{where}/{subject}.txt", "r", encoding="UTF8")
word = [i.strip("\n") for i in f.readlines()]
f.close()

temp = len(word)
log = [i for i in new_word if i not in word]

word += new_word
word = sorted(set(word))

f = open(f"./{where}/{subject}.txt", "w", encoding="UTF8")
for i in word:
    f.write(i + "\n")
f.close()

for i in os.scandir("./파밍/"):
    os.remove(i.path)

f = open("./log.txt", "w", encoding="UTF8")
f.write(f"<{subject}>\n")
for i in log:
    f.write(i + "\n")
f.close()

print(f"\n추가된 단어 : {len(word) - temp}개")