import tkinter
from utilities.event import Event


class TkView():
    def __init__(self):
        self.addEpisodeEvent = Event()
        self.addMediaSetEvent = Event()
        self.addToCollectionEvent = Event()
        self.eventTestEvent = Event()

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

        b = tkinter.Button(f2, text="Add Episode", command=self.clicked_add_episode)
        b.pack(fill=tkinter.X)
        b = tkinter.Button(f2, text="Add Media Set", command=self.clicked_add_media_set)
        b.pack(fill=tkinter.X)
        b = tkinter.Button(f2, text="Add to Collection", command=self.clicked_add_to_collection)
        b.pack(fill=tkinter.X)
        b = tkinter.Button(f2, text="Event Test", command=self.eventTestEvent.fire)
        b.pack(fill=tkinter.X)

    def init_ui(self):
        # TODO: everything that's currently in the constructor should probably be here.
        pass

    def clicked_add_episode(self):
        print("Add Episode clicked.")

    def clicked_add_media_set(self):
        print("Add Media Set clicked.")

    def clicked_add_to_collection(self):
        print("Add to Collection clicked.")

    def mainloop(self):
        self.root.mainloop()

# class SeasonDropbox(tkinter.OptionMenu):
#     def __init__(self, master, status, *options):
#         self.var = tkinter.StringVar(master)
#         self.var.set(status)
#         tkinter.OptionMenu.__init__(self, master, self.var, *options)
#         self.initUI()
#
#     def initUI(self):
#         self.master.title("Timer")
#         self.pack(fill=tkinter.BOTH, expand=1)
#
#
# class EpisodeListbox(tkinter.Listbox):
#     def __init__(self, master):
#         tkinter.Listbox.__init__(self, master)
#         self.insert(tkinter.END, "K01")
#         self.insert(tkinter.END, "K02")
#         self.insert(tkinter.END, "K03")
#
#
# def clicked_add_episode():
#     pass
#
# def clicked_add_media_set():
#     pass
#
# def clicked_add_to_collection():
#     pass
#
#
# def main():
#     root = tkinter.Tk()
#     root.geometry("600x400+200+200")
#     root.title("MST Manager")
#     f1 = tkinter.Frame(root, borderwidth=2, relief=tkinter.SUNKEN)
#     f1.pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True)
#     f2 = tkinter.Frame(root, borderwidth=2, relief=tkinter.SUNKEN)
#     f2.pack(fill=tkinter.BOTH, side=tkinter.LEFT)
#
#     w = tkinter.Label(f1, text="Red", bg="red", fg="white")
#     w.pack()
#     w = tkinter.Label(f1, text="Green", bg="green", fg="black")
#     w.pack()
#     w = tkinter.Label(f1, text="Blue", bg="blue", fg="white")
#     w.pack()
#     listbox = tkinter.Listbox(f1)
#     listbox.pack(fill=tkinter.BOTH, expand=True)
#     for item in ["one", "two", "three", "four"]:
#         listbox.insert(tkinter.END, item)
#
#     b = tkinter.Button(f2, text="Add Episode", command=clicked_add_episode)
#     b.pack(fill=tkinter.X)
#     b = tkinter.Button(f2, text="Add Media Set", command=clicked_add_media_set)
#     b.pack(fill=tkinter.X)
#     b = tkinter.Button(f2, text="Add to Collection", command=clicked_add_to_collection)
#     b.pack(fill=tkinter.X)
#
#
#     # text = tkinter.Label(root, text="You are currently on: ")
#     # text.place(x=10, y=55)
#     # skills = ['K', '1', '2', '3', '4', '5', '6']
#     # mymenu1 = SeasonDropbox(root, 'Select status', *skills)
#     # mymenu1.grid(column=2, row=2)
#     # mymenu1.place(x=130, y=50)
#     # mylist = EpisodeListbox(root)
#     # mylist.place(x=130, y=100)
#     root.mainloop()

# buttons:
# Add Episode (string entry for episode #, string entry for movie #)
# Add Media Set (string entry for media set name)
# Add to Collection (for selected episode in listbox, dropbox for media set, string entry for notes)

#if __name__ == '__main__':
#    def doAThing():
#        print("Doin' a thing!")
#
#    app = TkView()
#
#    app.eventTestEvent.subscribe(doAThing)
#
#    app.mainloop()
