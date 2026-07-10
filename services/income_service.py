
from datetime import datetime
from bson import ObjectId

from models.income_model import IncomeModel


class IncomeService:

    @staticmethod
    def _validate_income(form_data):

        title = form_data.get("title", "").strip()
        amount = form_data.get("amount", "").strip()
        description = form_data.get("description", "").strip()
        income_date = form_data.get("income_date")

        if not title:
            return False, "Income title is required.", None

        if not amount:
            return False, "Amount is required.", None

        try:
            amount = float(amount)

            if amount <= 0:
                return False, "Amount must be greater than 0.", None

        except ValueError:
            return False, "Invalid amount.", None

        if not income_date:
            return False, "Income date is required.", None

        data = {
            "title": title,
            "amount": amount,
            "description": description,
            "income_date": datetime.strptime(
                income_date,
                "%Y-%m-%d"
            )
        }

        return True, "", data

    @staticmethod
    def create_income(user_id, form_data):

        valid, message, data = IncomeService._validate_income(form_data)

        if not valid:
            return False, message

        data["user_id"] = ObjectId(user_id)
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()

        IncomeModel.create_income(data)

        return True, "Income added successfully."

    @staticmethod
    def update_income(user_id, income_id, form_data):

        valid, message, data = IncomeService._validate_income(form_data)

        if not valid:
            return False, message

        data["updated_at"] = datetime.utcnow()

        IncomeModel.update_income(
            user_id,
            income_id,
            data
        )

        return True, "Income updated successfully."

    @staticmethod
    def delete_income(user_id, income_id):

        IncomeModel.delete_income(
            user_id,
            income_id
        )

        return True, "Income deleted successfully."

    @staticmethod
    def get_all_income(user_id):

        return IncomeModel.get_all_income_by_user(user_id)

    @staticmethod
    def get_income(user_id, income_id):

        return IncomeModel.get_income_by_id(
            user_id,
            income_id
        )

    @staticmethod
    def get_total_income(user_id):

        return IncomeModel.get_total_income(user_id)

