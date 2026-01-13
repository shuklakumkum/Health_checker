#import model
from fastapi import FastAPI
import requests
from datetime import datetime
import file_handler

#create app
app=FastAPI()

@app.post("/scan")
def scan(url:str):
    try:
        final_url = url if url.startswith("http") else "https://" + url
        r = requests.get(final_url, timeout=5)
        data = {
            "url": url,
            "status": "online",
            "status_code": r.status_code,
            "uses_https": url.startswith("https"),
            "timestamp": datetime.now().isoformat()
        }

    #any error occurs
    except Exception as e:
        data={
            "url":url,
            "status":"offline",
            "status_code": None, 
            "uses_https":url.startswith("https"),
            "timestamp":datetime.now().isoformat(),
            "error":str(e)
        }

    file_handler.save_scan_result(data)
    return data

@app.get("/history")
def history(url: str = None):
    if url:
        return file_handler.get_scan_url(url)  # <--- fix function name
    return file_handler.get_scans()
