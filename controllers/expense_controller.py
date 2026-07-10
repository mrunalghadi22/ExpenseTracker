from flask import render_template, request, redirect, url_for, flash, session

from services.expense_service import ExpenseService


class ExpenseController:

    @staticmethod
    def index():

        expenses = ExpenseService.get_all_expenses(
            session["user_id"]
        )

        return render_template(
            "expense/index.html",
            expenses=expenses
        )

    @staticmethod
    def create():

        categories = ExpenseService.get_categories(
            session["user_id"]
        )

        if request.method == "GET":

            return render_template(
                "expense/form.html",
                expense=None,
                categories=categories
            )

        success, message = ExpenseService.create_expense(
            session["user_id"],
            request.form
        )

        flash(
            message,
            "success" if success else "error"
        )

        if success:

            return redirect(
                url_for("expense.index")
            )

        return render_template(
            "expense/form.html",
            expense=None,
            categories=categories
        )

    @staticmethod
    def edit(expense_id):

        expense = ExpenseService.get_expense(
            session["user_id"],
            expense_id
        )

        if not expense:

            flash(
                "Expense not found.",
                "error"
            )

            return redirect(
                url_for("expense.index")
            )

        categories = ExpenseService.get_categories(
            session["user_id"]
        )

        if request.method == "GET":

            return render_template(
                "expense/form.html",
                expense=expense,
                categories=categories
            )

        success, message = ExpenseService.update_expense(
            session["user_id"],
            expense_id,
            request.form
        )

        flash(
            message,
            "success" if success else "error"
        )

        if success:

            return redirect(
                url_for("expense.index")
            )

        expense = ExpenseService.get_expense(
            session["user_id"],
            expense_id
        )

        return render_template(
            "expense/form.html",
            expense=expense,
            categories=categories
        )

    @staticmethod
    def delete(expense_id):

        success, message = ExpenseService.delete_expense(
            session["user_id"],
            expense_id
        )

        flash(
            message,
            "success" if success else "error"
        )

        return redirect(
            url_for("expense.index")
        )

