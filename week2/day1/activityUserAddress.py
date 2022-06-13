class User:
    def __init__ (self, first_name, last_name, address=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
    def createNewAddress (self, stacyAddress):
        stacyUser.address.append(stacyAddress)


class Address:
    def __init__ (self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

stacyUser = User("Stacy", "Samuels")
stacyAddress = Address("NoWhereLand", "Baton Rouge", "LA", "11111")



stacyUser.createNewAddress(stacyAddress)
print(stacyUser.address[0].zip_code)
