from flask import Blueprint, request

from controllers.auth_controller import (
    register_page,
    register_user,
    login_page,
    login_user,
    logout_user
)

auth_bp = Blueprint(
    "auth",
    __name__
)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        return register_user()

    return register_page()


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        return login_user()

    return login_page()


@auth_bp.route("/logout")
def logout():

    return logout_user()