from bson import ObjectId
from database.mongo import db

expense_collection = db["expenses"]


class ExpenseModel:

    @staticmethod
    def create_expense(data):
        return expense_collection.insert_one(data)

    
    @staticmethod
    def get_expense_by_id(user_id, expense_id):

        pipeline = [

            {
                "$match": {
                    "_id": ObjectId(expense_id),
                    "user_id": ObjectId(user_id)
                }
            },

            {
                "$lookup": {
                    "from": "categories",
                    "localField": "category_id",
                    "foreignField": "_id",
                    "as": "category"
                }
            },

            {
                "$unwind": "$category"
            }

        ]

        result = list(
            expense_collection.aggregate(pipeline)
        )

        return result[0] if result else None



  
    @staticmethod
    def get_all_expenses_by_user(user_id):

        pipeline = [

            {    
            "$match": {

                "user_id": ObjectId(user_id)

            }
        },

            {
                "$lookup": {
    
                    "from": "categories",
    
                    "localField": "category_id",
    
                    "foreignField": "_id",
    
                    "as": "category"
    
                }
            },

            {
                "$unwind": "$category"
            },

            {
                "$sort": {

                    "expense_date": -1,
                    "created_at": -1
    
                }
        }

        ]

        return list(
            expense_collection.aggregate(
                pipeline
            )
        )


    @staticmethod
    def update_expense(user_id, expense_id, data):
        return expense_collection.update_one(
            {
                "_id": ObjectId(expense_id),
                "user_id": ObjectId(user_id)
            },
            {
                "$set": data
            }
        )

    @staticmethod
    def delete_expense(user_id, expense_id):
        return expense_collection.delete_one(
            {
                "_id": ObjectId(expense_id),
                "user_id": ObjectId(user_id)
            }
        )

    @staticmethod
    def get_total_expense(user_id):

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

        result = list(
            expense_collection.aggregate(pipeline)
        )

        return result[0]["total"] if result else 0

    @staticmethod
    def get_expense_count(user_id):
        return expense_collection.count_documents(
            {
                "user_id": ObjectId(user_id)
            }
        )
    
    @staticmethod
    def get_recent_expenses(user_id, limit=5):

        pipeline = [

            {
                "$match": {
                    "user_id": ObjectId(user_id)
                }
            },

            {
                "$lookup": {
                    "from": "categories",
                    "localField": "category_id",
                    "foreignField": "_id",
                    "as": "category"
                }
            },

            {
                "$unwind": "$category"
            },

            {
                "$sort": {
                    "expense_date": -1,
                    "created_at": -1
                }
            },

            {
                "$limit": limit
            }

        ]

        return list(
            expense_collection.aggregate(pipeline)
        )

    @staticmethod
    def get_total_expense_this_month(user_id):

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
                    "expense_date": {
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
            expense_collection.aggregate(pipeline)
        )

        return result[0]["total"] if result else 0
    
    @staticmethod
    def get_monthly_expense(user_id):

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
                            "$year": "$expense_date"
                        },
                        "month": {
                            "$month": "$expense_date"
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
            expense_collection.aggregate(pipeline)
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
    
    @staticmethod
    def get_category_wise_expense(user_id):

        pipeline = [

            {
                "$match": {
                    "user_id": ObjectId(user_id)
                }
            },

            {
                "$lookup": {
                    "from": "categories",
                    "localField": "category_id",
                    "foreignField": "_id",
                    "as": "category"
                }
            },

            {
                "$unwind": "$category"
            },

            {
                "$group": {

                    "_id": "$category._id",

                    "category": {
                        "$first": "$category.name"
                    },

                    "color": {
                        "$first": "$category.color"
                    },

                    "amount": {
                        "$sum": "$amount"
                    }

                }
            },

            {
                "$sort": {
                    "amount": -1
                }
            }

        ]

        results = list(
            expense_collection.aggregate(pipeline)
        )

        data = []

        for item in results:

            data.append({

                "category": item["category"],

                "amount": item["amount"],

                "color": item["color"]

            })

        return data