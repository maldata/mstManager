import tkinter
from views import baseView


class TkView(baseView.BaseView):
    def __init__(self):
        super().__init__()

        self.root = tkinter.Tk()
        self.root.geometry("600x400+200+200")
        self.root.title("MST Manager")

        f1 = tkinter.Frame(self.root, borderwidth=2, relief=tkinter.SUNKEN)
        f1.pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True)
        f2 = tkinter.Frame(self.root, borderwidth=2, relief=tkinter.SUNKEN)
        f2.pack(fill=tkinter.BOTH, side=tkinter.LEFT)
        f3 = tkinter.Frame(f1, borderwidth=2, relief=tkinter.SUNKEN)
        f3.pack(fill=tkinter.X, side=tkinter.TOP)

        w = tkinter.Label(f3, text="Season:")
        w.pack(side=tkinter.LEFT)

        # TODO: get this from controller
        seasons = ['K', '1', '2', '3', '4', '5', '6']
        self.seasonVar = tkinter.StringVar(self.root)
        self.seasonVar.set('Select season')
        self.seasonDropbox = tkinter.OptionMenu(f3, self.seasonVar, *seasons)
        self.seasonDropbox.pack(side=tkinter.LEFT)

        self.listbox = tkinter.Listbox(f1)
        self.listbox.pack(fill=tkinter.BOTH, side=tkinter.TOP, expand=True)
        for item in ["one", "two", "three", "four"]:
            self.listbox.insert(tkinter.END, item)

        # If any of these events need to send data also, just call a class private method as the
        # command, and let that method grab the data it needs and fire the event.
        b = tkinter.Button(f2, text="Add Episode", command=self.addEpisodeEvent.fire)
        b.pack(fill=tkinter.X)
        b = tkinter.Button(f2, text="Add Media Set", command=self.addMediaSetEvent.fire)
        b.pack(fill=tkinter.X)
        b = tkinter.Button(f2, text="Add to Collection", command=self.addToCollectionEvent.fire)
        b.pack(fill=tkinter.X)

    def init_ui(self):
        """
        Anything that needs to be done to get the UI visually ready for use should be done here.
        The constructor should be used only to prepare member objects.
        :return: Nothing
        """
        # TODO: everything that's currently in the constructor should probably be here.
        pass

    def run_ui(self):
        self.root.mainloop()
