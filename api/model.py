from pydantic import BaseModel
    
class RemoveBgInRequest(BaseModel):
    image_base64: str
    

class RemoveBgInResponse(BaseModel):
    status_code: int
    message: str
    mask_url: str

class GetMaskBGRequest(BaseModel): 
    image_base64: str

class GetMaskBGResponse(BaseModel):
    status_code: int
    message: str
    image_base64: str
