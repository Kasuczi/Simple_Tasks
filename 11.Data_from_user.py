class User:

    def __init__(self, name, lastname, city):
        "the func initialize parameters which is going to be take from user"
        self._name = name
        self._lastname = lastname
        self._city = city

    @classmethod
    def from_input(cls):
        "the func takes the data from user"
        return cls(
            input('First Name: '),
            input('Last Name: '), 
            input('City: '),
        )


if __name__ == '__main__':
    users = {}
    for _ in range(1):  
        user = User.from_input()  
        users[user._name] = user 
        users[user._lastname] = user
        users[user._city] = user  
    print(users)
