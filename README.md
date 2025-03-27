# Disk Scheduling Simulator

A Python-based disk scheduling simulator that implements FCFS, SSTF, SCAN, and C-SCAN algorithms. It calculates performance metrics such as seek time, average seek time, and system throughput and visualizes disk head movement.

## Features

- Supports FCFS, SSTF, SCAN, and C-SCAN algorithms
- Calculates seek time, average seek time, and system throughput
- Visualizes disk head movement using Matplotlib
- Interactive user input for dynamic simulation

## Installation

1. Clone the repository:
   git clone [https://github.com/yourusername/disk-scheduling-simulator.git](https://github.com/yourusername/disk-scheduling-simulator.git)
   cd disk-scheduling-simulator

2. Install dependencies:
   pip install matplotlib numpy

## Usage

Run the script:
python simulator.py

Follow the prompts to input disk access requests, initial head position, and select a scheduling algorithm.

## Example Input/Output

Enter disk access requests (comma-separated): 98,183,37,122,14,124,65,67
Enter initial disk head position: 53
Choose a scheduling algorithm:

1. FCFS
2. SSTF
3. SCAN
4. C-SCAN
   Enter the number of your choice: 1

Output:
Selected Algorithm: FCFS
Seek Time: 640
Average Seek Time: 80.00
System Throughput: 0.12 requests/unit time

A graph displaying the disk head movement is also generated.

