class InMemoryRepository:
    def __init__(self):
        self.users = []

    def add(self, user):
        self.users.append(user)

    def get(self, id):
        return self.users[id]

