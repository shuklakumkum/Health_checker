
#import model
import requests
from datetime import datetime
import time


def check_health(url):
    result={
        "url":url, 
        "status":"fail", 
        "response_time_ms":None, 
        "status_code":None,
        "uses_https":url.startswith("https://"), 
        "timestamp":datetime.utcnow().isoformat(), 
        "error":None
    }

    try:
        start_time=time.time()
        response=requests.get(url, timeout=5)
        end_time=time.time()

      #calculate response time
        result["response_time_ms"] = round((end_time - start_time) * 1000, 2)
        result["status_code"]=response.status_code
        if response.ok:
            result["status"] = "ok"
        else:
            result["status"] = "fail"

    except requests.exceptions.RequestException as e:
       result["error"] = str(e)
       result["status"] = "fail"
       result["response_time_ms"] = None
       result["status_code"] = None

    return result
