from context import *

import views
import views.tkView


def collectionEv():
    print("Add to collection")

def mediaEv():
    print("Add media")

def episodeEv():
    print("Add episode")

app = views.tkView.TkView()

app.addToCollectionEvent.subscribe(collectionEv)
app.addMediaSetEvent.subscribe(mediaEv)
app.addEpisodeEvent.subscribe(episodeEv)

app.init_ui()
app.run_ui()
