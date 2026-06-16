import dns.resolver
import dns.exception

def dns_lookup(domain: str) -> list:
    """Perform DNS lookup for a domain.
    
    Args:
        domain: Domain name to look up
    
    Returns:
        List of IP addresses for the domain
    """
    try:
        answers = dns.resolver.resolve(domain, "A")
        return [rdata.to_text() for rdata in answers]
    except dns.resolver.NXDOMAIN:
        # Domain does not exist
        return []
    except dns.resolver.Timeout:
        # DNS query timed out
        return []
    except dns.exception.DNSException:
        # Other DNS errors
        return []
    except Exception:
        # Fallback for any other exceptions
        return []
