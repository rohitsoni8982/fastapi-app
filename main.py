from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Dict, Any
from DataFile import databassconnection


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Add_Card(BaseModel):
    firstname : str
    lastname : str
    email : str
    address : str
    city : str
    state : str
    pincode : str
    country : str
    phone : str

@app.get("/your-endpoint")
async def your_get_method():
    return {"message": "This is a GET response"}

@app.post("/add_card")
def Add_Card(data: Dict[Any, Any]):
    data = dict(data)
    data = databassconnection.data_store(data)
    return "successfully data stored"