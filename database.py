from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()

# User Model
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)

    role = db.relationship('Role', back_populates='users')

    def __repr__(self):
        return f"<User(username={self.username}, role={self.role.name})>"

# Role Model
class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    permissions = db.Column(db.PickleType, nullable=False)  # Store permissions as a list

    users = db.relationship('User', back_populates='role', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Role(name={self.name}, permissions={self.permissions})>"

# Utility function to initialize the database
def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
