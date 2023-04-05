from pydantic import BaseModel 

class topic (BaseModel) :
    tag : str 
    questions : str
    responses: str

    