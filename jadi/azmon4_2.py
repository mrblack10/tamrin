def count_consonants(sample_string):
    sample_string = sample_string.lower().replace(' ','')
    s = 0
    sedadar = ['a','e','i','o','u']
    for ch in sample_string :
        if ch not in sedadar :
            s += 1
    return s

sample_string = 'armin azarakhsh'
print(count_consonants(sample_string))
