class user:
    userCount = 0
    activeUsers = 0
    loggedUpUsers = list()
    loggedInUsers = list()

    def __init__(self, gotUserName='undefined', gotUserFamily='undefined', gotUserPassword=1234, gotAge=0):
        self.userName = gotUserName
        self.userFamily = gotUserFamily
        self._userPassword = gotUserPassword
        self.index = 0
        if gotAge > 0:
            self._age = gotAge
        userDict = {'name': gotUserName, 'family': gotUserFamily, 'age': gotAge}
        user.loggedUpUsers.append(userDict)
        user.userCount += 1

    def showFullName(self):
        return f"{self.userName} {self.userFamily}"

    # or
    @property
    def showfullName(self):
        return f"{self.userName} {self.userFamily}"

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, gotAge):
        if gotAge >= 0:
            self._age = gotAge
        else:
            raise ValueError("age can not be negetive!")

    def login(self, gotPassword):
        if self._userPassword == gotPassword:
            user.loggedInUsers.append(self.userFamily)
            user.activeUsers += 1
            print(f"{self.showFullName()} logged in!")
        else:
            print("Password is inCorrect!!")

    def logOut(self):
        if self.userFamily not in user.loggedInUsers:
            raise ValueError("you are not logged in !!")
        else:
            user.activeUsers -= 1
            user.loggedInUsers.remove(self.userFamily)
            print(f"{self.showFullName()} has logged out!")

    @classmethod
    def getActiveUsersCount(cls):
        print(f"there are currently {cls.activeUsers} active users.")

    @classmethod
    def fromString(cls, stringData):
        name, family = stringData.split()
        return cls(name, family)

    def __repr__(self):
        return f"{self.showFullName()}"

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < user.userCount:
            person = user.loggedUpUsers[self.index]
            self.index += 1
            return person
        else:
            self.index = 0
            raise StopIteration
# print(help(user))
