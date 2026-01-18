#import model
from fastapi import FastAPI,HTTPException
from models import ScanRequest
from scanner import scan_health

#create application
app=FastAPI(title="website Health Checker")

#Root endpoint
@app.get("/")
def home():
    return{"message":"API is running"}

#scan endpointmake short code
@app.post("/scan")
def scan_website(data: ScanRequest):
    try:
       result=scan_health(data.url)
       return result
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error while scanning the website:{str(e)}"
        )
   