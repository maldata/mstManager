import tkinter


class SeasonDropbox(tkinter.OptionMenu):
    def __init__(self, master, status, *options):
        self.var = tkinter.StringVar(master)
        self.var.set(status)
        tkinter.OptionMenu.__init__(self, master, self.var, *options)
        self.initUI()

    def initUI(self):
        self.master.title("Timer")
        self.pack(fill=tkinter.BOTH, expand=1)


class EpisodeListbox(tkinter.Listbox):
    def __init__(self, master):
        tkinter.Listbox.__init__(self, master)
        self.insert(tkinter.END, "K01")
        self.insert(tkinter.END, "K02")
        self.insert(tkinter.END, "K03")


def main():
    root = tkinter.Tk()
    root.geometry("500x300+300+300")
    text = tkinter.Label(root, text="You are currently on: ")
    text.place(x=10, y=55)
    skills = ['K', '1', '2', '3', '4', '5', '6']
    mymenu1 = SeasonDropbox(root, 'Select status', *skills)
    mymenu1.grid(column=2, row=2)
    mymenu1.place(x=130, y=50)
    mylist = EpisodeListbox(root)
    mylist.place(x=130, y=100)
    root.mainloop()

# buttons:
# Add Episode (string entry for episode #, string entry for movie #)
# Add Media Set (string entry for media set name)
# Add to Collection (for selected episode in listbox, dropbox for media set, string entry for notes)

if __name__ == '__main__':
    main()
