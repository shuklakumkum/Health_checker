#import Basemodel
from pydantic import BaseModel
from typing import List,Optional

#store final score
class securityScore(BaseModel):
    score:int
    max_score:int
    grade:str
    recommendations:List[str]

#store all scan result
class ScanResponse(BaseModel):
    url:str
    https:bool
    ssl:dict
    security_headers:dict
    vulnerabilities:list
    response_time:float
    security_score:Optional[securityScore]=None
    