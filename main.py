import tkinter as tk
import random
import bubblesort
import insertionSort

# Create the main window
window = tk.Tk()

# Create a canvas to display the sorting animation
canvas = tk.Canvas(window, width=800, height=600)
canvas.pack()

# Generate a random list to sort
# lst = random.sample(range(1, 100), 90)

# Define a function to draw the list on the canvas
def draw_list(lst, window):
    canvas.delete('all') # clear the canvas
    bar_width = 5
    x = 50
    y_scale = 5
    for i, num in enumerate(lst):
        height = num * y_scale
        canvas.create_rectangle(x, 600-height, x+bar_width, 600, fill='black')
        # canvas.create_text(x+bar_width//2, 500-height-10, text=str(num))
        x += bar_width 

sorted_list1 = bubblesort.bubble_sort
sorted_list2 = insertionSort.insertion_sort
functionList = [sorted_list1, sorted_list2]

# def animate_sort(lst, window):
#     bubblesort.bubble_sort(lst, window, draw_list)
#     # Call the draw_list function after each iteration of the sorting algorithm
#     window.after(10) # Call the function again after 100 milliseconds

# # Call the animate_sort function to start the animation
# animate_sort(lst, window)

for func in functionList:
    lst = random.sample(range(1, 100), 75)
    func(lst,window,draw_list)
    window.after(100)

# Start the main loop
window.mainloop()
