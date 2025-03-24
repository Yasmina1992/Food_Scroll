from fastapi import APIRouter
from models.collections import User, Posts
from schema.schemas import serialize_list
from bson import ObjectId
from config.database import users_collection, posts_collection

'''need to separate the routes for users and posts
so that the user routes are in one file and the post routes are in another file, 
to keep the code organized and avoid confusion'''


router = APIRouter(prefix="/users", tags=["Users"])
# GET Request Method
@router.get("/")
async def get_users():
    #added this line for automating serialization process in schemas.py
    users = users_collection.find() 
    users_list = serialize_list(users, "users")
    #changed get_todos to get_users & todos to users_list
    #changed list_serial to serialize_list
    #changed collection_name.find() to (users, "users") and used find() before it
    return users_list


#POST Request Method
@router.post("/")
#changed from post_todo to add_user
async def add_user(user: User):
    users_collection.insert_one(dict(user))
    return {"message": "User created successfully"}


#PUT Request Method (updating a user)
@router.put("/{id}")
#changed from put_todo to update_user
async def update_user(id: str, user: User,):
    users_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})
    return {"message": "User updated successfully"}


'''async def put_todo(id: str, todo: Todo):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)})
    return {"message": "Todo updated successfully"}'''

#DELETE Request Method
@router.delete("/{id}")
#changed from delete_todo to delete_user
async def delete_user(id: str):
    users_collection.find_one_and_delete({"_id": ObjectId(id)})
    return {"message": "User deleted successfully"}
