from utilities.event import Event


class BaseView:
    def __init__(self):
        self.addEpisodeEvent = Event()
        self.addMediaSetEvent = Event()
        self.addToCollectionEvent = Event()
        self.receivedEpisode = Event()

    def init_ui(self):
        raise NotImplementedError

    def run_ui(self):
        raise NotImplementedError

    def show_dialog_get_episode(self):
        raise NotImplementedError

    def show_dialog_get_media_set(self):
        raise NotImplementedError

    def show_dialog_add_to_collection(self):
        raise NotImplementedError
