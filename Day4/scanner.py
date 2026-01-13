#import request
import requests

#scan a website
def check_vulnerabilities(url):
    paths=[
        "/.git/HEAD",
        "/.git/config",
        "/.env",
        "/config.php",
        "/backup.sql",
        "/backup/",
        "/admin/",
        "/.DS_Store",
    ]
    #list to collect and store
    vulnerabilities_found=[]
    
    #try each path one by one
    for path in paths:
        full_url=url.rstrip('/')+path
        try:
           response=requests.get(full_url,timeout=5,allow_redirects=False)
           if response.status_code in(200,403):  
              vulnerabilities_found.append({
                    "type":"Exposed file or directory",
                    "path":path,
                    "severity": "high" if path in ["/.git/HEAD", "/.git/config", "/.env", "/config.php"] else "medium"
              })
           elif response.status_code == 403:
               vulnerabilities_found.append({
                    "type": "Forbidden file hint",
                    "path": path,
                    "severity": "low"
                })
        except Exception as e:
            print(f"Error checking {full_url}: {e}")
    
    #it chekc HTTP method that allow
    try:
       response = requests.options(url, timeout=5)
       allowed_methods = response.headers.get("Allow", "")
       for method in ["PUT", "DELETE", "TRACE"]:
            if method in allowed_methods:
               vulnerabilities_found.append({
                    "type": "Dangerous HTTP method allowed",
                    "path": url,
                    "severity": "high",
                    "method": method
                })
    except Exception as e:
        print(f"Error checking HTTP methods: {e}")
    #return result
    return {
        "url": url,
        "total_found": len(vulnerabilities_found),
        "vulnerabilities_found": vulnerabilities_found
    }

