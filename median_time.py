from math import sqrt

raw_logs = []
logs_count = 5
for i in range(logs_count):
    raw_logs.append([])
    with open(f"../logs/517log{i+1}.txt") as f:
        lines = f.readlines()
    for j in range(len(lines)):
        raw_logs[i].append(float(lines[j]))

median_logs = []
droped_count = 0
for i in range(len(raw_logs[0])):
    cur_logs =[]
    for j in range(logs_count):
        cur_logs.append(raw_logs[j][i])
    cur_logs.sort()
    median_logs.append(cur_logs[len(cur_logs)//2])

with open("../logs/517log.txt", "w") as f:
    for i in median_logs:
        f.write(str(i)+"\n")
