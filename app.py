from flask import Flask
from team1.routes import team1_bp
from team2.routes import team2_bp
from team3.routes import team3_bp

app = Flask(__name__)

app.register_blueprint(team1_bp, url_prefix='/team1')
app.register_blueprint(team2_bp, url_prefix='/team2')
app.register_blueprint(team3_bp, url_prefix='/team3')


if __name__ == "__main__":
    app.run(debug=True)
