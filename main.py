def round_robin_scheduling(processes, quantum):

    n = len(processes)
    
 
    process_data = []
    for pid, arrival, burst in processes:
        process_data.append({
            'pid': pid,
            'arrival': arrival,
            'burst': burst,
            'remaining': burst,
            'waiting': 0,
            'turnaround': 0,
            'completion': 0
        })
    

    process_data.sort(key=lambda x: x['arrival'])
    
    ready_queue = []
    current_time = 0
    completed = 0
    gantt_chart = []
    
    print("=" * 80)
    print("ROUND ROBIN SCHEDULING (Time Quantum = {})".format(quantum))
    print("=" * 80)
    

    added_to_queue = [False] * n
    current_process_index = 0
    
    while completed < n:

        for i in range(n):
            if (not added_to_queue[i] and 
                process_data[i]['arrival'] <= current_time and 
                process_data[i]['remaining'] > 0):
                ready_queue.append(i)
                added_to_queue[i] = True
        
        if not ready_queue:
          
            next_arrival = min([p['arrival'] for p in process_data 
                              if p['remaining'] > 0])
            current_time = next_arrival
            continue
        
   
        idx = ready_queue.pop(0)
        process = process_data[idx]
        

        execution_time = min(quantum, process['remaining'])
        
        gantt_chart.append({
            'pid': process['pid'],
            'start': current_time,
            'end': current_time + execution_time
        })
        
        current_time += execution_time
        process['remaining'] -= execution_time
        
      
        for i in range(n):
            if (not added_to_queue[i] and 
                process_data[i]['arrival'] <= current_time and 
                process_data[i]['remaining'] > 0):
                ready_queue.append(i)
                added_to_queue[i] = True
        
      
        if process['remaining'] > 0:
            ready_queue.append(idx)
        else:
          
            process['completion'] = current_time
            process['turnaround'] = process['completion'] - process['arrival']
            process['waiting'] = process['turnaround'] - process['burst']
            completed += 1
    
  
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
    print("{:<10} {:<15} {:<15} {:<15} {:<15}".format(
        "Process", "Arrival Time", "Burst Time", "Waiting Time", "Turnaround Time"))
    print("-" * 80)
    
    total_waiting = 0
    total_turnaround = 0
    
    for process in process_data:
        print("{:<10} {:<15} {:<15} {:<15} {:<15}".format(
            process['pid'],
            process['arrival'],
            process['burst'],
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
        ('P1', 0, 5),
        ('P2', 1, 3),
        ('P3', 2, 1),
        ('P4', 3, 2),
        ('P5', 4, 3)
    ]
   
    quantum = 2
    

    results = round_robin_scheduling(processes, quantum)
