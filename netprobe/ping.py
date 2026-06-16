
import platform
import subprocess

def ping_host(host: str) -> bool:
    """Ping a host to check availability.
    
    Args:
        host: IP address or domain name
    
    Returns:
        True if host is reachable, False otherwise
    """
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]

    result = subprocess.run(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    return result.returncode == 0
