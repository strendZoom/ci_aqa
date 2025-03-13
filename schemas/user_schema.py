from pydantic import BaseModel

class UserSchema(BaseModel):
    userId: str
    expires: str
    isActive: bool

class TokenSchema(BaseModel):
    token : str
    expires : str
    status : str
    result : str