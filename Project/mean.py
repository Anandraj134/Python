import statistics

import numpy as np

x = [11, 29, 41, 46, 46, 46, 46, 47, 49, 54, 59, 59]
print(np.mean(x))
print(np.median(x))
print(np.std(x))
print(np.var(x))
print(statistics.mode(x))
print(max(x) - min(x))