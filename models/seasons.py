import models.modelBase
import models.episodes
import sqlalchemy
import sqlalchemy.orm


class Season(models.modelBase.Base):
    # Here we define our class variables. These are shared among all instances of this class.
    # They can be accessed as (for example) Address.id from inside the class or outside the class.
    __tablename__ = 'seasons'

    # Among our class variables are the descriptions of each column of the table, as follows
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    seasonNumber = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    # A season contains multiple episodes. Each record in the episodes table will have a foreign key
    # to a season, so here we'll have a collection of episodes in this season.
    episodes = sqlalchemy.orm.relationship('Episode',
                                           back_populates='season')

    def __repr__(self):
        return "<Season(seasonNum='%s')>" % self.seasonNumber
