def selection_sort(elements: list):
    """ simplest algorithm and T(n) = O(n^2) """
    n = len(elements)
    for i in range(n-1):
        min_i = i
        for j in range(min_i+1, n):
            if elements[j] < elements[min_i]:
                min_i = j
        if i != min_i:
            elements[i], elements[min_i] = elements[min_i], elements[i]


if __name__ == '__main__':
    lst = [21, 38, 29, 17, 4, 25, 11, 32, 9]
    selection_sort(lst)
    print(lst)
