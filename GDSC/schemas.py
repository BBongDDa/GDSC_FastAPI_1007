from pydantic import BaseModel

class User(BaseModel):
    no: int
    id: str
    name: str
    
    class Config():
        orm_mode = True