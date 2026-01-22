from pydantic import BaseModel
from typing import List,Dict,Optional
from datetime import datetime

class Security(BaseModel):
    present:List[str]
    missing:List[str]
    score:str
    details:Dict[str,str]
    error:Optional[str]=None

class ScanRequest(BaseModel):
    url:str
    
class ScanResponse(BaseModel):
    url: str
    status: str
    response_time_ms: Optional[float] = None
    status_code: Optional[int] = None
    uses_https: bool
    timestamp: datetime
    error: Optional[str] = None
    security_headers: Optional[Security] = None

        