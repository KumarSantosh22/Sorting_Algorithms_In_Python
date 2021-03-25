def shell_sort(arr: list):
    size = len(arr)
    gap = size // 2
    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j-gap] > anchor:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor
        gap = gap // 2


""" It is an optimization over Insertion sort. It uses the concept of gap.
It starts with the gap n/2 and sort sub arrays, and keep  reducing the gap by n/2 in.
Last Iteration have the gap=1. At this point it is same as Insertion sort but
the only difference is number of swaps is reduced. """


if __name__ == '__main__':
    lst = [21, 38, 29, 17, 4, 25, 11, 32, 9]
    shell_sort(lst)
    print(lst)
