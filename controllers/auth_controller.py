from flask import (
    render_template,
    request,
    redirect,
    flash,
    url_for,
    session
)

from services.auth_service import AuthService


def register_page():
    return render_template("auth/register.html")


def register_user():

    success, message = AuthService.register_user(request.form)

    if success:
        flash(message, "success")
        return redirect(url_for("auth.login"))

    flash(message, "error")
    return redirect(url_for("auth.register"))


def login_page():
    return render_template("auth/login.html")


def login_user():

    success, message, user = AuthService.login_user(request.form)

    if not success:
        flash(message, "error")
        return redirect(url_for("auth.login"))

    session["user_id"] = str(user["_id"])
    # session["user_name"] = user["full_name"]
    # session["user_email"] = user["email"]

    flash(message, "success")

    return redirect(url_for("dashboard.dashboard_page"))

def logout_user():

    session.clear()

    flash("Logged out successfully.", "success")

    return redirect(url_for("auth.login"))