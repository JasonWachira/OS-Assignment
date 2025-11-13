def preemptive_priority_scheduling(processes):
    n = len(processes)
    
    process_data = []
    for pid, arrival, burst, priority in processes:
        process_data.append({
            'pid': pid,
            'arrival': arrival,
            'burst': burst,
            'priority': priority,
            'remaining': burst,
            'waiting': 0,
            'turnaround': 0,
            'completion': 0,
            'start_time': -1
        })
    
    current_time = 0
    completed = 0
    gantt_chart = []
    last_process = None
    
    print("=" * 80)
    print("PREEMPTIVE PRIORITY SCHEDULING (Higher Number = Higher Priority)")
    print("=" * 80)
    
    while completed < n:
        available_processes = []
        
        for i in range(n):
            if (process_data[i]['arrival'] <= current_time and 
                process_data[i]['remaining'] > 0):
                available_processes.append(i)
        
        if not available_processes:
            current_time += 1
            continue
        
        available_processes.sort(key=lambda x: (-process_data[x]['priority'], 
                                                 process_data[x]['arrival']))
        
        idx = available_processes[0]
        process = process_data[idx]
        
        if process['start_time'] == -1:
            process['start_time'] = current_time
        
        if last_process != process['pid']:
            gantt_chart.append({
                'pid': process['pid'],
                'start': current_time,
                'end': current_time + 1
            })
            last_process = process['pid']
        else:
            gantt_chart[-1]['end'] = current_time + 1
        
        process['remaining'] -= 1
        current_time += 1
        
        if process['remaining'] == 0:
            process['completion'] = current_time
            process['turnaround'] = process['completion'] - process['arrival']
            process['waiting'] = process['turnaround'] - process['burst']
            completed += 1
            last_process = None
    
    print("\nGantt Chart:")
    print("-" * 80)
    for entry in gantt_chart:
        print("| {} ".format(entry['pid']), end="")
    print("|")
    
    print("{}".format(gantt_chart[0]['start']), end="")
    for entry in gantt_chart:
        print("    {}".format(entry['end']), end="")
    print("\n" + "-" * 80)
    
    process_data.sort(key=lambda x: x['pid'])
    
    print("\nProcess Details:")
    print("-" * 80)
    print("{:<10} {:<15} {:<15} {:<12} {:<15} {:<15}".format(
        "Process", "Arrival Time", "Burst Time", "Priority", "Waiting Time", "Turnaround Time"))
    print("-" * 80)
    
    total_waiting = 0
    total_turnaround = 0
    
    for process in process_data:
        print("{:<10} {:<15} {:<15} {:<12} {:<15} {:<15}".format(
            process['pid'],
            process['arrival'],
            process['burst'],
            process['priority'],
            process['waiting'],
            process['turnaround']
        ))
        total_waiting += process['waiting']
        total_turnaround += process['turnaround']
    
    print("-" * 80)
    
    avg_waiting = total_waiting / n
    avg_turnaround = total_turnaround / n
    
    print("\nPerformance Metrics:")
    print("-" * 80)
    print("Average Waiting Time: {:.2f} units".format(avg_waiting))
    print("Average Turnaround Time: {:.2f} units".format(avg_turnaround))
    print("=" * 80)
    
    return {
        'processes': process_data,
        'avg_waiting_time': avg_waiting,
        'avg_turnaround_time': avg_turnaround,
        'gantt_chart': gantt_chart
    }


if __name__ == "__main__":
    processes = [
        ('P1', 0, 4, 2),
        ('P2', 1, 3, 3),
        ('P3', 2, 1, 4),
        ('P4', 3, 5, 5),
        ('P5', 4, 2, 5)
    ]
    
    results = preemptive_priority_scheduling(processes)