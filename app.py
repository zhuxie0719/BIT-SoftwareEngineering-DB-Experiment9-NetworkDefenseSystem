from flask import Flask
from team1.routes import team1_bp
from team2.routes import team2_bp
from team3.routes import team3_bp

app = Flask(__name__)

app.register_blueprint(team1_bp)
app.register_blueprint(team2_bp)
app.register_blueprint(team3_bp)

@app.route('/')
def home():
    return "你好"

if __name__ == "__main__":
    app.run(debug=True)
