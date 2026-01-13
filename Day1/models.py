#import model
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

#request body
class ModelReq(BaseModel):
    url:str

#response body
class ModelResponse(BaseModel):
    url:str
    status:str
    response_time_ms:float=None
    status_code:int=None
    uses_https:bool
    timestamp:datetime
    error:Optional[str]=None