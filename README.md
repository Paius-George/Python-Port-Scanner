# Python Port Scanner

*[Versiunea în limba română →](README.ro.md)*

A fast port scanner written in Python that uses multithreading for performance and includes TTL-based operating system detection.

## Features

* **Multithreading:** Uses `ThreadPoolExecutor` for fast scanning.
* **OS Detection:** Identifies the operating system (Windows/Linux/Cisco) by analyzing the ICMP TTL.
* **Service Detection:** Identifies common services based on the port number.
* **Banner Grabbing:** Attempts to extract the service banner for open ports.
* **DNS Support:** You can enter IP addresses or domain names (e.g. google.com).

## Installation

1. Clone the repository:

```
git clone https://github.com/Paius-George/Python-Port-Scanner
cd Python-Port-Scanner/
```

2. Install the dependencies:

```
pip install -r requirements.txt
```

## Usage
Run the script and follow the instructions in the terminal:

```
python portscanner.py
```

## Output

<img alt="image" src="https://github.com/user-attachments/assets/14e0d189-8642-4307-9f1d-4dccb3958e77" />


---
> This tool is created strictly for educational purposes. The user is solely responsible for how they choose to use it. Scanning networks without prior permission may be illegal.
