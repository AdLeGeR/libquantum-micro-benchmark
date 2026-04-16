from math import sqrt

raw_logs = []
logs_count = 10
for i in range(logs_count):
    raw_logs.append([])
    with open(f"../logs/logarr{i}.txt") as f:
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
        mean += raw_logs[j][i]/10
        mean2 += raw_logs[j][i]*raw_logs[j][i]/10
    disp =  mean2 - mean*mean
    sigma = sqrt(disp)
    new_mean=0
    for j in range(logs_count):
        if raw_logs[j][i] < sigma*3+mean and mean - 3*sigma < raw_logs[j][i] :
            cur_logs.append(raw_logs[j][i])
    droped_count += logs_count - len(cur_logs)
    for j in range(len(cur_logs)):
        new_mean += cur_logs[j]/len(cur_logs)
    mean_logs.append(new_mean)

with open("../logs/mean_logs.txt", "w") as f:
    for i in mean_logs:
        f.write(str(i)+"\n")

print(droped_count)
