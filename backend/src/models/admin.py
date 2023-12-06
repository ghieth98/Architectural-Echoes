from src import db


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(70), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Admin('{self.email}')"
