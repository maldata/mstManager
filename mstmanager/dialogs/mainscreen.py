import blinker


class MainScreenController:
    def __init__(self):
        def handle_new_episode_request(sender, **kwargs):
            self.new_episode_request_handler(sender, **kwargs)
        def handle_new_media_set_request(sender, **kwargs):
            self.new_media_set_request_handler(sender, **kwargs)
            
        self.handle_new_episode_request_ref = handle_new_episode_request
        self.handle_new_media_set_request_ref = handle_new_media_set_request

        self.view = MainScreenView()
        self.view.new_episode_requested.connect(handle_new_episode_request)
        self.view.new_media_set_requested.connect(handle_new_media_set_request)
        
    def new_episode_request_handler(self, sender, **kwargs):
        print(sender, kwargs['message'])
        # TODO: business logic for verifying & inserting in DB

    def new_media_set_request_handler(self, sender, **kwargs):
        print(sender, kwargs['message'])
        # TODO: business logic for verifying & inserting in DB

    def run_ui(self):
        self.view.show()

        
class MainScreenView:
    def __init__(self):
        self.prompt = '--> '
        self.new_episode_requested = blinker.signal('new_episode_requested')
        self.new_media_set_requested = blinker.signal('new_media_set_requested')
        
    def show(self):
        running = True
        while running:
            print('1. Add new episode')
            print('2. Add new media set')
            main_menu_choice = input(self.prompt)
            main_menu_choice = main_menu_choice.upper()

            if main_menu_choice == '1':
                self.new_episode_requested.send(self, message='new ep. selected')
            elif main_menu_choice == '2':
                self.new_media_set_requested.send(self, message='new med. set sel.')
            elif main_menu_choice == 'Q':
                running = False
            else:
                print('not a thing')
