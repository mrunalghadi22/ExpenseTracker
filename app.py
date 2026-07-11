from flask import Flask,session
from config import Config

from routes.home_routes import home_bp
from routes.auth_routes import auth_bp
from routes.category_routes import category_bp
from routes.income_routes import income_bp
from routes.expense_routes import expense_bp
from models.user_model import UserModel
from routes.dashboard_routes import dashboard_bp
from routes.profile_routes import profile_bp

app = Flask(__name__)
app.config.from_object(Config)

@app.context_processor
def inject_user():

    user = None

    if "user_id" in session:
        user = UserModel.get_user_by_id(session["user_id"])

    return {
        "current_user": user
    }

app.register_blueprint(home_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(category_bp)
app.register_blueprint(income_bp)
app.register_blueprint(expense_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(profile_bp)



if __name__ == "__main__":
    app.run(debug=True)