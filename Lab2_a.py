import random
import matplotlib.pyplot as plt

n = 1000000
values = [random.uniform(0, 1) for _ in range(n)]

sn_values = []
sn_sum = 0

# Calculating partial sums (sn)
for i in range(n):  # (0, n-1)
    sn_sum += values[i]
    sn = sn_sum / (i + 1)
    sn_values.append(sn)

# Plotting the n to sn function
plt.plot(range(1, n+1), sn_values)
plt.xlabel('n')
plt.ylabel('sn')
plt.title('n to sn Function')
plt.grid(True)
plt.savefig('lab2a.png')
plt.show()
