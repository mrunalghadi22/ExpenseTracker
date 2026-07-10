from datetime import datetime
from bson import ObjectId

from models.expense_model import ExpenseModel
# from models.category_model import CategoryModel
from services.category_service import CategoryService


class ExpenseService:

    @staticmethod
    def _validate_expense(user_id, form_data):

        title = form_data.get("title", "").strip()
        amount = form_data.get("amount", "").strip()
        category_id = form_data.get("category_id", "").strip()
        description = form_data.get("description", "").strip()
        expense_date = form_data.get("expense_date")

        if not title:
            return False, "Expense title is required.", None

        if not amount:
            return False, "Amount is required.", None

        try:

            amount = float(amount)

            if amount <= 0:
                return False, "Amount must be greater than 0.", None

        except ValueError:

            return False, "Invalid amount.", None

        if not category_id:
            return False, "Please select a category.", None

        category = CategoryService.get_category(
             user_id,
            category_id
        )    

        if not category:
            return False, "Invalid category selected.", None

        if not expense_date:
            return False, "Expense date is required.", None

        data = {

            "category_id": ObjectId(category_id),

            "title": title,

            "amount": amount,

            "description": description,

            "expense_date": datetime.strptime(
                expense_date,
                "%Y-%m-%d"
            )

        }

        return True, "", data

    @staticmethod
    def create_expense(user_id, form_data):

        valid, message, data = ExpenseService._validate_expense(
            user_id,
            form_data
        )

        if not valid:
            return False, message

        data["user_id"] = ObjectId(user_id)
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()

        ExpenseModel.create_expense(data)

        return True, "Expense added successfully."

    @staticmethod
    def update_expense(user_id, expense_id, form_data):

        valid, message, data = ExpenseService._validate_expense(
            user_id,
            form_data
        )

        if not valid:
            return False, message

        data["updated_at"] = datetime.utcnow()

        ExpenseModel.update_expense(
            user_id,
            expense_id,
            data
        )

        return True, "Expense updated successfully."

    @staticmethod
    def delete_expense(user_id, expense_id):

        ExpenseModel.delete_expense(
            user_id,
            expense_id
        )

        return True, "Expense deleted successfully."

    @staticmethod
    def get_all_expenses(user_id):

        return ExpenseModel.get_all_expenses_by_user(
            user_id
        )

    @staticmethod
    def get_expense(user_id, expense_id):

        return ExpenseModel.get_expense_by_id(
            user_id,
            expense_id
        )

    @staticmethod
    def get_total_expense(user_id):

        return ExpenseModel.get_total_expense(
            user_id
        )
    

    @staticmethod
    def get_categories(user_id):

        return CategoryService.get_all_categories(
            user_id
        )



