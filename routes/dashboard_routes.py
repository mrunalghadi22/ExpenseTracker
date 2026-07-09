from flask import Blueprint
from controllers.dashboard_controller import dashboard
from middleware.auth import login_required

dashboard_bp = Blueprint(
    "dashboard",
    __name__
)


@dashboard_bp.route("/dashboard")
@login_required
def dashboard_page():
    return dashboard()