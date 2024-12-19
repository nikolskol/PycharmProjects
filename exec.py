# Найти второе по величине число:

def find_second_largest(listik):
    first, second = float('-inf'), float('-inf')
    for num in listik:
        if num > first:
            first, second = num, first
        elif num > second and num != first:
            second = num
    return second

print(find_second_largest([1,15,18,22,27,4,12,29]))