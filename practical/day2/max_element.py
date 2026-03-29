def max_element(element_list):
    if element_list is not None:
        max_element = element_list[0]
        for element in element_list:
            if element > max_element:
                max_element = element

        return "Max Element: "+ str(max_element)
    else:
        return "Element list is empty"


print(max_element([10,5,20,8]))