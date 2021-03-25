def bubble_sort(elements: list):
    """This is not optimized code."""
    n = len(elements)
    for i in range(n):
        for j in range(i+1):
            if elements[i] < elements[j]:
                elements[i], elements[j] = elements[j], elements[i]
    return elements


# driver function
if __name__ == '__main__':
    my_list = [63, 75, 48, 23, 54, 81, 29]
    try:
        print(bubble_sort(my_list))
    except TypeError as e:
        print('Error : ', e)
