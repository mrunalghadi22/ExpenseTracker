from flask import Blueprint

from controllers.category_controller import CategoryController

category_bp = Blueprint(
    "category",
    __name__
)

category_bp.route(
    "/categories",
    methods=["GET"]
)(CategoryController.index)

category_bp.route(
    "/categories/new",
    methods=["GET", "POST"]
)(CategoryController.create)

category_bp.route(
    "/categories/edit/<category_id>",
    methods=["GET", "POST"]
)(CategoryController.edit)

category_bp.route(
    "/categories/delete/<category_id>",
    methods=["POST"]
)(CategoryController.delete)