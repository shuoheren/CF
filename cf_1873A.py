def getResult(input):
    answer = set()
    answer.add("abc")
    answer.add("acb")
    answer.add("bac")
    answer.add("cba")
    if input in answer:
        print("YES")
    else:
        print("NO")
    return


t = int(input())

for _ in range(t):
    s = input().strip().lower()
    getResult(s)
