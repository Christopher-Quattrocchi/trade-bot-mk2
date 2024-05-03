from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from auth.auth_module import create_auth_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['JWT_SECRET_KEY'] = 'your-secret-key'

db = SQLAlchemy(app)
jwt = JWTManager(app)

# Create and register the auth blueprint
auth_bp = create_auth_blueprint(db)
app.register_blueprint(auth_bp)

from user.user import user_bp
app.register_blueprint(user_bp)

from dex.dex import dex_bp
app.register_blueprint(dex_bp)

@app.route('/')
def home():
    return 'Welcome to the Arbitrage Bot!'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

# from flask import Flask
# from flask_jwt_extended import JWTManager
# from flask_sqlalchemy import SQLAlchemy
# from auth.auth import auth_bp
# from user.user import user_bp
# from models import db
# from dex.dex import dex_bp

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # Update with your database URI
# app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # Update with your secret key

# jwt = JWTManager(app)
# db.init_app(app)

# app.register_blueprint(auth_bp)
# app.register_blueprint(user_bp)
# app.register_blueprint(dex_bp)

# @app.route('/')
# def home():
#     return 'Welcome to the Arbitrage Bot!'

# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)