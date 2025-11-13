# Shortest Remaining Time First (SRTF) Scheduling

processes = [
    {'id': 'P1', 'arrival': 3, 'burst': 1},
    {'id': 'P2', 'arrival': 1, 'burst': 4},
    {'id': 'P3', 'arrival': 4, 'burst': 2},
    {'id': 'P4', 'arrival': 0, 'burst': 6},
    {'id': 'P5', 'arrival': 2, 'burst': 3}
]

n = len(processes)
remaining_time = [p['burst'] for p in processes]
complete = 0
time = 0
minm = 999999999
short = 0
check = False
wt = [0]*n
tat = [0]*n
finish_time = [0]*n

while complete != n:
    for j in range(n):
        if (processes[j]['arrival'] <= time) and (remaining_time[j] > 0):
            if remaining_time[j] < minm:
                minm = remaining_time[j]
                short = j
                check = True
    if not check:
        time += 1
        continue

    # Reduce remaining time
    remaining_time[short] -= 1
    minm = remaining_time[short] if remaining_time[short] > 0 else 999999999

    # If a process finishes
    if remaining_time[short] == 0:
        complete += 1
        check = False
        finish_time[short] = time + 1
        tat[short] = finish_time[short] - processes[short]['arrival']
        wt[short] = tat[short] - processes[short]['burst']
        if wt[short] < 0:
            wt[short] = 0
    time += 1

print(f"{'Process':<6}{'Arrival':<8}{'Burst':<7}{'Completion':<11}{'Turnaround':<11}{'Waiting':<8}")
for i in range(n):
    print(f"{processes[i]['id']:<6}{processes[i]['arrival']:<8}{processes[i]['burst']:<7}"
          f"{finish_time[i]:<11}{tat[i]:<11}{wt[i]:<8}")

print(f"\nAverage Waiting Time: {sum(wt)/n:.2f}")
print(f"Average Turnaround Time: {sum(tat)/n:.2f}")
