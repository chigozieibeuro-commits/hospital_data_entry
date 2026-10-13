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

    query="""INSERT INTO TABLE appointment(name,age,gender,phone,doctor)
    VALUES(%s,%s,%s,%s,%s)
    RETURNING id;
    """
    cursor.execute(
        query,
        (data.Name,data.Age,data.Gender,data.Phone,data.Doctor
         )
    )

    con.commit()
    cursor.close()
    con.close()

    patient_id=cursor.fetchone()


    return {
        "message:entry successful"
        "patient_id": patient_id
    }