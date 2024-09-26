from flask import Flask, Blueprints, request

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/wwii_mission'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'MOCK_SECRET_123456'

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)