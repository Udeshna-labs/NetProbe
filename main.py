from netprobe.ping import ping_host
from netprobe.scanner import scan_ports
from netprobe.dns_lookup import dns_lookup
from netprobe.utils import print_banner
import re

COMMON_PORTS = [21, 22, 25, 53, 80, 110, 139, 143, 443, 445, 8080]

def is_valid_target(target: str) -> bool:
    """Validate if target is a valid IP or domain."""
    # Simple validation for IPv4
    ipv4_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    # Simple validation for domain (basic check)
    domain_pattern = r'^[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$'
    
    return bool(re.match(ipv4_pattern, target)) or bool(re.match(domain_pattern, target))

def main():
    print_banner()
    target = input("Enter target (IP or domain): ").strip()
    
    # Validate input
    if not target:
        print("[✘] Target cannot be empty")
        return
    
    if not is_valid_target(target):
        print("[✘] Invalid IP address or domain format")
        return

    print("\n[+] Checking host availability...")
    if ping_host(target):
        print("[✔] Host is UP")
    else:
        print("[✘] Host is DOWN")
        return

    print("\n[+] Scanning common ports...")
    open_ports = scan_ports(target, COMMON_PORTS)

    if open_ports:
        print(f"[✔] Open ports: {open_ports}")
    else:
        print("[✘] No open ports found")

    print("\n[+] Performing DNS lookup...")
    ips = dns_lookup(target)

    if ips:
        print(f"[✔] IP Addresses: {ips}")
    else:
        print("[✘] No DNS records found")

if __name__ == "__main__":
    main()
