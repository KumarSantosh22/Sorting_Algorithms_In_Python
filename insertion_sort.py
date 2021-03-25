def insertion_sort(elements: list):
    """ a.k.a. online algorithm """
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i-1
        while j >= 0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j-1
        elements[j+1] = anchor


if __name__ == '__main__':
    lst = [21, 38, 29, 17, 4, 25, 11, 32, 9]
    insertion_sort(lst)
    print(lst)
    print(insertion_sort.__doc__)
