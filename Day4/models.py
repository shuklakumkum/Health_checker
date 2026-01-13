from pydantic import BaseModel
from typing import List,Optional

class Vulnerability(BaseModel):
    type:str
    path:str
    severity:str
    description:Optional[str]=None

class Scan(BaseModel):
    vulnerabilities_found:List[Vulnerability]
    checks_performed:List[str]
    total_found:int
    severity:str
    error:Optional[str]=None

class ScanResponse(BaseModel):
    url:str
    status:str
    uses_https:bool
    response_time:Optional[float]=None
    status_code:Optional[int]=None
    error:Optional[str]=None
    vulnerabilities: Optional[Scan] = None
