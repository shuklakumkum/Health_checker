from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
from typing import Optional
from scanner import check_health

app = FastAPI(title="Website Health + SSL Checker")

# Request model
class ScanRequest(BaseModel):
    url: HttpUrl

# SSL info model
class SSLInfo(BaseModel):
    valid: bool
    expires_in_days: Optional[int]
    expires_on: Optional[str]
    issuer: Optional[str]
    error: Optional[str]

# Response model
class ScanResponse(BaseModel):
    url: str
    checked_at: str
    uses_https: bool
    status: str
    status_code: Optional[int] = None
    response_time_ms: Optional[float] = None
    ssl: Optional[SSLInfo] = None
    error: Optional[str] = None

# API endpoint
@app.post("/scan", response_model=ScanResponse)
def scan(request: ScanRequest):
    return check_health(request.url)
