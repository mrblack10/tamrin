def find_word_horizontal(crosswords,word):
    for row in range(len(crosswords)) :
        s = ''
        for ch in crosswords[row] :
            s += ch
        #print('row:',s)
        if word in s :
            #print('s:',s,"-----> YES")
            return [row,s.find(word)]

crosswords=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
word='pat'
print(find_word_horizontal(crosswords,word))
