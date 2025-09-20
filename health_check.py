import os
import platform
import subprocess
from datetime import datetime
import psutil

def ping_server(host: str) -> bool:
   
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
    return (
        psutil.cpu_percent(interval=1),
        psutil.virtual_memory().percent,
        psutil.disk_usage("/").percent if platform.system() != "Windows"
        else psutil.disk_usage("C:\\").percent
    )

def main():
    with open("servers.txt", "r", encoding="utf-8") as f:
        servers = [s.strip() for s in f if s.strip()]

    os.makedirs("logs", exist_ok=True)
    report = f"logs/report-{datetime.now().strftime('%Y-%m-%d')}.txt"

    with open(report, "w", encoding="utf-8") as log:
        for server in servers:
            hdr = f"--- Checking {server} ---"
            print(hdr); log.write(hdr + "\n")

            if ping_server(server):
                print("Server is UP "); log.write("Server is UP \n")
                cpu, mem, disk = check_local_health()
                line = f"CPU: {cpu}% | Memory: {mem}% | Disk: {disk}%"
                print(line); log.write(line + "\n\n")
            else:
                print("Server is DOWN "); log.write("Server is DOWN \n\n")

    print(f"\nReport saved to: {report}")

if __name__ == "__main__":
    main()
