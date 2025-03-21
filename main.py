from fastapi import FastAPI
from routes import users, posts 
#changed from route to users and posts

app = FastAPI()

app.include_router(users.router)
app.include_router(posts.router)

#added this line to include the posts router in the app