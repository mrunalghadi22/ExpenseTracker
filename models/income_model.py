from bson import ObjectId
from database.mongo import db
from datetime import datetime

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
    
    @staticmethod
    def get_recent_income(user_id, limit=5):

        return list(
            income_collection.find(
                {
                    "user_id": ObjectId(user_id)
                }
            )
            .sort(
                [
                    ("income_date", -1),
                    ("created_at", -1)
                ]
            )
            .limit(limit)
        )
    
    @staticmethod
    def get_total_income_this_month(user_id):

        from datetime import datetime

        today = datetime.utcnow()

        start = datetime(
            today.year,
            today.month,
            1
        )

        pipeline = [

            {
                "$match": {
                    "user_id": ObjectId(user_id),
                    "income_date": {
                        "$gte": start
                    }
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

        result = list(
            income_collection.aggregate(pipeline)
        )

        return result[0]["total"] if result else 0
    
    @staticmethod
    def get_monthly_income(user_id):

        pipeline = [

            {
                "$match": {
                    "user_id": ObjectId(user_id)
                }
            },

            {
                "$group": {
                    "_id": {
                        "year": {
                            "$year": "$income_date"
                        },
                        "month": {
                            "$month": "$income_date"
                        }
                    },
                    "amount": {
                        "$sum": "$amount"
                    }
                }
            },

            {
                "$sort": {
                    "_id.year": -1,
                    "_id.month": -1
                }
            },

            {
                "$limit": 6
            },

            {
                "$sort": {
                    "_id.year": 1,
                    "_id.month": 1
                }
            }

        ]

        results = list(
            income_collection.aggregate(pipeline)
        )

        months = [
            "Jan", "Feb", "Mar",
            "Apr", "May", "Jun",
            "Jul", "Aug", "Sep",
            "Oct", "Nov", "Dec"
        ]

        data = []

        for item in results:

            data.append({

                "label": f"{months[item['_id']['month'] - 1]} {item['_id']['year']}",

                "month": item["_id"]["month"],

                "year": item["_id"]["year"],

                "amount": item["amount"]

            })

        return data