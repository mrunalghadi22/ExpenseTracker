from flask import render_template, session

from services.dashboard_service import DashboardService


class DashboardController:

    @staticmethod
    def dashboard_page():

        user_id = session["user_id"]

        dashboard = DashboardService.get_dashboard_data(
            user_id
        )

        return render_template(
            "dashboard/index.html",
            dashboard=dashboard
        )