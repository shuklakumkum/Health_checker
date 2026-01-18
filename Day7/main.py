# main.py
from fastapi import FastAPI
from models import ScanRequest,ScanResponse

app = FastAPI(title="Website Health Checker API")

@app.post("/scan",response_model=ScanResponse)
def scan_website(request:ScanRequest):
    if not request.url.startswith("http"):
        raise HTTPException(status_code=400,detail="Invalid URL")
    
    detail=scan_site(request.url)
    return detail
    