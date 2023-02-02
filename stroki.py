# text = input("input your name: ")
# print(text)
# print(len(text))

# print("dddd МИр мир МИР МиР".lower().find("мир"))

# url = "http://ya.ru"

# print(url.startswith("https"))

# new_text = "O"+text[1::]

# print(new_text)

# text = "мама мыла раму c мылом"
# words = text.split()
# words_lens = [len(word) for word in words]
# print(words)
# print(words_lens)
# print(max(words_lens))

# ga = 3
# gb = 5

# def f():
#     global ga
#     ga = 200
#     print(f"F() ga = {ga} gb = {gb}")

# print(f"GLOBAL ga = {ga} gb = {gb}")
# f()
# print(f"GLOBAL ga = {ga} gb = {gb}")

fin = open("input.txt","r")
fout = open("output.txt","w")

# fin.readline()
# weights = list(map(int, fin.readline().split()))
# fout.write(f"{min(weights)} {max(weights)}")

# a, b = map(int, fin.readline().split())
# fout.write(f"{a}\n\n\n{b}\n\n{a+b}")

# numsAsString = fin.readline().split()
# nums = [int(num) for num in numsAsString]

# fin.close()
# fout.close()

import re

# number_tel = "32-45-67"
# result = re.match(r"[0-9]{2}-[0-9]{2}-[0-9]{2}",number_tel)

text = "Alex"
result = re.match(r"[А-ЯA-Z]+",text)

if result==None:
    print("номер неверный")
else:
    print("номер верный")

# text = "пришлите свой документ на мою почту abc123@mail.ru и продублируйте на почту сотрудника 234dfjkg32@ya.com 234dfjkg32@ff.org спасибо"

# emails = re.findall(r"\w+@\w+\.com|\w+@\w+\.ru",text)

# print(emails)



