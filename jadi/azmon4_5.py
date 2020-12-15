def my_encryption(s):
    output = ''
    character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    secret_key    = "Dd18Abz2EqNPW hYTOjBvtVlpXaH6msFUICg4o0KZwJeryQx3f9kSinRu5L7cGM"
    for ch in s :
        output = output + secret_key[character_set.find(ch)]
    return output

s = "Lets meet at the usual place at 9 am"
        
print( my_encryption(s))
