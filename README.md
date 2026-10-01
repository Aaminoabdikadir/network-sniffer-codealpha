# Basic Network Sniffer - CodeAlpha Internship

A functional network packet sniffer written in Python utilizing raw sockets (`socket.SOCK_RAW`). The tool captures live network traffic, resolves IP addresses to hostnames (Reverse DNS), logs data to CSV files, and provides protocol distribution analysis via Matplotlib.

## Features
- **Raw Socket Capture**: Captures IPv4 TCP, UDP, and ICMP packets.
- **Domain Resolution**: Resolves IP addresses into domain names automatically (`socket.gethostbyaddr`).
- **Data Logging**: Generates timestamped CSV log files for captured packets.
- **Data Visualization**: Includes a secondary script (`chart.py`) to render protocol distribution pie charts using `pandas` and `matplotlib`.

## Requirements
- Python 3.x
- Administrative privileges (Windows PowerShell / Command Prompt)
- Required Python Libraries:
  ```bash
  pip install pandas matplotlib