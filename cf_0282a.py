n = int(input())
x = 0
for i in range(n):
    temp = input()
    if temp == "X++":
        x += 1
    elif temp == "X--":
        x -= 1
    elif temp == "++X":
        x += 1
    elif temp == "--X":
        x -= 1
print(x)
