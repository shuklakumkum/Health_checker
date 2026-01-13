import requests
from models import Vulnerability

def check_vulnerabilities(url):
    detail={
        "vulnerabilities_found":[],
        "checks_performed":[],
        "total_found":0,
        "severity":"none",
        "error":None
    }

    paths=[
        ("/.git/HEAD","high"),
        ("/.git/config","high"),
        ("/.env","high"),
        ("/config.php","high"),
        ("/backup.sql","medium"),
        ("/backup/","medium"),
        ("/admin/","medium"),
        ("/.DS_Store","low"),
    ]
    try:
        for path,severity in paths:
            full_url=url.rstrip('/')+path
            detail["checks_performed"].append(path)
            response=requests.get(full_url,timeout=5,allow_redirects=False)
            if response.status_code in(200,403):
                detail["vulnerabilities_found"].append({
                    "type":"Exposed file or directory",
                    "path":path,
                    "severity":severity,
            })
            options=requests.options(url,timeout=5)
            allowed_methods=options.headers.get("Allow","")
            for method in["PUT","DELETE","TRACE","PATCH"]:
                if method in allowed_methods:
                    detail["vulnerabilities_found"].append({
                        "type":"Dangerous HTTP method",
                        "path":method,
                        "severity":"medium"
                     })

            detail["total_found"]=len(detail["vulnerabilities_found"])
            severities=[v["severity"]for v in detail["vulnerabilities_found"]]
            if "high" in severities:
                detail["severity"]="high"
            elif "medium" in severities:
                detail["severity"]="medium"
            elif "low" in severities:
                detail["severity"]="low"

    except Exception as e:
        detail["error"]=str(e)

    return detail