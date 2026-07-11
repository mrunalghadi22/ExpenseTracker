from flask import session, redirect, url_for, render_template

def home():
    if session.get("user_id"):
            return redirect(url_for("dashboard.dashboard_page"))

    return render_template("home.html")