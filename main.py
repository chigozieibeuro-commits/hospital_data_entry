import  fastapi
from fastapi import FastAPI

from  data_base import  connection
from schema import  Records


app=FastAPI()

@app.get("/")
def get():
    return {
        "message: hospital fastAPI is running"
    }

@app.post("/enter_patients")
def post(data:Records):
    con=connection()
    cursor=con.cursor()

    query="""INSERT INTO TABLE appointment(
    """