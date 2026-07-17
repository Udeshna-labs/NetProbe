import platform
import subprocess
import re
import ipaddress

def ping_host(host: str) -> bool:
    """Ping a host to check availability.
    
    Args:
        host: IP address or domain name
    
    Returns:
        True if host is reachable, False otherwise
    """
    # Strict validation - only allow valid IPs and domain names
    try:
        # Try to parse as IP address
        ipaddress.ip_address(host)
    except ValueError:
        # Try to validate as domain name
        domain_pattern = r'^[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$'
        if not re.match(domain_pattern, host):
            return False
    
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]

    try:
        result = subprocess.run(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=5
        )
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        return False
    except Exception:
        return False
