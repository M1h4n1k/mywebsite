import motor.motor_asyncio
import os

client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGODB_URL", 'mongodb://localhost:27017'))
db = client.get_database("mywebsite")
projects = db.get_collection("projects")
posts = db.get_collection("posts")
