import os
import platform
import psutil
from datetime import datetime

# Function to check if server is reachable
def ping_server(server):
    response = os.system(f"ping -c 1 {server} > /dev/null 2>&1")
    return response == 0

# Function to check local server health
def check_local_health():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    return cpu, memory, disk

# Main function
def main():
    with open("servers.txt") as file:
        servers = file.read().splitlines()

    report_file = f"logs/report-{datetime.now().strftime('%Y-%m-%d')}.txt"
    os.makedirs("logs", exist_ok=True)

    with open(report_file, "w") as log:
        for server in servers:
            log.write(f"\n--- Checking {server} ---\n")
            print(f"\n--- Checking {server} ---")

            if ping_server(server):
                cpu, memory, disk = check_local_health()
                log.write(f"CPU Usage: {cpu}%\nMemory Usage: {memory}%\nDisk Usage: {disk}%\n")
                print(f"CPU Usage: {cpu}%\nMemory Usage: {memory}%\nDisk Usage: {disk}%")
            else:
                log.write("Server is DOWN ❌\n")
                print("Server is DOWN ❌")

    print(f"\nReport saved to: {report_file}")

if __name__ == "__main__":
    main()

