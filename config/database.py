from pymongo import MongoClient

client = MongoClient("mongodb+srv://yasminkhan2014yk:Mongo654321!@cluster0.xetvj.mongodb.net/?appName=Cluster0")

db = client.Food_Scroll_db 
#changed from todo_db to Food_Scroll_db

users_collection = db["users"]
#changed from collection_name to users_collection, and todo_collection to users

posts_collection = db["posts"]
#added this line for posts collection

#xyz_collection = db["xyz"] 