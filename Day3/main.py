from fastapi import FastAPI
from models import ScanRequest,ScanResponse
from scanner import scan

app=FastAPI(title="website Health Checker")

@app.post("/scan",response_model=ScanResponse)
def scan_endpoint(data:ScanRequest):
    return scan(data.url)