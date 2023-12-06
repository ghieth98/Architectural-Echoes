from src import db


class Architect(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(20), nullable=False)
    projects = db.relationship('Project', backref='architect', lazy=True)
    bio = db.relationship('Bio', backref='architect', lazy=True)

    def to_dict(self):
        return {
            'name': self.name,
            'image': self.image,
            # 'project': self.projects,
            'bio': self.bio
        }
