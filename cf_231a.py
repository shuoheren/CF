t = int(input())
ans = 0
for _ in range(t):
    temp = (input())
    a = int(temp[0])
    b = int(temp[2])
    c = int(temp[4])
    ans += (a+b+c) >= 2
print(ans)
