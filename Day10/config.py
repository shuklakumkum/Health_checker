import os
from dotenv import load_dotenv

load_dotenv()

API_HOST=os.getenv("API_HOST","127.0.0.1")
API_PORT_int(os.getenv("API_PORT",8000))
SCAN_TIMEOUT=int(os.getenv("SCAN_TIMEOUT",10))
MAX_SCANS_PER_DAY=  int(os.getenv("MAX_SCANS_PER_DAY",100))
API_KEY=os.getenv("API_KEY","")