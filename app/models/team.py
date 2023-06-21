from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.orm import validates

class Team(db.Model):
    __tablename__ = 'teams'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), nullable=False)
    league = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(100), nullable=False)


## Relationships ##
    # Many-to-One with Odds History
    # One team can have many odds_Histories
    odds_histories = db.relationship('Odds_History', back_populates='team')


    def to_dict(self):
        return {
            'id': self.id,
            'code': self.code,
            'league': self.league,
            'name': self.name,
        }
