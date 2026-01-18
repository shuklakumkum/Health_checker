#import model
from pydantic import BaseModel,HttpUrl,validator

#It check user input
class ScanRequest(BaseModel):
    url:HttpUrl

    @validator("url")
    def url(cls,v):
        url_str=str(v)
     
        if url_str.startswith("file://"):
            raise ValueError("Local File URLs are not allowed")

        if len(url_str)>500:
            raise ValueError("URL is too long")

        return v