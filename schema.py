from pydantic import  BaseModel
from datetime import  date

class Records(BaseModel):
    Name:str
    Age:int
    Gender:str
    Phone:int
    Doctor:str
    date:date



