from pydantic import BaseModel,HttpUrl
from datetime import datetime

class ScanRequest(BaseModel):
    url:HttpUrl

class ScanResponse(BaseModel):
    "url":str
    "status":str
    "response_time_ms":None
    "status_code":None
    "uses_https":bool
    "timestamp":datetime
    "error":None
