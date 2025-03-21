from fastapi import APIRouter
from models.collections import User, Posts
from schema.schemas import serialize_list
from bson import ObjectId
from config.database import users_collection, posts_collection

router = APIRouter()

#need a get_posts method too, to get all posts
@router.get("/")
async def get_posts():
    #added this line for automating serialization process in schemas.py
    posts = posts_collection.find() 
    posts_list = serialize_list(posts, "posts")
    #changed get_todos to get_posts & todos to posts_list
    #changed list_serial to serialize_list
    #changed collection_name.find() to (posts, "posts") and used find() before it
    return posts_list

#need a post method for adding a post
@router.post("/")
#changed from post_todo to add_post
async def add_post(post: Posts):
    posts_collection.insert_one(dict(post))
    return {"message": "Post created successfully"}

#need a put method for updating a post
@router.put("/{id}")
#changed from put_todo to update_post
async def update_post(id: str, post: Posts):
    posts_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(post)})
    return {"message": "Post updated successfully"}

#need a delete method for deleting a post
@router.delete("/{id}")
#changed from delete_todo to delete_post
async def delete_post(id: str):
    posts_collection.find_one_and_delete({"_id": ObjectId(id)})
    return {"message": "Post deleted successfully"}