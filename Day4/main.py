#import model
from fastapi import FastAPI
from pydantic import BaseModel,HttpUrl
from typing import Optional
from datetime import datetime

from security_checker import check_vulnerabilities
from models import Scan,ScanResponse

#create app
app=FastAPI()

#request model
class ScanRequest(BaseModel):
    url:HttpUrl

@app.post("/scan",response_model=ScanResponse)
def scan_website(request:ScanRequest):
    url=request.url
    scan_result={
        "url":str(url),
        "status":"ok",
        "uses_https": str(url).startswith("https://")

    }
        
    #run vulnerability scan
    try:
        vulnerabilities_data=check_vulnerabilities(str(url))
        scan_result["vulnerabilities"] = Scan(**vulnerabilities_data)
    except Exception as e:
        scan_result["error"]=str(e)

    return scan_result