from datetime import datetime

from models.category_model import CategoryModel
from utils.category_validator import validate_category_name
from bson import ObjectId


class CategoryService:

    @staticmethod
    def create_category(user_id, data):

        name = data.get("name", "").strip()

        # Validate category name
        valid, message = validate_category_name(name)

        if not valid:
            return False, message

        # Check duplicate category
        category = CategoryModel.get_category_by_name(
            user_id,
            name
        )

        if category:
            return False, "Category already exists."

        category_data = {
            "user_id": ObjectId(user_id),
            "name": name,
            "icon": data.get("icon", "category"),
            "color": data.get("color", "#2563EB"),
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }

        CategoryModel.create_category(category_data)

        return True, "Category created successfully."
    
    @staticmethod
    def get_categories(user_id):
        return CategoryModel.get_categories_by_user(user_id)
    
    @staticmethod
    def update_category(user_id, category_id, data):

        name = data.get("name", "").strip().title()

        valid, message = validate_category_name(name)
    
        if not valid:
            return False, message

        category = CategoryModel.get_category_by_name(
            user_id,
            name
        )
    
        if category and str(category["_id"]) != category_id:
            return False, "Category already exists."

        update_data = {
            "name": name,
            "icon": data.get("icon"),
            "color": data.get("color"),
            "updated_at": datetime.utcnow()
        }

        CategoryModel.update_category(
            category_id,
            update_data
        )

        return True, "Category updated successfully."
    
    @staticmethod
    def delete_category(category_id):

        CategoryModel.delete_category(category_id)

        return True, "Category deleted successfully."