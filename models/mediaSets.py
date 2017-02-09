import models.modelBase
import sqlalchemy
import sqlalchemy.orm


class MediaSet(models.modelBase.Base):
    __tablename__='media_sets'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    episodes = sqlalchemy.orm.relationship('Episode',
                                           back_populates='media_sets')
    media = sqlalchemy.orm.relationship('Media',
                                         back_populates='media_sets')
    
