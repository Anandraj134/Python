import numpy as np
n, p = [int(x) for x in input().split()]

list1 = []

for i in range(n):
    temp = input()
    list1.append(temp.split())

array1 = np.array(list1, dtype=np.float64).reshape(n, p)

temp = np.mean(array1, axis=1).round(2)
print(temp)