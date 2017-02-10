import sqlalchemy
import alembic
import alembic.config

from . import models

class DbEngine:
    def __init__(self):
        self._conn = None
        self._session = None

    def initialize(self):
        alembic_args = ['--raiseerr', 'upgrade', 'head']
        alembic.config.main(argv=alembic_args)

        # TODO: relative (to top level) path... asking for trouble.
        c = alembic.config.Config('./alembic.ini')
        url = c.get_main_option('sqlalchemy.url')

        # Connect to the database
        self._conn = sqlalchemy.create_engine(url, connect_args={'check_same_thread': False})

        # Create a configured "Session" class, then instantiate it
        session_factory = sqlalchemy.orm.sessionmaker(bind=self._conn)
        Session = sqlalchemy.orm.scoped_session(session_factory)
        self._session = Session()

    def deinitialize(self):
        self._session.close()
        self._session = None
        self._conn = None

    def add_or_get_season(self, number):
        s = self._session.query(models.Season) \
                         .filter(models.Season.number == number).one_or_none()

        if s is None:
            s = models.Season(number=number)
            self._session.add(s)
            self._session.commit()

        return s

    def get_all_seasons(self):
        return self._session.query(models.Season).all()

    def parse_episode_number(self, number):
        # TODO
        season = 'K'
        episode_number = 7
        return (season, episode_number)

    def build_episode_number(self, season, episode_number):
        # TODO
        return 'K07'
    
    def add_episode(self, number, name):
        """
        :param number: the episode number, e.g., 'K07'
        :type number: str
        :param name: the episode name
        :type name: str, e.g., 'Gamera vs. Zigra'
        """
        # TODO
        # parse the episode number
        # check if the season exists
        # if not, add it
        e = models.Episode(number=number, name=name)
