def merge_list(arr1, arr2, arr):
    len_a = len(arr1)
    len_b = len(arr2)
    i = j = k = 0

    while i < len_a and j < len_b:
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1

    while i < len_a:
        arr[k] = arr1[i]
        i += 1
        k += 1

    while j < len_b:
        arr[k] = arr2[j]
        j += 1
        k += 1


def merge_sort(arr: list):
    if len(arr) <= 1:
        return
    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_list(left, right, arr)


""" T(n) = O(nlogn) => This algorithm is inplace. It doesn't need extra space.
It is the algorithm used by Python built in sort() function.
Python uses Timsort which is a hybrid stable sorting algorithm, derived from merge sort and insertion sort. """

if __name__ == '__main__':
    lst = [11, 9, 29, 7, 9, 2, 15, 28]
    merge_sort(lst)
    print(lst)
