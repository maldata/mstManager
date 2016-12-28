# http://stackoverflow.com/questions/1904351/python-observer-pattern-examples-tips

from . import observer as obs


class Event:

    def __init__(self, name, data, autofire=True):
        self.name = name
        self.data = data
        if autofire:
            self.fire()

    def fire(self):
        for o in obs.Observer._observers:
            if self.name in o._observables:
                o._observables[self.name](self.data)
