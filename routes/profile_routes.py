from flask import Blueprint

from controllers.profile_controller import ProfileController

profile_bp = Blueprint(
    "profile",
    __name__,
    url_prefix="/profile"
)


@profile_bp.route("/")
def index():
    return ProfileController.index()


@profile_bp.route("/update", methods=["POST"])
def update_profile():
    return ProfileController.update_profile()


@profile_bp.route("/change-password", methods=["POST"])
def change_password():
    return ProfileController.change_password()