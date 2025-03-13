from pydantic import BaseModel

class UserSchema(BaseModel):
    userId: str
    username : str
    password : str
    token : str
    expires: str
    created_date : str
    isActive: bool

class TokenSchema(BaseModel):
    token : str
    expires : str
    status : str
    result : str