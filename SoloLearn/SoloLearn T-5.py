import numpy as np

players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
list1 = []
mean = np.mean(players)
std = np.std(players)

for i in players:
    if (mean - std) <= i <= (mean + std):
        list1.append(i)

print(len(list1))
