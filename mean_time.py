from math import sqrt
import sys
if len(sys.argv)>1:
    file = sys.argv[1]
else:
    file = "../logs/logarr.txt"

if len(sys.argv)>1:
    count = int(sys.argv[1])
else:
    count =10 

raw_logs = []
logs_count = count
for i in range(logs_count):
    raw_logs.append([])
    with open(file[:-4]+str(i)+file[-4:]) as f:
        lines = f.readlines()
    for j in range(len(lines)):
        raw_logs[i].append(float(lines[j]))

mean_logs = []
droped_count = 0
for i in range(len(raw_logs[0])):
    cur_logs =[]
    mean = 0
    mean2 = 0
    for j in range(logs_count):
        mean += raw_logs[j][i]/count
        mean2 += raw_logs[j][i]*raw_logs[j][i]/count
    disp =  mean2 - mean*mean
    sigma = sqrt(disp)
    new_mean=0
    for j in range(logs_count):
        if raw_logs[j][i] < sigma*2.9+mean and mean - 2.9*sigma < raw_logs[j][i] :
            cur_logs.append(raw_logs[j][i])
    droped_count += logs_count - len(cur_logs)
    for j in range(len(cur_logs)):
        new_mean += cur_logs[j]/len(cur_logs)
    mean_logs.append(new_mean)

with open(file, "w") as f:
    for i in mean_logs:
        f.write(str(i)+"\n")

print(droped_count)
