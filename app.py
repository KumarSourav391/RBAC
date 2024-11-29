from flask import Flask
from models import db, User, Role
from flask_jwt_extended import JWTManager
from routes.auth import auth
from routes.role import role_bp
from routes.protected import protected

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rbac.db'
app.config['JWT_SECRET_KEY'] = 'your-secret-key'

db.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(role_bp, url_prefix='/role')
app.register_blueprint(protected, url_prefix='/api')

@app.before_request
def create_tables_once():
    if not hasattr(app, 'tables_created'):
        db.create_all()
        app.tables_created = True


if __name__ == "__main__":
    app.run(debug=True)
