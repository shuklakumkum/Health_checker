#import request
import requests

#import security header
def check_security_headers(url: str):
    headers_check = [
       "Strict-Transport-Security",
        "X-Content-Type-Options",
        "X-Frame-Options",
        "Content-Security-Policy"
    ]

#store header detail
    detail={
       "present":[],
       "missing":[],
       "score":"",
       "details":{},
       "error":None,
    }
    #get request
    try:
       response=requests.get(url,timeout=10)

       for header in headers_check:
            if header in response.headers:
               detail["present"].append(header)
               detail["details"][header]=response.headers[header]
            else:
               detail["missing"].append(header)

      
      #calculate security sore
       detail["score"]=f"{len(result['present'])}/{len(headers_check)}"

    except Exception as e:
       detail["error"]=str(e)  

   #return result   
    return detail