
from flask import render_template, request, redirect, url_for, flash, session

from services.category_service import CategoryService


class CategoryController:

    @staticmethod
    def index():

        user_id = session["user_id"]

        categories = CategoryService.get_all_categories(
            user_id
        )

        return render_template(
            "category/index.html",
            categories=categories
        )

    @staticmethod
    def create():

        user_id = session["user_id"]

        if request.method == "GET":

            return render_template(
                "category/form.html",
                category=None
            )

        success, message = CategoryService.create_category(
            user_id,
            request.form
        )

        flash(
            message,
            "success" if success else "error"
        )

        if success:

            return redirect(
                url_for("category.index")
            )

        return render_template(
            "category/form.html",
            category=None
        )

    @staticmethod
    def edit(category_id):

        user_id = session["user_id"]

        category = CategoryService.get_category(
            user_id,
            category_id
        )

        if not category:

            flash(
                "Category not found.",
                "error"
            )

            return redirect(
                url_for("category.index")
            )

        if request.method == "GET":

            return render_template(
                "category/form.html",
                category=category
            )

        success, message = CategoryService.update_category(
            user_id,
            category_id,
            request.form
        )

        flash(
            message,
            "success" if success else "error"
        )

        if success:

            return redirect(
                url_for("category.index")
            )

        category = CategoryService.get_category(
            user_id,
            category_id
        )

        return render_template(
            "category/form.html",
            category=category
        )

    @staticmethod
    def delete(category_id):

        user_id = session["user_id"]

        success, message = CategoryService.delete_category(
            user_id,
            category_id
        )

        flash(
            message,
            "success" if success else "error"
        )

        return redirect(
            url_for("category.index")
        )

