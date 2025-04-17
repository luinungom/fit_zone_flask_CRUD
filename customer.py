class Customer:

    def __init__(self, id=None, name=None, surname=None, membership=None):
        self.id = id
        self.name = name
        self.surname = surname
        self.membership = membership

    def __str__(self):
        return f"Id: {self.id}, Name: {self.name}, Surname: {self.surname}, Membership: {self.membership}"
