import socket
import threading
import re
import subprocess
from IPy import IP
from concurrent.futures import ThreadPoolExecutor

def scan(target):
    converted_ip = check_ip(target)
    print('\n' + '[+] Scanning target: ' + str(target))
    detect_os(converted_ip)

    try:
        start_port = int(input("Start port: "))
        end_port = int(input("End port: "))
    except ValueError:
        print("[!] Please enter valid port numbers.")
        return

    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, converted_ip, port)


def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)

BANNER_PAYLOADS = {
    80: b"HEAD / HTTP/1.0\r\n\r\n",
    443: b"HEAD / HTTP/1.0\r\n\r\n",
    21:  b"",        # FTP
    22:  b"",        # SSH
    25:  b"",        # SMTP
    110: b"",        # POP3
    143: b"",        # IMAP
}

def grab_banner(ipaddress, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1.5)
            result = sock.connect_ex((ipaddress, port))

            payload = BANNER_PAYLOADS.get(port, b"\r\n")
            if payload:
                sock.send(payload)
            
            banner = sock.recv(1024).decode(errors="ignore").strip()

            first_line = banner.splitlines()[0] if banner else ""
            return first_line[:100]
    except:
        return None

def scan_port(ipaddress, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex((ipaddress, port))
            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "unknown"

                banner = grab_banner(ipaddress, port)
                if banner:
                    print(f"[+] Port {port} open - {service} | Banner: {banner}")
                else:
                    print(f"[+] Port {port} open - {service}")
    except:
        pass


def detect_os(ip):
    try:
        result = subprocess.run(["ping", "-c", "1", "-W", "1", ip],
            capture_output=True,
            text=True
        )
        ttl_match = re.search(r"ttl=(\d+)", result.stdout.lower())
        if ttl_match:
            ttl = int(ttl_match.group(1))
            if ttl <= 64:
                os_guess = "Linux / macOS / Android"
            elif ttl <= 128:
                os_guess = "Windows"
            elif ttl <= 255:
                os_guess = "Cisco / Network device"
            else:
                os_guess = "Necunoscut"
            print(f"[*] OS detectat: {os_guess} (TTL={ttl})")
        else:
            print("[!] Host offline or ICMP blocked")
    except Exception as e:
        print(f"[!] Eroare ping: {e}")


targets = input("[+] Enter target/s to scan (split multiple targets with ','): ")
if ',' in targets:
    for ip_add in targets.split(','):
        scan(ip_add.strip())
else:
    scan(targets)
