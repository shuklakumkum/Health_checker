#import model
import requests
from typing import Dict,Any
from functools import lru_cache

#save response time
@lru_cache(maxsize=100)
def get_response_time(url):
    response = requests.get(url,timeout=5)
    return round(response.elapsed.total_seconds()*1000,2)

#scan website and give result
def scan_website(url:str)->Dict[str,Any]:
    try:
        response_time=get_response_time(url)
        return{
            "url": url,
            "status": "success",
            "response_time_ms": response_time
        }

    #return error message 
    except requests.exceptions.RequestException as error:
        return{
            "url":url,
            "status":"error",
            "message":str(error)
        }
        