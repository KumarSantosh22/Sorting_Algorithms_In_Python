def merge_list(arr1, arr2):
    sorted_list = []
    len_a = len(arr1)
    len_b = len(arr2)
    i = j = 0

    while i < len_a and j < len_b:
        if arr1[i] <= arr2[j]:
            sorted_list.append(arr1[i])
            i += 1
        else:
            sorted_list.append(arr2[j])
            j += 1

    while i < len_a:
        sorted_list.append(arr1[i])
        i += 1

    while j < len_b:
        sorted_list.append(arr2[j])
        j += 1

    return sorted_list


def merge_sort(arr: list):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_list(left, right)


""" T(n) = O(nlogn)
It is the algorithm used by Python built in sort() function.
Python uses Timsort which is a hybrid stable sorting algorithm, derived from merge sort and insertion sort. """

if __name__ == '__main__':
    lst = [11, 9, 29, 7, 9, 2, 15, 28]
    print(merge_sort(lst))

