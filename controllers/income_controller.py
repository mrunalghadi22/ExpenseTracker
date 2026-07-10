from flask import render_template, request, redirect, url_for, flash, session

from services.income_service import IncomeService


class IncomeController:

    @staticmethod
    def index():

        incomes = IncomeService.get_all_income(
            session["user_id"]
        )

        return render_template(
            "income/index.html",
            incomes=incomes
        )

    @staticmethod
    def create():

        if request.method == "GET":

            return render_template(
                "income/form.html",
                income=None
            )

        success, message = IncomeService.create_income(
            session["user_id"],
            request.form
        )

        flash(
            message,
            "success" if success else "error"
        )

        if success:

            return redirect(
                url_for("income.index")
            )

        return render_template(
            "income/form.html",
            income=None
        )

    @staticmethod
    def edit(income_id):

        income = IncomeService.get_income(
            session["user_id"],
            income_id
        )

        if not income:

            flash(
                "Income not found.",
                "error"
            )

            return redirect(
                url_for("income.index")
            )

        if request.method == "GET":

            return render_template(
                "income/form.html",
                income=income
            )

        success, message = IncomeService.update_income(
            session["user_id"],
            income_id,
            request.form
        )

        flash(
            message,
            "success" if success else "error"
        )

        if success:

            return redirect(
                url_for("income.index")
            )

        return render_template(
            "income/form.html",
            income=income
        )

    @staticmethod
    def delete(income_id):

        success, message = IncomeService.delete_income(
            session["user_id"],
            income_id
        )

        flash(
            message,
            "success" if success else "error"
        )

        return redirect(
            url_for("income.index")
        )

