import tkinter as tk
import math

# Create the main tkinter window
root = tk.Tk()
root.title("Rotating Rectangle")

# Create a Canvas widget
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Rectangle coordinates
x1, y1 = 250, 250
x2, y2 = 280, 280
x3, y3 = x1, y2
x4, y4 = x2, y1

# Create a rectangle
rectangle = canvas.create_polygon(x1, y1, x3, y3, x2, y2, x4, y4, fill="blue")

# Function to rotate the rectangle
def rotate_rectangle(angle):
    global x1,y1,x2,y2,x3,y3,x4,y4
    global rectangle
    # Rotate by 30 degrees
    print(angle)
    angle_degrees = angle

    # Calculate the center of the rectangle
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2

    # Convert the angle to radians
    angle_radians = math.radians(angle_degrees)

    # Rotate the rectangle
    canvas.delete(rectangle)

    x1,y1 = rotate_point(x1,y1,cx,cy,angle_radians)
    x2,y2 = rotate_point(x2,y2,cx,cy,angle_radians)
    x3,y3 = rotate_point(x3,y3,cx,cy,angle_radians)
    x4,y4 = rotate_point(x4,y4,cx,cy,angle_radians)
    rectangle = canvas.create_polygon(x1,y1,x3,y3,x2,y2,x4,y4,fill="red")
    print(canvas.coords(rectangle))
# [257.5, 252.00961894323342, 268.48076211353316, 292.9903810567666, 242.5, 277.9903810567666, 283.48076211353316, 267.0096189432334]
# Rotate a point (x, y) around a center (cx, cy) by an angle (radians)
def rotate_point(x, y, cx, cy, angle):
    dx = x - cx
    dy = y - cy
    new_x = cx + dx * math.cos(angle) - dy * math.sin(angle)
    new_y = cy + dx * math.sin(angle) + dy * math.cos(angle)
    return new_x, new_y

# Bind a click event to rotate the rectangle
# lambda txt="stop":printlines(txt)
# button.bind("<Button-1>", lambda event, arg1="Hello", arg2="World": my_function(arg1, arg2))
root.bind("<d>", lambda event,a=30:rotate_rectangle(a))
root.bind("<a>", lambda event,a=-30:rotate_rectangle(a))

root.mainloop()
