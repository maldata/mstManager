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

