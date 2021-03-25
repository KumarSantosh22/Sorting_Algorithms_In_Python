def bubble_sort_optimized(elements: list):
    n = len(elements)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]
                swapped = True
        if not swapped:
            break
    return elements


# driver function
if __name__ == '__main__':
    my_list = [63, 75, 48, 23, 54, 81, 29]
    try:
        bubble_sort_optimized(my_list)
        print(my_list)
    except TypeError as e:
        print('Error : ', e)
