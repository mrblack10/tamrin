from MyModules.tamrin.circle import masahat
from MyModules.tamrin.Class.user_class import user

# print(f"active users : {user.userCount}")
armin = user("armin", 'azarakhsh', 1234, 20)
armin.login(1234)
print(armin.showFullName())
print(armin.showfullName)  # property
print(armin)  # repr
print(armin.age)  # property
# print(armin._userPassword)
soheil = user("soheil", "zolal", 5678)
soheil.login(5678)
# print(soheil.userName)
ali = user()
# print(f"logged up users : {user.userCount}")
# print(f"logged in users : {user.loggedInUsers}")
armin.logOut()
user.getActiveUsersCount()
print(f"active users : {user.activeUsers}\nlogged in users : {user.loggedInUsers}")
print(user.fromString("danial ronaqi").showFullName())
print(f"logged up users : {user.loggedUpUsers}")
# ali.logOut()
# print(armin)
# print(masahat(10))
# print(dir())

for person in armin:
    print(person)
#print(armin.index)