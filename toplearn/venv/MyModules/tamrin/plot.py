from matplotlib import pyplot

x = list()
i = -10
while i <= 10:
    x.append(round(i,10))
    i += 0.0001
print(list(x))
y = [n**2 for n in x]
a = pyplot.plot(x, y)
pyplot.show()
pyplot.close()
