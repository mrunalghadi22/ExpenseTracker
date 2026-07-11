from datetime import datetime

from werkzeug.security import (
    check_password_hash,
    generate_password_hash
)

from models.user_model import UserModel
from models.income_model import IncomeModel
from models.expense_model import ExpenseModel

from utils.validators import validate_name, validate_password


class ProfileService:

    @staticmethod
    def get_profile(user_id):

        user = UserModel.get_user_by_id(user_id)

        if not user:
            return None

        total_income = IncomeModel.get_total_income(user_id)

        total_expense = ExpenseModel.get_total_expense(user_id)

        balance = total_income - total_expense

        transaction_count = (
            IncomeModel.get_income_count(user_id) +
            ExpenseModel.get_expense_count(user_id)
        )

        return {

            "user": user,

            "stats": {

                "total_income": total_income,

                "total_expense": total_expense,

                "balance": balance,

                "transactions": transaction_count

            }

        }

    @staticmethod
    def update_profile(user_id, form):

        full_name = form.get("full_name", "").strip()

        valid, message = validate_name(full_name)

        if not valid:
            return False, message
        
        update_data = {

            "full_name": full_name,

            "updated_at": datetime.utcnow()

        }

        UserModel.update_user(

            user_id,

            update_data

        )

        return True, "Profile updated successfully."

    @staticmethod
    def change_password(user_id, form):

        current_password = form.get("current_password", "")

        new_password = form.get("new_password", "")

        confirm_password = form.get("confirm_password", "")

        user = UserModel.get_user_by_id(user_id)

        if not check_password_hash(

            user["password"],

            current_password

        ):

            return False, "Current password is incorrect."

        valid, message = validate_password(new_password)

        if not valid:
            return False, message

        if new_password != confirm_password:

            return False, "Passwords do not match."

        hashed_password = generate_password_hash(

            new_password

        )

        UserModel.update_password(

            user_id,

            hashed_password

        )

        return True, "Password updated successfully."