import requests
from datetime import datetime
from security_checker import check_security_headers
from models import Security  # make sure you import this

def scan(url: str):
    result = {
        "url": url,
        "status": "down",               # matches ScanResponse
        "response_time_ms": None,
        "status_code": None,            # matches ScanResponse
        "uses_https": url.startswith("https"),
        "timestamp": datetime.utcnow(),
        "error": None,
        "security_headers": None,
    }

    try:
        response = requests.get(url, timeout=10)
        result["status"] = "up"
        result["status_code"] = response.status_code
        result["response_time_ms"] = response.elapsed.total_seconds() * 1000

    except Exception as e:
        result["error"] = str(e)

    # wrap dict returned from check_security_headers into Security model
    result["security_headers"] = Security(**check_security_headers(url))

    return result
