from app.database import DB

class User(object):
    def __init__(self, id, firstname, lastname, email, password):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.sessions = []

    def json(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "password": self.password,
            "sessions": self.sessions
        }