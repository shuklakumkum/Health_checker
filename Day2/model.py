from pydantic import BaseModel
from typing import Optional

#store ssl information
class SSL(BaseModel):
    valid:bool
    expires_in_days:Optional[int]
    expires_on:Optional[str]
    issuer:Optional[str]
    error:Optional[str]

#update ssl info
class ScanResponse(BaseModel):
    url:str
    status:str
    response_time_ms:Optional[float]=None
    status_code:Optional[int]=None
    uses_https:bool
    ssl:Optional[SSLInfo]=None