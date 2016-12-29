from context import *

import views
import views.tkView

def doAThing():
    print("Doin' a thing!")

app = views.tkView.TkView()

app.eventTestEvent.subscribe(doAThing)

app.mainloop()
