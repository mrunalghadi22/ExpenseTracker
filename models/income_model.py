from bson import ObjectId
from database.mongo import db

income_collection = db["income"]


class IncomeModel:

    @staticmethod
    def create_income(data):
        return income_collection.insert_one(data)

    @staticmethod
    def get_income_by_id(user_id, income_id):
        return income_collection.find_one(
            {
                "_id": ObjectId(income_id),
                "user_id": ObjectId(user_id)
            }
        )

    @staticmethod
    def get_all_income_by_user(user_id):
        return list(
            income_collection.find(
                {
                    "user_id": ObjectId(user_id)
                }
            ).sort("income_date", -1)
        )

    @staticmethod
    def update_income(user_id, income_id, data):
        return income_collection.update_one(
            {
                "_id": ObjectId(income_id),
                "user_id": ObjectId(user_id)
            },
            {
                "$set": data
            }
        )

    @staticmethod
    def delete_income(user_id, income_id):
        return income_collection.delete_one(
            {
                "_id": ObjectId(income_id),
                "user_id": ObjectId(user_id)
            }
        )

    @staticmethod
    def get_total_income(user_id):

        pipeline = [
            {
                "$match": {
                    "user_id": ObjectId(user_id)
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {
                        "$sum": "$amount"
                    }
                }
            }
        ]

        result = list(income_collection.aggregate(pipeline))

        return result[0]["total"] if result else 0
    
    @staticmethod
    def get_income_count(user_id):
        return income_collection.count_documents(
            {
                "user_id": ObjectId(user_id)
            }
        )