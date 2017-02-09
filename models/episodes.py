import models.modelBase
import models.seasons
import sqlalchemy
import sqlalchemy.orm


class Episode(models.modelBase.Base):
    # Here we define our class variables. These are shared among all instances of this class.
    # They can be accessed as (for example) Address.id from inside the class or outside the class.
    __tablename__ = 'episodes'

    # Among our class variables are the descriptions of each column of the table, as follows
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    number = sqlalchemy.Column(sqlalchemy.Integer, unique=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    season_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('seasons.id'))

    season = sqlalchemy.orm.relationship('Season',
                                         back_populates='episodes')
    media_sets = sqlalchemy.orm.relationship('MediaSet',
                                             back_populates='episodes')
    media = sqlalchemy.orm.relationship('Media',
                                         back_populates='episodes')
    
    def __repr__(self):
        return "<Episode(episodeNumber='%s')>" % (self.season.seasonNumber + str(self.episodeNumber))
