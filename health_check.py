import os
import platform
import subprocess
from datetime import datetime
import psutil

def ping_server(host: str) -> bool:
    """Return True if host responds to a single ping (cross-platform)."""
    count_flag = "-n" if platform.system().lower().startswith("win") else "-c"
    try:
        result = subprocess.run(
            ["ping", count_flag, "1", host],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=5,
        )
        return result.returncode == 0
    except Exception:
        return False

def check_local_health():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    return cpu, mem, disk

def main():
    # read servers list
    with open("servers.txt", "r", encoding="utf-8") as f:
        servers = [line.strip() for line in f if line.strip()]

    os.makedirs("logs", exist_ok=True)
    report_path = f"logs/report-{datetime.now().strftime('%Y-%m-%d')}.txt"

    with open(report_path, "w", encoding="utf-8") as log:
        for server in servers:
            header = f"--- Checking {server} ---"
            print(header); log.write(header + "\n")

            if ping_server(server):
                print("Server is UP ✅"); log.write("Server is UP ✅\n")
                cpu, mem, disk = check_local_health()
                line = f"CPU: {cpu}% | Memory: {mem}% | Disk: {disk}%"
                print(line); log.write(line + "\n\n")
            else:
                print("Server is DOWN ❌"); log.write("Server is DOWN ❌\n\n")

    print(f"\nReport saved to: {report_path}")

if __name__ == "__main__":
    main()
