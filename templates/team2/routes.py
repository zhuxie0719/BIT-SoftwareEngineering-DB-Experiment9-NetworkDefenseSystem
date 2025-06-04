from flask import Blueprint, render_template

team2_bp = Blueprint('team2', __name__)

@team2_bp.route('/page3')
def page3():
    return render_template('page3.html')

@team2_bp.route('/page4')
def page4():
    return render_template('page4.html')
