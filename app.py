from flask import Flask
from config import Config

from routes.home_routes import home_bp
from routes.auth_routes import auth_bp
from routes.dashboard_routes import dashboard_bp

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(home_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)



if __name__ == "__main__":
    app.run(debug=True)