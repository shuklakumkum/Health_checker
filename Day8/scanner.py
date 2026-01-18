#import request
import requests

#It check website is working
def scan_health(url:str):
    try:
        response=requests.get(url,timeout=5)

        return{
            "website_status":"online",
            "http_status":response.status_code,
            "response_time_ms":response.elapsed.total_seconds()*1000
        }

    #If website take time
    except requests.exceptions.Timeout:
        print("TImeout occurred while trying to reach:",url)
        return{
            "website_status":"offline",
            "reason":"Timeout",
            "details":"Website did not respond in 5 seconds",
            "suggestion":"check your network connection"
        }
     
     #if SSL certificate is expired
    except requests.exceptions.SSLError as ssl_issue:
        print("SSL error detected for:",url)
        return{
            "website_status":"offline",
            "reason":"SSL Error",
            "details":str(ssl_issue),
            "suggestion":"verify SSL certificate"
        }

    #If website is not reach
    except requests.exceptions.ConnectionError as conn_issue:
        print("connction error for:",url)
        return {
            "website_status":"offline",
            "reason":"connection Failed",
            "details":str(conn_issue),
            "suggestion":"check the URL or your internet connection"
        }

    #for any other unexcepted error
    except Exception as unexpected:
        print("unexpected error for:",url)
        return{
            "website_status":"offline",
            "reason":"Unkown Error",
            "details":str(exc),
            "suggestion":"Try again later"
        }