#file renamed from todos.py to collections.py

from pydantic import BaseModel

#renamed from Todo to User
class User(BaseModel):
    _id: str        #(Object ID)
    username: str
    email: str
    password: str  # This should be stored as a hashed password
    profilePicture: str  # (String or Binary Data)
    location: dict  # GeoJSON Point or str
    bio: str = None
    preferences: list[str] = []
    favorites: list[str] = []
    joinedDate: datetime
    lastLogin: datetime  # (Date/Timestamp)

#renamed from Todo to Posts
class Posts(BaseModel):
    _id: str        #(Object ID)
    userId: str     #(Object ID, foreign key)
    title: str
    images: list[str]  # (Array of Strings or Binary Data)
    location: dict  # (GeoJSON Point or String)
    tags: list[str]  # (Array of Strings)
    availability: str  # (String or Date/Time Range)
    price: float = None
    createdDate: datetime  # (Date/Timestamp)
    updatedDate: datetime = None  # (Date/Timestamp)
    likes: int
    comments: list[dict] = []  # (Array of Objects)
    ratings: list[int] = []  # (Array of numbers)
