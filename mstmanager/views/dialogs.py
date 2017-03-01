import logging
import tkinter

from blinker import signal


logger = logging.getLogger(__name__)




class EpisodeEntryDialog(tkinter.TopLevel):
    def __init__(self, parent):
        super().__init__(self, parent)
        self.transient(parent)
        self.parent = parent
        
        self.title('Enter episode number and title')

        self.ok_clicked_signal = signal('episode_entry_ok')
        self.cancel_clicked_signal = signal('episode_entry_cancel')

        self.result = None

        body = Frame(self)
        body.pack(padx=5, pady=5)

        box = Frame(self)

        w = Button(box, text="OK", width=10,
                   command=self.ok_clicked, default=ACTIVE)
        w.pack(side=LEFT, padx=5, pady=5)
        w = Button(box, text="Cancel", width=10,
                   command=self.cancel_clicked)
        w.pack(side=LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        box.pack()

        self.grab_set()

        if not self.initial_focus:
            self.initial_focus = self

        self.protocol("WM_DELETE_WINDOW", self.cancel)

        self.geometry("+%d+%d" % (parent.winfo_rootx()+50,
                                  parent.winfo_rooty()+50))

        self.initial_focus.focus_set()

        self.wait_window(self)


    def ok_clicked(self):
        self.ok_clicked_signal.send(self, (self.ep_num, self.ep_title))

    def cancel_clicked(self):
        self.cancel_clicked_signal.send(self)
        
