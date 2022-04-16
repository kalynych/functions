""" Check if all elements of list are integers"""

def check_if_all_elements_are_int(seq):
    return all(isinstance(seq[i], int) for i in range(len(seq)))

my_list = [1, 3, 5, "hello"]

answer = check_if_all_elements_are_int(my_list)

if answer:
    print("All elements of list --> are integers.")
else:
    print("Not all elements of list --> are integers.")

check_if_all_elements_are_int(my_list)