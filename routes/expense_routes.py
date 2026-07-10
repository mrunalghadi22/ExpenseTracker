from flask import Blueprint

from controllers.expense_controller import ExpenseController

expense_bp = Blueprint(
    "expense",
    __name__
)

expense_bp.route(
    "/expense"
)(
    ExpenseController.index
)

expense_bp.route(
    "/expense/create",
    methods=["GET", "POST"]
)(
    ExpenseController.create
)

expense_bp.route(
    "/expense/edit/<expense_id>",
    methods=["GET", "POST"]
)(
    ExpenseController.edit
)

expense_bp.route(
    "/expense/delete/<expense_id>",
    methods=["POST"]
)(
    ExpenseController.delete
)

