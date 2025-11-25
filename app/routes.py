from flask import Blueprint, render_template
from .decorators import login_required, role_required
from .models import Salary
bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    return render_template("home.html")

@bp.route("/dashboard")
@login_required
@role_required("user")
def dashboard():
    salary = Salary.query.all()
    return render_template("dashboard.html", salary=salary)

@bp.route("/admin")
@login_required
@role_required("admin")
def admin_area():
    salary = Salary.query.all()
    return render_template('admin/admin.html', salary=salary)