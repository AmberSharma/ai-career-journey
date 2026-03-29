def remove_duplicates(element_list):
    return list(dict.fromkeys(element_list))
    # Better Solution
    # return list(set(element_list))

print(remove_duplicates([1,1,2,3,4,5,5,5,5]))