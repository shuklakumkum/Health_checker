from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ScanResponse(BaseModel):
    url:str
    status:str
    response_time_ms:Optional[float]=None
    status_code:Optional[int]=None
    uses_https: bool
    timestamp:datetime
    error:Optional[str]=None
