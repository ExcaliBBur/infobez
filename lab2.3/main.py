N = 500984306287
e1 = 470149
e2 = 267797
C1 = '''274230487503
6821302647
172152295595
454539302130
462305524774
73589652382
274794725040
295185494003
159348742119
62021560582
311827395163
159638616315'''
C2 = '''176943898057
272954693703
141643708385
238296127866
270971764501
389314459147
476866404163
295344931481
288885538254
144738759088
52793710114
416204845784'''

answer = ""

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
    return gcd, x, y 

c1 = C1.split("\n")
c2 = C2.split("\n")

a, s, r = extended_gcd(e2, e1)
print(f"s = {s}, r = {r}")

for i in range(len(c1)):
    m = (pow(int(c1[i]), r, N) * pow(int(c2[i]), s, N)) % N
    part = m.to_bytes(4, byteorder='big').decode('cp1251')
    answer += part

print(f"answer = {answer}")