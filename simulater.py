import matplotlib.pyplot as plt
import numpy as np

def calculate_performance_metrics(seek_time, num_requests):
    avg_seek_time = seek_time / num_requests if num_requests else 0
    system_throughput = num_requests / (seek_time + 1)  # Adding 1 to avoid division by zero
    return avg_seek_time, system_throughput

def visualize(sequence, algorithm, seek_time, avg_seek_time, system_throughput):
    plt.figure(figsize=(8, 5))
    plt.plot(sequence, range(len(sequence)), marker="o", linestyle="-", color="b", label="Disk Head Movement")
    plt.xlabel("Cylinder Number")
    plt.ylabel("Request Order")
    plt.title(f"Disk Scheduling Algorithm: {algorithm}\nTotal Seek Time: {seek_time}\nAvg Seek Time: {avg_seek_time:.2f}, Throughput: {system_throughput:.2f}")
    plt.legend()
    plt.gca().invert_yaxis()
    plt.grid()
    plt.show()

def main():
    print("\U0001F4C0 Advanced Disk Scheduling Simulator \U0001F4C0")
    
    requests = list(map(int, input("Enter disk access requests (comma-separated): ").split(",")))
    head = int(input("Enter initial disk head position: "))
    print("Choose a scheduling algorithm:")
    print("1. FCFS\n2. SSTF\n3. SCAN\n4. C-SCAN")
    choice = int(input("Enter the number of your choice: "))

    if choice == 1:
        algorithm = "FCFS"
        sequence, seek_time = fcfs(requests, head)
    elif choice == 2:
        algorithm = "SSTF"
        sequence, seek_time = sstf(requests, head)
    elif choice == 3:
        direction = input("Enter direction (left/right): ").lower()
        algorithm = "SCAN"
        sequence, seek_time = scan(requests, head, direction=direction)
    elif choice == 4:
        algorithm = "C-SCAN"
        sequence, seek_time = cscan(requests, head)
    else:
        print("❌ Invalid choice. Exiting...")
        return

    avg_seek_time, system_throughput = calculate_performance_metrics(seek_time, len(requests))

    print(f"\n🔹 Selected Algorithm: {algorithm}")
    print(f"🔹 Seek Time: {seek_time}")
    print(f"🔹 Average Seek Time: {avg_seek_time:.2f}")
    print(f"🔹 System Throughput: {system_throughput:.2f} requests/unit time")
    print(f"🔹 Disk Head Movement Sequence: {sequence}\n")

    visualize(sequence, algorithm, seek_time, avg_seek_time, system_throughput)

if __name__ == "_main_":
    main()
