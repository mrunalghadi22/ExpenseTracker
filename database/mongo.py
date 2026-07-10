from pymongo import MongoClient
from config import Config

client = MongoClient(Config.MONGO_URI)

db = client[Config.DATABASE_NAME]

# Collections
user_collection = db["users"]
category_collection = db["categories"]
expense_collection = db["expenses"]
income_collection = db["income"]