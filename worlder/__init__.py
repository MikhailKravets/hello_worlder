

class Hello:
    """Return various hello messages

    :param name: name to greet
    """
    def __init__(self, name: str):
        self.name = name

    def world(self):
        """Greats the world from predefined name"""
        return f"Hello World! From {self.name}"
