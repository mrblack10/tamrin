def find_word_horizontal(crosswords,word):
    for row in range(len(crosswords)) :
        s = ''
        for ch in crosswords[row] :
            s += ch
        if word in s :
            return [row,s.find(word)]
        
###################################################

def find_word_vertical(crosswords,word):
    for i in range(len(crosswords[0])):
        s = ''
        for j in range(len(crosswords)):
            s += crosswords[j][i]
        #print(s)
        if word in s :
            return [s.find(word),i]
###################################################

def capitalize_word_in_crossword(crosswords,word):
    row = find_word_horizontal(crosswords,word)
    col = find_word_vertical(crosswords,word)
    #print('row:',row)
    #print('col:',col)
    if row != None :
        for l in range(0,len(word)) :
            crosswords[row[0]][row[1]+l] = crosswords[row[0]][row[1]+l].upper() 
            
    elif  col != None :
        for l in range(0,len(word)) :
            crosswords[col[0]+l][col[1]] = crosswords[col[0]+l][col[1]].upper()
    return crosswords

#**********************main code****************************************************

crosswords=[['s','d','o','g'],['c','u','c','m'],['a','x','a','t'],['t','e','t','k']]
word='cat'
print(capitalize_word_in_crossword(crosswords,word))
