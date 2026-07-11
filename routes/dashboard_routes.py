from flask import Blueprint

from controllers.dashboard_controller import DashboardController


dashboard_bp = Blueprint(
    "dashboard",
    __name__
)


dashboard_bp.route(
    "/dashboard"
)(
    DashboardController.dashboard_page
)