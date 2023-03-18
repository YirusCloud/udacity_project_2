def sort_012(input_list):

    count_0 = 0
    count_1 = 0
    count_2 = 0

    for digit in input_list:
        if digit == 0:
            count_0 += 1
        elif digit == 1:
            count_1 += 1
        elif digit == 2:
            count_2 += 1

    
    sorted_list = [0] * count_0 + [1] * count_1 + [2] * count_2

    return sorted_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])


