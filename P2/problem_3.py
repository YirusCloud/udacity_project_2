def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) < 2:
        return [-1, -1]

    # sort the input list in descending order
    sorted_list = sorted(input_list, reverse=True)

    # initialize two empty strings to represent the two numbers we will form
    num1_str = ""
    num2_str = ""

    # iterate through the sorted list and alternate adding each element to one of the two numbers
    for i, num in enumerate(sorted_list):
        if i % 2 == 0:
            num1_str += str(num)
        else:
            num2_str += str(num)

    # convert the two strings to integers and return them
    return [int(num1_str), int(num2_str)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)
test_function([[], [-1, -1]])
test_function([[0], [-1, -1]])
test_function([[0, 0], [0, 0]])
test_function([[1, 1, 1, 3, 5, 6], [631, 511]])
