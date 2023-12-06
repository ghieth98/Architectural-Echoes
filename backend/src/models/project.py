from src import db


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    created_at = db.Column(db.Date(), nullable=False)
    city = db.Column(db.String(20), nullable=True)
    country = db.Column(db.String(30), nullable=False)
    architect_id = db.Column(db.Integer, db.ForeignKey('architect.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at,
            'city': self.city,
            'country': self.country,
            'architect': self.architect_id
        }


