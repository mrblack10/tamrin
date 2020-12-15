# lets work with some files


myfile = open('test.txt','r+')

print(myfile.readlines())

print('positio:',myfile.tell())

myfile.seek(16)

print(myfile.readline())

print('positio:',myfile.tell())


myfile.close()
