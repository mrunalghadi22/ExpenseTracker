from flask import Blueprint

from controllers.income_controller import IncomeController

income_bp = Blueprint(
    "income",
    __name__
)

income_bp.route(
    "/income"
)(
    IncomeController.index
)

income_bp.route(
    "/income/create",
    methods=["GET", "POST"]
)(
    IncomeController.create
)

income_bp.route(
    "/income/edit/<income_id>",
    methods=["GET", "POST"]
)(
    IncomeController.edit
)

income_bp.route(
    "/income/delete/<income_id>",
    methods=["POST"]
)(
    IncomeController.delete
)

