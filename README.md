# Server Health Check Automation

A simple Python script to check the health of multiple servers.  
It pings each server and checks basic metrics like **CPU**, **Memory**, and **Disk Usage**.

## Features
- Ping servers to check availability  
- Get CPU, memory, and disk usage  
- Save output to log files  

---

## Prerequisites
Make sure you have **Python 3.6+** installed.  
Install the required dependencies using:

```bash
 pip install -r requirements.txt

```

## How to Run

Clone this repository:

- git clone https://github.com/YOUR-USERNAME/python-server-health-check.git
- cd python-server-health-check


Install dependencies:

pip install -r requirements.txt


Add your servers to servers.txt:

- 127.0.0.1
- google.com


Run the script:

python health_check.py


