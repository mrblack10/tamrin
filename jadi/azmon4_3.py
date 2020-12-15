def find_longest_word(input_string):
    input_string = input_string.split()
    #print(input_string)
    maxs = None
    maxlen = 0
    for s in input_string :
        #print ('s:',s)
        if len(s)>= maxlen :
            maxlen = len(s)
            maxs = s
        #print (maxlen,maxs,'\n************')
    return maxs

input_string = 'armin azarakhsh dos dre toro'
print (find_longest_word(input_string))
