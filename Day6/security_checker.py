def calculate_security_score(scan):
    score=100  #start with full mark
    tips=[]

   #it check if website uses HTTPS
    if not scan.get("https"):
        score -=20
        tips.append("Enable HTTPS")

    #check if SSL certificatee is valid
    if not scan.get("ssl",{}).get("valid"):
        score -=20
        tips.append("Fix SSL certificate")

    #check security header
    headers = scan.get("security_headers", {})
    missing = sum(1 for h in headers.values() if not h)
    score -= missing * 5
    if missing:
        tips.append("Add security headers")

    #check vulnerabilities
    vulns = len(scan.get("vulnerabilities", []))
    score -= vulns * 10
    if vulns:
        tips.append("Fix vulnerabilities")

    # It check speed
    if scan.get("response_time", 2000) > 1000:
        score -= 10
        tips.append("Improve performance")

    #Decide grade
    if score>=90:
        grade="A"
    elif score>=80:
        grade="B"
    elif score>=70:
        grade="c"
    elif score>=60:
        grade="D"
    else:
        grade="F"

    return {
        "score": max(score, 0),
        "max_score": 100,
        "grade": grade,
        "recommendations": tips
    }