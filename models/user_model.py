from bson import ObjectId
from datetime import datetime
from database.mongo import db


class UserModel:

    collection = db.users

    @staticmethod
    def email_exists(email):
        return UserModel.collection.count_documents(
        {"email": email},
        limit=1
    ) > 0

    @staticmethod
    def create_user(user_data):
        """
        Insert a new user into MongoDB.
        """

        return UserModel.collection.insert_one(user_data)


    @staticmethod
    def get_user_by_email(email):
        """
        Find user using email.
        """

        return UserModel.collection.find_one(
            {"email": email}
        )


    @staticmethod
    def get_user_by_id(user_id):
        """
        Find user using ObjectId.
        """

        return UserModel.collection.find_one(
            {"_id": ObjectId(user_id)}
        )


    @staticmethod
    def update_user(user_id, update_data):

        update_data["updated_at"] = datetime.utcnow()

        return UserModel.collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": update_data}
        )


    @staticmethod
    def deactivate_user(user_id):

        return UserModel.collection.update_one(
            {"_id": ObjectId(user_id)},
            {
                "$set": {
                    "is_active": False,
                    "updated_at": datetime.utcnow()
                }
            }
        )
    
    @staticmethod
    def update_password(user_id, hashed_password):

        return UserModel.collection.update_one(
            {
                "_id": ObjectId(user_id)
            },
            {
                "$set": {
                    "password": hashed_password
                }
            }
        )