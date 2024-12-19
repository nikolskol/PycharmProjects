# Объединение и сортировка двух списков:

def merge_and_sort(list1, list2):
    return sorted(list1 + list2)

a = [1,2,3]
b = [12,-2,5]
print(merge_and_sort(a, b))