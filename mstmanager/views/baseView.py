from mstmanager.utilities.event import Event


class BaseDialog:
    def __init__(self):
        pass    


class BaseView:
    def __init__(self):
        self.addEpisodeEvent = Event()
        self.addMediaSetEvent = Event()
        self.addToCollectionEvent = Event()
        self.listSeasonEvent = Event()
        self.receivedEpisode = Event()
        self.requestMediaSetUpdate = Event()

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

    def show_episodes_for_selected_season(self, episodes):
        raise NotImplementedError
    
