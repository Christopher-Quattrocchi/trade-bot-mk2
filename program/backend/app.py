from flask import Flask
from flask_jwt_extended import JWTManager
from auth.auth import auth_bp
from user.user import user_bp
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # Update with your database URI
app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # Update with your secret key

jwt = JWTManager(app)
db.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)

@app.route('/')
def home():
    return 'Welcome to the Arbitrage Bot!'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)