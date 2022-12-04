"""
==============================
Plotting categorical variables
==============================

You can pass categorical values (i.e. strings) directly as x- or y-values to
many plotting functions:
"""


import matplotlib.pyplot as plt

data = {'apple': 10, 'orange': 15, 'lemon': 5, 'lime': 20}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
axs[0].bar(names, values)
axs[1].scatter(names, values)
axs[2].plot(names, values)
fig.suptitle('Categorical Plotting')

"""
###############################################################################
# This works on both axes:
import matplotlib.pyplot as plt

path = 'result_stemming/Okapi_analysis.txt'
precision = []
count = 1
with open(path) as f:
    for line in f.readlines():
        if count >= 8 and count <=18:
            precision.append(line[18:24])
        if count == 18:
            break
        count += 1
print(precision)

recall = ["0.00", "0.10", "0.20", "0.30", "0.40", "0.50","0.60", "0.70", "0.80", "0.90", "1.00"]

fig, ax = plt.subplots()
# ax.plot(activity, dog, label="dog")
ax.plot(recall, precision, label="score")
ax.legend()

plt.show()
"""
