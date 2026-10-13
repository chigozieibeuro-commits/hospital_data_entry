from pydantic import  BaseModel
from datetime import  date

class Records(BaseModel):
    Name:str
    Age:int
    Gender:str
    Phone:str
    Doctor:str
    date:date



