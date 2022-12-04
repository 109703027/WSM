import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

recall = [0.00,0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90,1.00]

path = "./result_stemming/Okapi_analysis.txt"
precision = []

count = 1
with open(path) as f:
    for line in f.readlines():
        if count >= 8 and count <= 18:
            num = float(line[18:24])
            precision.append(num)
        if count == 18:
            break
        count += 1

plt.plot(recall, precision,'o-',color = 'b',label = "Okapi")
##########################################
path = "./result_stemming/JM_analysis.txt"
precision1 = []

count = 1
with open(path) as f:
    for line in f.readlines():
        if count >= 8 and count <= 18:
            num = float(line[18:24])
            precision1.append(num)
        if count == 18:
            break
        count += 1

plt.plot(recall, precision1,'o-',color = 'r',label = "JM")

##########################################
path = "./result_stemming/Dirichlet_analysis.txt"
precision2 = []

count = 1
with open(path) as f:
    for line in f.readlines():
        if count >= 8 and count <= 18:
            num = float(line[18:24])
            precision2.append(num)
        if count == 18:
            break
        count += 1

plt.plot(recall, precision2,'o-',color = 'g',label = "Dirichlet")

##########################################
path = "./result_stemming/new_Okapi_analysis.txt"
precision3 = []

count = 1
with open(path) as f:
    for line in f.readlines():
        if count >= 8 and count <= 18:
            num = float(line[18:24])
            precision3.append(num)
        if count == 18:
            break
        count += 1

plt.plot(recall, precision3,'o-',color = 'y',label = "new query to Okapi")

plt.title('index with stemming', fontsize=20)
#plt.figure(figsize=(15,10),dpi=100,linewidth = 2)
plt.ylim(0.0,0.8)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel("recall", fontsize=30, labelpad = 15)
plt.ylabel("precision", fontsize=30, labelpad = 20)
plt.legend(loc = "best",fontsize=15)

plt.show()
