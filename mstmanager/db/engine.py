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
                         .filter(models.Season.number == number) \
                         .one_or_none()

        if s is None:
            s = models.Season(number=number)
            self._session.add(s)
            self._session.commit()

        return s

    def get_all_seasons(self):
        return self._session.query(models.Season).all()

    def get_all_season_numbers(self):
        ss = self.get_all_seasons()
        return [s.number for s in ss]

    def get_season(self, number):
        return self._session.query(models.Season) \
                            .filter(models.Season.number == number) \
                            .one_or_none()
        
    def parse_episode_number(self, number):
        """
        Break up an episode number (string) into the season identifier and
        the episode number (int)
        :param number: the full episode number to parse
        :type number: str
        """
        try:
            season = number[:-2]
            ep = number[-2:]
            episode_number = int(ep)
            return (season, episode_number)
        except (ValueError, TypeError) as e:
            logger.Error('Failed to parse {0} as an episode number.'.format(number))
            return None

    def build_episode_number(self, season, episode_number):
        """
        Put together the season string and an episode number (integer)
        into the full episode id
        :param season: the season id string
        :type season: str
        :param episode_number: the number of the episode within the season
        :type episode_number: int
        """
        episode_string = '{:02d}'.format(episode_number)
        return season + episode_string
    
    def add_episode(self, number, name):
        """
        :param number: the episode number, e.g., 'K07'
        :type number: str
        :param name: the episode name
        :type name: str, e.g., 'Gamera vs. Zigra'
        """
        (season, episode) = self.parse_episode_number(number)
        s = self.add_or_get_season(season)
        
        e = models.Episode(number=episode, name=name)
        e.season = s
        
        self._session.add(e)
        self._session.commit()

        return e

    def add_media_set(self, name):
        m = models.MediaSet(name=name)
        self._session.add(m)
        self._session.commit()

        return m

    def add_to_collection(self, episode, media_set):
        m = models.Media()
        m.episode = episode
        m.media_set = media_set
        self._session.add(m)
        self._session.commit()

    def get_episode_list_by_season(self, season_code):
        s = self.get_season(season_code)
        if s:
            return s.episodes
        
    def get_all_media_sets(self):
        return self._session.query(models.MediaSet) \
                            .order_by(models.MediaSet.id).all()

    def get_episode_by_code(self, code):
        return self._session.query(models.Episode) \
                            .filter(models.Episode.episode_code == code) \
                            .one_or_none()
        
