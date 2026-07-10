
from datetime import datetime
from bson import ObjectId

from models.category_model import CategoryModel
from utils.category_validator import validate_category_name


class CategoryService:

    @staticmethod
    def create_category(user_id, data):

        name = data.get("name", "").strip().title()

        valid, message = validate_category_name(name)

        if not valid:
            return False, message

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
    def get_all_categories(user_id):

        return CategoryModel.get_categories_by_user(
            user_id
        )

    @staticmethod
    def get_category(user_id, category_id):

        return CategoryModel.get_category_by_id(
            user_id,
            category_id
        )

    @staticmethod
    def update_category(user_id, category_id, data):

        existing_category = CategoryService.get_category(
            user_id,
            category_id
        )

        if not existing_category:
            return False, "Category not found."

        name = data.get("name", "").strip().title()

        valid, message = validate_category_name(name)

        if not valid:
            return False, message

        duplicate = CategoryModel.get_category_by_name(
            user_id,
            name
        )

        if duplicate and str(duplicate["_id"]) != category_id:
            return False, "Category already exists."

        update_data = {
            "name": name,
            "icon": data.get("icon"),
            "color": data.get("color"),
            "updated_at": datetime.utcnow()
        }

        CategoryModel.update_category(
            user_id,
            category_id,
            update_data
        )

        return True, "Category updated successfully."

    @staticmethod
    def delete_category(user_id, category_id):

        category = CategoryService.get_category(
            user_id,
            category_id
        )

        if not category:
            return False, "Category not found."

        CategoryModel.delete_category(
            user_id,
            category_id
        )

        return True, "Category deleted successfully."

