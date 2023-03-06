#insertion sort
def insertion_sort(array, window, draw_list):
   # Loop from the second element of the array until
   # the last element
    for i in range(1, len(array)):
       key_item = array[i]
       j = i - 1

       while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
            draw_list(array, window)
            window.update()
       array[j + 1] = key_item

    return array

