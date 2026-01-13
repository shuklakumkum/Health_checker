#import models to create API
from fastapi import FastAPI
from models import ModelReq,ModelResponse
from scanner import check_health

#create FastAPI application
main = FastAPI(title="website Health Checker API")

#Root endpoint to  accept the API
@main.get("/")
def welcome():
    return{"message":"Welcome to Website Health Checker API"}

#to check API is running
@main.get("/health")
def health():
    return{"status":"API is running"}

#it scan health of website
@main.post("/scan",response_model=ModelResponse)
def check(scan: ModelReq):
    result = check_health(scan.url)
    return result