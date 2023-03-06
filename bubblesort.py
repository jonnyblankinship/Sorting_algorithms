#Bubble sort
def bubble_sort(array, window, draw_list):
    
    n = len(array)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                draw_list(array, window)
                window.update()
                already_sorted = False
        if already_sorted:
            break
    return array
