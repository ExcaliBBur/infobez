N = 762930465497
e = 369197
C = '''272601390768
146191862405
56417639739
25010208392
569176485965
292815488501
152909580675
634319609453
578700740159
648142948177
39319966771
517127377434
490584971826'''

answer = ""

for num in C.split("\n"):
    y = pow(int(num), e, N)
    res = 0
    while y != int(num):
        res = y
        y = pow(y, e, N)
    part = res.to_bytes(4, byteorder='big').decode('cp1251')
    answer += part
    
print(f"answer = {answer}")