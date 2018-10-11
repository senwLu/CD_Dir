# class is like a blueprint, in this case, a blueprint for instances/object of user
class User:
    # the __init__ method is called every time a new object is created
    def __init__(self, name, email):

        # attributes => characteristics shared by all instances of the class type
        self.name = name
        self.email = email
        self.logged = False

    # methods => actions that an object can preform
    def login(self):
        self.logged = True
        print(self.name + ' is logged in.')
        return self

    def logout(self):
        self.logged = False
        print(self.name + " is not logged in")
        return self

    def show(self):
        print("My name is {self.name}. You can email me at {self.email}.")
        return self


# an instance/object of the class User is created
new_user = User("Anna", "anna@anna.com")
print(new_user.email)
print(new_user.logged)
new_user.login()
