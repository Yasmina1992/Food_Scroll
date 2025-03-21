#changed individual_serial to serialize_document
#serializing a list of users or posts
#function to automate both user and post serializations
def serialize_document(doc, collection_name) -> dict:
    if collection_name == "users":
        return {
            "id": str(doc["_id"]),
            "username": doc["username"],
            "email": doc["email"],
            "password": doc["password"],
            "profilePicture": doc["profilePicture"],
            "location": doc["location"],
            "bio": doc["bio"],
            "preferences": doc["preferences"],
            "favorites": doc["favorites"],
            "joinedDate": doc["joinedDate"],
            "lastLogin": doc["lastLogin"]
        }
    elif collection_name == "posts":
        return {
            "id": str(doc["_id"]),
            "userId": str(doc["userId"]),
            "title": doc["title"],
            "images": doc["images"],
            "location": doc["location"],
            "tags": doc["tags"],
            "availability": doc["availability"],
            "price": doc["price"],
            "createdDate": doc["createdDate"],
            "updatedDate": doc["updatedDate"],
            "likes": doc["likes"],
            "comments": doc["comments"],
            "ratings": doc["ratings"]
        }
    return doc


#renamed from list_serial to serialize_list
def serialize_list(docs, collection_name) -> list:
    return [serialize_document(doc, collection_name) for doc in docs]

