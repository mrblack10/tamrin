# a program to calculate the size of pizza

# read shoa
shoa = input ("please give me the shoa: ")

# convert shoa to number
shoa = float(shoa)

# everybody knows it
pi = 3.1415

# calculate the area
pizza= pi*(shoa**2)
if pizza < 100:
    print("very small pizza")
elif pizza >= 100 and pizza < 200:
    print("normal size")
else:
    print("huuuuuge pizza")

print("the size of your pizza is ",pizza)

