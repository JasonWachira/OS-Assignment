# FCFS Scheduling Algorithm

processes = [
    {'id': 'P1', 'arrival': 0, 'burst': 8},
    {'id': 'P2', 'arrival': 1, 'burst': 4},
    {'id': 'P3', 'arrival': 2, 'burst': 9},
    {'id': 'P4', 'arrival': 3, 'burst': 5}
]

# Sort by arrival time
processes.sort(key=lambda x: x['arrival'])

current_time = 0
total_wt = 0
total_tat = 0

print(f"{'Process':<10}{'Arrival':<8}{'Burst':<7}{'Start':<7}{'Completion':<11}{'Waiting':<9}{'Turnaround':<11}")
for p in processes:
    if current_time < p['arrival']:
        current_time = p['arrival']

    start_time = current_time
    completion_time = start_time + p['burst']
    waiting_time = start_time - p['arrival']
    turnaround_time = completion_time - p['arrival']

    p['start'] = start_time
    p['completion'] = completion_time
    p['waiting'] = waiting_time
    p['turnaround'] = turnaround_time

    total_wt += waiting_time
    total_tat += turnaround_time
    current_time = completion_time

    print(
        f"{p['id']:<10}{p['arrival']:<8}{p['burst']:<7}{p['start']:<7}{p['completion']:<11}{p['waiting']:<9}{p['turnaround']:<11}")

n = len(processes)
print(f"\nAverage Waiting Time: {total_wt / n:.2f} ms")
print(f"Average Turnaround Time: {total_tat / n:.2f} ms")
