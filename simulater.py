import matplotlib.pyplot as plt
import numpy as np

# Function to calculate performance metrics
def calculate_performance_metrics(seek_time, num_requests):
    avg_seek_time = seek_time / num_requests if num_requests else 0
    system_throughput = num_requests / (seek_time + 1)  # Adding 1 to avoid division by zero
    return avg_seek_time, system_throughput

# Function for FCFS (First Come First Serve)
def fcfs(requests, head):
    sequence = [head] + requests
    seek_time = sum(abs(sequence[i] - sequence[i + 1]) for i in range(len(sequence) - 1))
    return sequence, seek_time

# Function for SSTF (Shortest Seek Time First)
def sstf(requests, head):
    sequence = [head]
    remaining_requests = requests.copy()
    seek_time = 0

    while remaining_requests:
        closest = min(remaining_requests, key=lambda x: abs(x - head))
        seek_time += abs(head - closest)
        head = closest
        sequence.append(head)
        remaining_requests.remove(head)

    return sequence, seek_time

# Function for SCAN (Elevator Algorithm)
def scan(requests, head, disk_size=200, direction="left"):
    sequence = []
    left = [r for r in requests if r < head] + ([0] if direction == "left" else [])
    right = [r for r in requests if r >= head] + ([disk_size] if direction == "right" else [])

    left.sort()
    right.sort()
    if direction == "left":
        sequence = [head] + left[::-1] + right
    else:
        sequence = [head] + right + left[::-1]

    seek_time = sum(abs(sequence[i] - sequence[i + 1]) for i in range(len(sequence) - 1))
    return sequence, seek_time

# Function for C-SCAN (Circular SCAN)
def cscan(requests, head, disk_size=200):
    sequence = []
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    left.sort()
    right.sort()

    sequence = [head] + right + [disk_size, 0] + left
    seek_time = sum(abs(sequence[i] - sequence[i + 1]) for i in range(len(sequence) - 1))
    return sequence, seek_time

# Function to visualize disk movement
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

# Main function to run the simulator
def main():
    print("Advanced Disk Scheduling Simulator")
    
    # User Inputs
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
        print("Invalid choice. Exiting...")
        return

    # Calculate performance metrics
    avg_seek_time, system_throughput = calculate_performance_metrics(seek_time, len(requests))

    # Show results
    print(f"\nSelected Algorithm: {algorithm}")
    print(f"Seek Time: {seek_time}")
    print(f"Average Seek Time: {avg_seek_time:.2f}")
    print(f"System Throughput: {system_throughput:.2f} requests/unit time")
    print(f"Disk Head Movement Sequence: {sequence}\n")

    # Visualize disk movement
    visualize(sequence, algorithm, seek_time, avg_seek_time, system_throughput)

if __name__ == "__main__":
    main()

    visualize(sequence, algorithm, seek_time, avg_seek_time, system_throughput)

if __name__ == "_main_":
    main()
