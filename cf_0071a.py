def getResult(input):
    if len(input) <= 10:
        print(input)
        return

    temp = input[0] + str(len(input)-2) + input[-1]
    print(temp)
    return


t = int(input())

for _ in range(t):
    s = input().strip()
    getResult(s)
