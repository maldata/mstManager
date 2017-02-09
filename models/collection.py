import models.modelBase
import sqlalchemy


class Media(models.modelBase.Base):
    __tablename__='media_collection'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    episode_id = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey('episodes.id'),
                                   nullable=False)
    media_set_id = sqlalchemy.Column(sqlalchemy.Integer,
                                     sqlalchemy.ForeignKey('media_sets.id'),
                                     nullable=False)

    episodes = sqlalchemy.orm.relationship('Episode',
                                           back_populates='media')
    media_sets = sqlalchemy.orm.relationship('MediaSet',
                                             back_populates='media')
