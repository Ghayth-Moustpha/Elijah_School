from model import topic 
#MangoDB Driver 
import motor.motor_asyncio

client =  motor.motor_asyncio.AsyncIOMotorClient ("mongodb+srv://<elijah>:<elijahelijah>@cluster0.umryc.mongodb.net/test") 

db =client.db 
collection = db.pattrens 

async def fetchtopic (tag):
    doc = await collection.find_one({"tag" : tag}) 
    return doc 
async def fetchpattrenas ():
    pattrens = [] 
    intents = collection.find ({}) 
    async for element in intents:
        pattrens.append(topic (**element))
    return pattrens 
 
async def add_topic (top):
    result = await collection.insert_one(top) 
    return top  

async def remove_topic (tag):
    await collection.delete_one({"tag":tag}) 
    return True 

async def update(tag , ques , res  ): 
    await collection.update_one({'tag' : tag }, {'$push':{'questions' : ques } } ) 
    return True 

