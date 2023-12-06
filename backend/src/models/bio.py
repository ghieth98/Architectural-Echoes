from src import db


class Bio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    country = db.Column(db.String(40), nullable=False)
    biography = db.Column(db.Text)
    architect_id = db.Column(db.Integer, db.ForeignKey('architect.id'), nullable=False)

