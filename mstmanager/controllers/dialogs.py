import logging


logger = logging.getLogger(__name__)


class EpisodeEntryController():
    def __init__(self):
        # Create closures to pass the self variable into the
        # handler class function
        def ok_clicked_closure(sender, **kwargs):
            self._handle_ok_clicked(sender, **kwargs)
        def cancel_clicked_closure(sender, **kwargs):
            self._handle_cancel_clicked(sender, **kwargs)

        # Store the reference to the closure so blinker doesn't eliminate
        # the weak reference
        self.ok_closure_ref = ok_clicked_closure
        self.cancel_closure_ref = cancel_clicked_closure

        self.view = None
        
        # Connect the closure to the signal
        self.view.ok_clicked.connect(ok_clicked_closure)
        self.view.cancel_clicked.connect(cancel_clicked_closure)

    def _handle_ok_clicked(self, sender, **kwargs):
        """
        Handler for the ok_clicked signal
        """
        logger.debug('Handling the OK-clicked signal')

    def _handle_cancel_clicked(self, sender, **kwargs):
        """
        Handler for the ok_clicked signal
        """
        logger.debug('Handling the cancel-clicked signal')

    def validate_episode_number(self, ep_num):
        long_enough = len(ep_num)
        number = ep_num[-2:]
        try:
            int(number)
            return long_enough
        except ValueError:
            return False
            
    def validate_title(self, title):
        t = title.strip()
        return len(t) > 0

    def show(self):
        self.view.init()
        results = self.view.run()

        if not results[0]:
            valid_ep_num = self.validate_episode_number(results[1])
            valid_title = self.validate_title(results[2])

        
