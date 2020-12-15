def find_word_vertical(crosswords,word):
    for i in range(len(crosswords[0])):
        s = ''
        for j in range(len(crosswords)):
            s += crosswords[j][i]
        #print(s)
        if word in s :
            return [s.find(word),i]
        

crosswords=[['s','d','o','g','a'],['c','u','c','m','b'],['a','c','a','t','v'],['t','e','t','k','c']]
word='ce'

print(find_word_vertical(crosswords,word)[0])
