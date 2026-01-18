#import model
from fastapi import FastAPI
from scanner import scan_website

#create application
app=FastAPI(title="Day9-performance&code Quality")

#route to check api is running
@app.get("/")
def home():
    return{"message":"Day9 API running"}

#route to scan website
@app.post("/scan")
def scan(url:str):
    return scan_website(url)