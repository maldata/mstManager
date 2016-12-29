from utilities.event import Event


class BaseView:
    def __init__(self):
        self.addEpisodeEvent = Event()
        self.addMediaSetEvent = Event()
        self.addToCollectionEvent = Event()

    def init_ui(self):
        raise NotImplementedError

    def run_ui(self):
        raise NotImplementedError

