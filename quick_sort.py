def partition(elements, start, end):
    pivot_i = start
    pivot = elements[pivot_i]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1

        while elements[end] > pivot:
            end -= 1

        if start < end:
            elements[start], elements[end] = elements[end], elements[start]

    elements[pivot_i], elements[end] = elements[end], elements[pivot_i]

    return end


""" Avg T(n) = O(nlogn)
    Worst Case T(n) = O(n^2)  when list is already sorted """


def quick_sort(arr: list, start, end):
    if start < end:
        pi = partition(arr, start, end)
        quick_sort(arr, start, pi - 1)  # left partition
        quick_sort(arr, pi + 1, end)  # right partition


if __name__ == '__main__':
    lst = [11, 9, 29, 7, 9, 2, 15, 28]
    quick_sort(lst, 0, len(lst) - 1)
    print(lst)
