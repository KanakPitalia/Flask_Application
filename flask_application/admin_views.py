from flask_application import app
from flask import render_template
@app.route("/admin/dashboard")
def dashboard():
    return render_template('/admin/dashboard.html')
@app.route("/admin/profile")
def _profile():
    return render_template('/admin/profile.html')