import numpy as np

data = [15,16,18,19,22,24,29,30,34]

print("Mean :- ", np.mean(data))
print("Median :- ", np.median(data))
print("25th Percentile :- ", np.percentile(data,25))
print("75th Percentile :- ", np.percentile(data,75))
print("SD :- ", np.std(data))
print("Variance :- ", np.var(data))
