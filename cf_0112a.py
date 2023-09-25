s1 = input()
s2 = input()
t1 = 0
t2 = 0
printed = False
for (a, b) in zip(s1, s2):
    if 'a' <= a <= 'z':
        t1 = ord(a)-ord('a')
    else:
        t1 = ord(a)-ord('A')
    if 'a' <= b <= 'z':
        t2 = ord(b)-ord('a')
    else:
        t2 = ord(b)-ord('A')
    if t1 > t2:
        print(1)
        printed = True
        break
    if t1 < t2:
        print(-1)
        printed = True
        break
if not printed:
    print(0)
