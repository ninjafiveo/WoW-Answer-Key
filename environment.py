class Environment:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"Environment: {self.name}, Description: {self.description}"
