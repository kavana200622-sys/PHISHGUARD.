
from urllib.parse import urlparse
import ipaddress

def analyze_url(url):

    score = 0
    reasons = []

    # Prepare URL for analysis
    if "://" not in url:
        url = "https://" + url

    parsed = urlparse(url)
    hostname = parsed.hostname or ""
    print("URL LENGTH:", len(url))
    # Check 7: Very long URL
    if len(url) > 75:
        score += 1
        reasons.append("URL is unusually long.")
    # Check 8: Punycode domain
    if "xn--" in hostname.lower():
        score += 2
        reasons.append("Domain contains encoded international characters (Punycode).")
    # Check 1: HTTP instead of HTTPS
    if parsed.scheme == "http":
        score += 1
        reasons.append("Website does not use HTTPS.")

    # Check 2: @ symbol
    if "@" in parsed.netloc:
        score += 2
        reasons.append("URL contains an @ symbol.")

    # Check 3: IP address
    try:
        ipaddress.ip_address(hostname)
        score += 2
        reasons.append("Website uses an IP address instead of a domain name.")
    except ValueError:
        pass

    # Check 4: Suspicious words
    keywords = ["login", "verify", "account", "password", "update"]

    for word in keywords:
        if word in url.lower():
            score += 1
            reasons.append(f"URL contains suspicious keyword: {word}")
            break

    # Check 5: URL shorteners
    shorteners = ["bit.ly", "tinyurl.com", "t.co"]

    if hostname.lower() in shorteners:
        score += 1
        reasons.append("URL uses a shortening service.")

    # Check 6: Too many hyphens
    if hostname.count("-") >= 3:
        score += 1
        reasons.append("Domain contains multiple hyphens.")

    return score, reasons
