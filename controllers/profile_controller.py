from flask import (
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session
)

from services.profile_service import ProfileService


class ProfileController:

    @staticmethod
    def index():

        user_id = session.get("user_id")

        profile = ProfileService.get_profile(user_id)

        return render_template(
            "profile/index.html",
            profile=profile
        )

    @staticmethod
    def update_profile():

        user_id = session.get("user_id")

        success, message = ProfileService.update_profile(
            user_id,
            request.form
        )

        flash(
            message,
            "success" if success else "error"
        )

        return redirect(
            url_for("profile.index")
        )

    @staticmethod
    def change_password():

        user_id = session.get("user_id")

        success, message = ProfileService.change_password(
            user_id,
            request.form
        )

        flash(
            message,
            "success" if success else "error"
        )

        return redirect(
            url_for("profile.index")
        )