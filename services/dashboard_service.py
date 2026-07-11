from models.income_model import IncomeModel
from models.expense_model import ExpenseModel


class DashboardService:

    @staticmethod
    def get_dashboard_data(user_id):

        total_income = IncomeModel.get_total_income(
            user_id
        )

        total_expense = ExpenseModel.get_total_expense(
            user_id
        )

        balance = total_income - total_expense

        income_count = IncomeModel.get_income_count(
            user_id
        )

        expense_count = ExpenseModel.get_expense_count(
            user_id
        )

        monthly_income = IncomeModel.get_total_income_this_month(
            user_id
        )

        monthly_expense = ExpenseModel.get_total_expense_this_month(
            user_id
        )

        monthly_income_chart = IncomeModel.get_monthly_income(
            user_id
        )

        monthly_expense_chart = ExpenseModel.get_monthly_expense(
            user_id
        )

        category_expense_chart = ExpenseModel.get_category_wise_expense(
            user_id
        )

        monthly_balance = monthly_income - monthly_expense
        total_savings = balance

        if monthly_income > 0:

            monthly_saving_rate = round(
                (monthly_balance / monthly_income) * 100,
                1
            )

        else:
          monthly_saving_rate = 0
        

        average_expense = (
            round(total_expense / expense_count, 2)
            if expense_count > 0
            else 0
        )

        average_income = (
            round(total_income / income_count, 2)
            if income_count > 0
            else 0
        )

        expense_ratio = (
            round((total_expense / total_income) * 100, 1)
            if total_income > 0
            else 0
        )

        recent_income = IncomeModel.get_recent_income(
            user_id,
            limit=5
        )

        recent_expenses = ExpenseModel.get_recent_expenses(
            user_id,
            limit=5
        )

        

        transactions = []

        for income in recent_income:

            transactions.append({

                "_id": str(income["_id"]),

                "type": "income",

                "title": income["title"],

                "category": "Income",

                "amount": income["amount"],

                "date": income["income_date"],

                "description": income.get("description", ""),

                "icon": "payments",

                "color": "#10B981"

            })

        for expense in recent_expenses:

            transactions.append({

                "_id": str(expense["_id"]),

                "type": "expense",

                "title": expense["title"],

                "category": expense["category"]["name"],

                "amount": expense["amount"],

                "date": expense["expense_date"],

                "description": expense.get("description", ""),

                "icon": expense["category"]["icon"],

                "color": expense["category"]["color"]

            })

        transactions.sort(
        key=lambda transaction: (
            transaction["date"],
            transaction["_id"]
        ),
        reverse=True
    )

        transactions = transactions[:5]

        return {

            "summary": {

                "balance": balance,

                "income": total_income,

                "expense": total_expense,

                "savings": total_savings

            },

            "monthly": {

                "income": monthly_income,

                "expense": monthly_expense,

                "balance": monthly_balance,

                "saving_rate": monthly_saving_rate

            },

            "stats": {

                "income_count": income_count,

                "expense_count": expense_count,

                "average_income": average_income,

                "average_expense": average_expense,

                "expense_ratio": expense_ratio

            },

            "recent_transactions": transactions,
            "monthly_income_chart": monthly_income_chart,

            "monthly_expense_chart": monthly_expense_chart,

            "category_expense_chart": category_expense_chart,

        }