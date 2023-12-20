from src import db
from src.models.bio import Bio
from src.models.project import Project


class Architect(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(20), nullable=False)
    projects = db.relationship('Project', backref='architect', lazy=True)
    bio = db.relationship('Bio', backref='architect', lazy=True)

    def to_dict(self):
        image = self.image.decode('utf-8')
        bio = Bio.query.filter_by(architect_id=self.id).first()
        projects = Project.query.filter_by(architect_id=self.id).all()

        project_list = []  # List to hold project details

        for project in projects:
            # Add details of each project to the project_list
            project_list.append({
                'name': project.name,
                'architect_id': project.architect_id
            })

        return {
            'id': self.id,
            'name': self.name,  # Assuming self.name exists in the Architect model
            'image': image,
            'bio': {
                'age': bio.age,
                'country': bio.country,
                'biography': bio.biography,
                'architect_id': bio.architect_id
            },
            'projects': project_list  # Include the list of project details
        }
