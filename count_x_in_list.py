""" Find count of "X" in a given list. """

def find_count_x(sequence:list, x:int):

    answer = 0

    for i in range(len(sequence)):
        if x == sequence[i]:
            answer += 1
    return answer

sequence = [0, 7, 8, 90, 34, 6, 4, 4, 4, 3, 5, 67, 7, 8, 7, 5 ,3, 0]
x = int(input("Enter any number: "))

print(find_count_x(sequence, x))