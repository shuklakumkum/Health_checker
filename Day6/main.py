#import model
from fastapi import FastAPI
from scanner import scan_website

#create appliction
app=FastAPI()

#api endppoint
@app.post("/scan")
def scan(url:str):
    return scan_website(url)
