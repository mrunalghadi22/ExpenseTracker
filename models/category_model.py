from bson import ObjectId
from database.mongo import category_collection


class CategoryModel:

    @staticmethod
    def create_category(data):
        return category_collection.insert_one(data)

    @staticmethod
    def get_categories_by_user(user_id):
        return list(
            category_collection.find(
                {"user_id": ObjectId(user_id)}
            ).sort("name", 1)
        )

    @staticmethod
    def get_category_by_id(category_id):
        return category_collection.find_one(
            {
                "_id": ObjectId(category_id)
            }
        )

    @staticmethod
    def get_category_by_name(user_id, name):
        return category_collection.find_one(
            {
                "user_id": ObjectId(user_id),
                "name": {
                    "$regex": f"^{name}$",
                    "$options": "i"
                }
            }
        )

    @staticmethod
    def update_category(category_id, data):
        return category_collection.update_one(
            {
                "_id": ObjectId(category_id)
            },
            {
                "$set": data
            }
        )

    @staticmethod
    def delete_category(category_id):
        return category_collection.delete_one(
            {
                "_id": ObjectId(category_id)
            }
        )