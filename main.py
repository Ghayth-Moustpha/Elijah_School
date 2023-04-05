from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import topic 

from database import(
    fetchpattrenas ,
    fetchtopic,
    add_topic,
    remove_topic,
    update
)

#app object
app = FastAPI () ; 
origins = ['http:localhost:3000'] 
 
app.add_middleware (
    CORSMiddleware ,
    allow_origins = origins, 
    allow_credentials = True ,
    allow_methods = ["*"] , 
    allow_headers= ["*"] , 
)

@app.get("/") 
async def read_root ():
    return ({"ping" , "pong"})  
@app.get("/api/patterns") 
async def getPatterns () : 
    response = await fetchpattrenas() 
    return response

@app.get("/api/topic{tag}" , response_model= topic) 
async def get_topic (tag) : 
    response = await fetchtopic (tag) 
    if response:
        return response 
    else : 
        raise HTTPException(404, "there is no Topic ")  

@app.post("/api/topic", response_model= topic) 
async def post_todo (Topic : topic ) :
    response = await add_topic (Topic.dict())
    if response:
        return response 
    else : 
        raise HTTPException( 400, "somthing went wrong ")  
@app.put("/api/topic{tag}", response_model= topic) 
async def update_topic(tag:str, question :str , ans : str ):
    response = await update (tag , question, ans )  
    if response:
        return response 
    else : 
        raise HTTPException( 400, "somthing went wrong ")  

@app.delete("/api/topic{tag}") 
async def delete_todo (tag) :
    res = await remove_topic (tag)
    if res:
        return "Topic Deleted successfuly " 
    else:
        raise HTTPException( 400, "somthing went wrong ")   





