def construct_dictionary_from_lists(names, ages, scores):
    dict = {}
    for i in range(len(names)) :
        t = 'fail'
        if scores[i]>=60 :
            t = 'pass'
        dict[names[i]] = [ages[i],scores[i],t]
    return dict


names = ["paul", "saul", "steve", "chimpy"]

ages = [28, 59, 22, 5]

scores = [59, 85, 55, 60]


print (construct_dictionary_from_lists(names, ages, scores))
