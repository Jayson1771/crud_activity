from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import db, Salary

app = Blueprint("cruds", __name__, url_prefix="/cruds")


@app.route('/admin')
def home():
    salary = Salary.query.all()
    return render_template('cruds.home', salary=salary)

@app.route('/add', methods=['GET', 'POST'])
def add_salary():
    if request.method == 'POST':
        name = request.form['name']
        MembershipType = request.form['MembershipType']
        Rate = request.form['Rate']
        HoursWork = request.form['HoursWork']
        NetPay = float(Rate) * float(HoursWork)
        deductions = float(NetPay) * (0.10)
        takehome = float(NetPay) - float(deductions)
        salary = Salary.query.all()
        if not name.strip():
            flash("Please fill correctly")
        elif float(Rate) <= 0:
            flash("Please fill correctly")
        elif int(HoursWork) <= 0:
            flash("Please fill correctly")
        for salay in salary:
            if name == salay.name:
                flash("Error")
                break
        else:
            new_salary = Salary(name=name, MembershipType=MembershipType, Rate=Rate, HoursWork=HoursWork, NetPay=NetPay, deductions=takehome)
            db.session.add(new_salary)
            db.session.commit()
            flash('Salary added successfully!')
            return redirect(url_for('cruds.home'))
    return render_template('admin/add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_salary(id):
    salary = Salary.query.get_or_404(id)
    if request.method == 'POST':
        salary.name = request.form['name']
        salary.MembershipType = request.form['MembershipType']
        salary.Rate = request.form['Rate']
        salary.HoursWork = request.form['HoursWork']
        salary.NetPay = float(salary.Rate) * float(salary.HoursWork)
        takehome = float(salary.NetPay) * (0.10)
        salary.deductions = float(salary.NetPay) - float(takehome)
        if salary.name == " ": 
            flash("Please fill correctly")
        elif float(salary.Rate) <= 0:
            flash("Please fill correctly")
        elif int(salary.HoursWork) <= 0:
            flash("Please fill correctly")
        else:
            db.session.commit()
            flash('Salary updated successfully!')
        return redirect(url_for('cruds.home'))
    return render_template('edit.html', salary=salary)

@app.route('/delete/<int:id>')
def delete_salary(id):
    salary = Salary.query.get_or_404(id)
    db.session.delete(salary)
    db.session.commit()
    flash('Salary deleted successfully!')
    return redirect(url_for('cruds.home'))