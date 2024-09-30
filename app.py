from flask import Flask
from sqlalchemy import text
from blue_prints.mission import mission_bp
from blue_prints.analysis import analysis_bp
from db import db
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/wwii_missions'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(mission_bp)
app.register_blueprint(analysis_bp)

with app.app_context():
    try:
        db.session.execute(text('SELECT 1'))
        print("Connection successful!")
    except Exception as e:
        print("Connection failed:", str(e))

if __name__ == '__main__':
    app.run(debug=True)