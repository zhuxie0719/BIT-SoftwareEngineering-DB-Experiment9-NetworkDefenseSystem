from flask import Blueprint, render_template

team1_bp = Blueprint('team1', __name__)

@team1_bp.route('/page1')
def page1():
    return render_template('page1.html')

@team1_bp.route('/page2')
def page2():
    return render_template('page2.html')
