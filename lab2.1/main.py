from math import sqrt

N = 59046883376179
e = 4044583
C = '''32279109612093
17838629182964
4165776716262
13093284635895
20048651313008
54626454832531
12801053743903
54675332003643
4544911979279
31928373564570
798945495513
19569174668782'''

answer = "" 

n = int(sqrt(N)) + 1

i = 0
while True:
    i += 1
    t = n + i
    w = t ** 2 - N
    if int(w ** 0.5) != w ** 0.5:
        continue
    sqrt_w = w ** 0.5
    break

p = t + sqrt_w
q = t - sqrt_w
phi = (p - 1) * (q - 1)
d = pow(e, -1, int(phi))

i = 0
for num in C.split("\n"):
    i += 1
    m = pow(int(num), d, N)
    part = m.to_bytes(4, byteorder='big').decode('cp1251')
    answer += part
    
print(f"n = {n}")
print(f"p = {p}")
print(f"q = {q}")
print(f"phi(N) = {phi}")
print(f"d = {d}")
print(f"answer = {answer}")
