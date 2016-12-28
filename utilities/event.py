class Event:
    def __init__(self):
        self.handlers=[]

    def subscribe(self, handler):
        self.handlers.append(handler)

    def unsubscribe_all(self):
        self.handlers.clear()

    def fire(self, *args):
        """
        Fires this event, which means we call all of the subscribed event handlers.
        :param *args: An arbitrary number of arguments that will get passed to the handlers.
        All handlers get the same arguments.
        """
        for h in self.handlers:
            h(*args)


if __name__ == '__main__':
    print("Starting event test...")

    def variable_args(*args):
        for arg in args:
            print(arg)

    def three_args(arg1, arg2, arg3):
        print(arg1, arg2, arg3)

    e = Event()
    e.subscribe(variable_args)
    e.subscribe(three_args)
    e.subscribe(variable_args)
    e.fire("s1", "s2", "s3")
    e.unsubscribe_all()
    e.fire("s4", "s5", "s6")
