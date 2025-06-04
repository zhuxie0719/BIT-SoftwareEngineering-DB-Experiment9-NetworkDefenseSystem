from flask import Blueprint, render_template

team1_bp = Blueprint('team1', __name__)

@team1_bp.route('/introInstitute')
def page1():
    return render_template('team1/introInstitute.html')

