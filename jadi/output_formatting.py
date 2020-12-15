# output formatting

scores = [ ['armin',17,18,19],
           ['jadi',8.5,12,18],
           ['sara',18,19,20]
        ]

for person in scores :
    for item in person :
        if type(item) == str :
            print ("{:6s}: |".format(item),end='')
        else:
            print ("{:7.2f} |".format(item),end='')
    print()

str = "str is _{:*^7s}_".format('armin')

print(str)
        
