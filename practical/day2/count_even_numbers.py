def count_even(element_list):
    # count = 0
    # for num in element_list:
    #     if num % 2 == 0:
    #         count += 1
    #
    # return count

    # Better Solution
    print(lambda x: x % 2 == 0, element_list)
print(count_even([1,2,3,4,5,6,7,8,9,0,2,3,4,4]))