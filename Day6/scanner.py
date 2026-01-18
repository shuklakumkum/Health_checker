#import model
from security_checker import calculate_security_score

#scan the website
def scan_website(url:str):
    detail={
        "url":url,
        "https":url.startswith("https"),
        "ssl": {
            "valid": url.startswith("https")
        },
        "security_headers":{
            "hsts":False,
            "csp":False,
            "x_frame":True,
            "x_content":True
        },
        "vulnerabilities": ["example vuln"],
        "response_time": 1200
    }
    #return result
    detail["security_score"]=calculate_security_score(detail)
    return detail

            