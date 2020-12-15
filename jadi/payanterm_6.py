def reverse_dictionary(input_dict):
    output_dict = {}
    for key in input_dict :
        for value in input_dict[key] :
            if value not in output_dict.keys() :
                output_dict[value] = [key.lower()]
            else :
                output_dict[value].append(key.lower())
            output_dict[value].sort()
    return output_dict
        


print( reverse_dictionary({'Accurate': ['exact', 'precise'], 'exact': ['precise'], 'astute': ['Smart', 'clever'], 'smart': ['clever', 'bright', 'talented']}))
    
