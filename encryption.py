import random

text = input()
inp_chr = []
rep_chr = []
rep = []
for i in range(32,128):
    inp_chr.append(chr(i))
    rep.append(i)
for i in inp_chr:
    temp = random.choice(rep)
    rep.remove(temp)
    rep_chr.append(chr(temp))
cipher = ""
for i in text:
    cipher += rep_chr[ord(i) - 32]

print(cipher)