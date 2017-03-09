import sqlalchemy
import sqlalchemy.orm
import sqlalchemy.ext.declarative

from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method


SAModelBase = sqlalchemy.ext.declarative.declarative_base()


class Season(SAModelBase):
    # Here we define our class variables. These are shared among all
    # instances of this class. They can be accessed as (for example)
    # Season.id from inside the class or outside the class.
    __tablename__ = 'seasons'

    # Among our class variables are the descriptions of each column
    # of the table, as follows
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    number = sqlalchemy.Column(sqlalchemy.String(4), nullable=False)

    # A season contains multiple episodes. Each record in the episodes
    # table will have a foreign key to a season, so here we'll have a
    # collection of episodes in this season.
    episodes = sqlalchemy.orm.relationship('Episode',
                                           back_populates='season')

    def __repr__(self):
        return "<Season(seasonNum='%s')>" % self.number


class Episode(SAModelBase):
    __tablename__ = 'episodes'

    # Columns
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    number = sqlalchemy.Column(sqlalchemy.Integer, unique=False, nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    @hybrid_property
    def episode_code(self):
        s = self.season.number
        e = '{0:02d}'.format(self.number)
        return s + e

    @episode_code.expression
    def episode_code(cls):
        return sqlalchemy.sql.select([sqlalchemy.func.printf('%s', Season.number) +
                                      sqlalchemy.func.printf('%02d', cls.number)]). \
                              where(Season.id == cls.season_id).as_scalar()
    
    # Foreign key columns
    season_id = sqlalchemy.Column(sqlalchemy.Integer,
                                  sqlalchemy.ForeignKey('seasons.id'),
                                  nullable=False)

    # Foreign key relationships
    season = sqlalchemy.orm.relationship('Season',
                                         back_populates='episodes')
    media_sets = sqlalchemy.orm.relationship('MediaSet',
                                             secondary='media_collection',
                                             back_populates='episodes')
    media = sqlalchemy.orm.relationship('Media',
                                         back_populates='episodes')
    
    def __repr__(self):
        return "<Episode(episodeNumber='%s')>".format(self.episode_code)


class MediaSet(SAModelBase):
    __tablename__='media_sets'

    # Columns
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    # Foreign key relationships
    episodes = sqlalchemy.orm.relationship('Episode',
                                           secondary='media_collection',
                                           back_populates='media_sets')
    media = sqlalchemy.orm.relationship('Media',
                                         back_populates='media_sets')
    
class Media(SAModelBase):
    __tablename__='media_collection'

    # Columns
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)

    # Foreign key columns
    episode_id = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey('episodes.id'),
                                   nullable=False)
    media_set_id = sqlalchemy.Column(sqlalchemy.Integer,
                                     sqlalchemy.ForeignKey('media_sets.id'),
                                     nullable=False)

    # Foreign key relationships
    episodes = sqlalchemy.orm.relationship('Episode',
                                           back_populates='media')
    media_sets = sqlalchemy.orm.relationship('MediaSet',
                                             back_populates='media')
