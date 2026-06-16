import socket

def scan_port(host: str, port: int, timeout: float = 1.0) -> bool:
    """Scan a single port on a host.
    
    Args:
        host: IP address or domain name
        port: Port number to scan
        timeout: Connection timeout in seconds
    
    Returns:
        True if port is open, False otherwise
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        result = s.connect_ex((host, port))
        return result == 0

def scan_ports(host: str, ports: list) -> list:
    """Scan multiple ports on a host.
    
    Args:
        host: IP address or domain name
        ports: List of port numbers to scan
    
    Returns:
        List of open ports
    """
    open_ports = []
    for port in ports:
        if scan_port(host, port):
            open_ports.append(port)
    return open_ports
