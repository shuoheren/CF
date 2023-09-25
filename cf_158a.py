# 15:53-16:04
i1 = input()
i2 = input()
i1 = [int(x) for x in i1.split()]
i2 = [int(x) for x in i2.split()]
treshold = i2[i1[1]-1]
print(sum([1*(x >= treshold and x > 0) for x in i2]))
