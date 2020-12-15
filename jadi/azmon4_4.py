def anagrams(s1, s2):
    if len(s1) != len(s2) :
        return False
    s1 = s1.lower()
    s2 = s2.lower()
    for i in s1 :
        if s1.count(i) != s2.count(i) :
            return False
    return True

s1 =  "Orchestra"
s2 =  "Carthorse"

print(anagrams(s1, s2)) 
