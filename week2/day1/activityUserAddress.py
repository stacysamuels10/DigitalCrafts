class User:
    def __init__ (self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
stacyUser = User("Stacy", "Samuels")

class Address:
    def __init__ (self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

stacyUser = Address("NoWhereLand", "Baton Rouge", "LA", "11111")