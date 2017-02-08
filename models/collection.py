import models.modelBase
import sqlalchemy


class Video(models.modelBase.Base):
    __tablename__='video_collection'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    episode_id = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey('episodes.id'),
                                   nullable=False)
    media_set_id = sqlalchemy.Column(sqlalchemy.Integer,
                                     sqlalchemy.ForeignKey('media_sets.id'),
                                     nullable=False)

    episodes = sqlalchemy.orm.relationship('Episode',
                                           back_populates='videos')
    media_sets = sqlalchemy.orm.relationship('MediaSet',
                                             back_populates='videos')
