class _Private:
    def __init__(self, name):
        self.name = name

class NotPrivate:
    def __init__(self, name):
        self.name = name
        self.priv =  _Private(name)

    def display(self):
        print("This is not a private method")

    def _display(self):
        print("This is a private method")