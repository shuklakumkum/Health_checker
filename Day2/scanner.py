import requests
from urllib.parse import urlparse
from datetime import datetime
from SSL_checker import check_ssl

def check_health(url):
    url_str=str(url)  # Convert HttpUrl to string
    scan_result={}
    scan_result["url"]=url_str
    scan_result["checked_at"]=datetime.utcnow().isoformat()
    scan_result["uses_https"]=urlparse(url_str).scheme == "https"

    try:
        http_response=requests.get(url_str, timeout=5)
        scan_result["status_code"]=http_response.status_code
        scan_result["response_time_ms"]=http_response.elapsed.total_seconds() * 1000
        scan_result["status"]="online"

    except requests.exceptions.Timeout:
        scan_result["status"]="offline"
        scan_result["error"]="Request timed out"

    except requests.exceptions.RequestException as request_error:
        scan_result["status"]="offline"
        scan_result["error"]=str(request_error)

    # Check SSL only if HTTPS
    try:
        if scan_result["uses_https"]:
            scan_result["ssl"]=check_ssl(url_str)
        else:
            scan_result["ssl"]=None
    except Exception as e:
        scan_result["ssl"]={
            "valid":False,
            "expires_in_days":None,
            "expires_on":None,
            "issuer":None,
            "error":str(e)
        }

    return scan_result
