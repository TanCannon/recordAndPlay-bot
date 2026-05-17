'''path remebering logic2''''''sleep_time is the speed of the car'''
'''issues:cannot use variable speed'''

import tkinter as tk
from time import *
import sys
import math

#varibles i need
# state = -1
pause = 1
index = -1
# count = 0
'''The maximum size of an array on an arduino is 32767 bytes'''
'''one int = 8byte => 8191.75 ints we can u, so if radius of wheel is 5cm => perimeter = 31.5cm => 31.5*8191.75 = 258040.125cm => 2.58040125km can be covered'''
seq_move = [-1 for i in range(700)]
# seq_time = [-1 for i in range(4)]
# st_time = int(time()*1000)

# Rectangle coordinates (x1,y1),(x3,y3),(x2,y2),(x4,y4)
x1, y1 = 250, 250
x2, y2 = 280, 280
x3, y3 = x1, y2
x4, y4 = x2, y1

cx = (x1 + x2) / 2
cy = (y1 + y2) / 2
print(cx,cy)

sleep_time = 0.055 #the constant speed

root = tk.Tk()
root.geometry("900x500")

#--record movements----#
def stop(event):
    global index
    # while pause:
    #     root.update()
    #     sleep(0.5)
    print(f'index={index}')
    index +=1
    seq_move[index] = 0
    go_stop()

def up(event):
    global index,pause
    # pause=0
    print(f'index={index}')
    index +=1
    seq_move[index] = 1
    go_forward()    

def down(event):
    global index
    print(f'index={index}')
    index +=1
    seq_move[index] = 2
    go_backward()
        
def right(event):
    global index
    print(f'index={index}')
    index +=1
    seq_move[index] = 3
    go_right()
    
def left(event):
    global index
    print(f'index={index}')
    index +=1
    seq_move[index] = 4
    go_left()

def rotate(angle):
    global index
    print(f'index={index}')
    index +=1
    if (angle>0):
        seq_move[index] = 5
    else:
        seq_move[index] = -5
    go_rotate(angle)

'''--------------------------------------------'''    

#------do movements-------------
def go_stop():
    print("go_stop")

def go_forward():
    global pause,cy
    global x1,y1,x2,y2,x3,y3,x4,y4
    print("go_forward")
    # new_cords = canvas_1.coords(car)
    # print(new_cords)
    x=0
    y=-5
    cy-=5
    y1-=5
    y2-=5
    y3-=5
    y4-=5
    canvas_1.move(car,x,y)
    # new_cords = canvas_1.coords(car)
    # print(new_cords)
    # pause = 1
    # stop()

def go_backward():
    global cy
    global x1,y1,x2,y2,x3,y3,x4,y4
    print("go_backward")
    x=0
    y=5
    cy+=5
    y1+=5
    y2+=5
    y3+=5
    y4+=5
    canvas_1.move(car,x,y)

def go_right():
    global cx
    global x1,y1,x2,y2,x3,y3,x4,y4
    print("go_right")
    x=5
    cx+=5
    y=0
    x1+=5
    x2+=5
    x3+=5
    x4+=5
    canvas_1.move(car,x,y)

def go_left():
    global cx
    global x1,y1,x2,y2,x3,y3,x4,y4
    print("go_left")
    x=-5
    cx-=5
    y=0
    x1-=5
    x2-=5
    x3-=5
    x4-=5
    canvas_1.move(car,x,y)

def go_rotate(angle):
    print("go_rotate")
    # print(f"cx,cy={cx,cy}")
    global x1,y1,x2,y2,x3,y3,x4,y4
    global car
    # new_cords = canvas_1.coords(car)
    # print(new_cords)
    # for i in range(len(new_cords)):
    #     new_cords[i] = round(new_cords[i])
    # print(new_cords)
    # x1,y1,x2,y2,x3,y3,x4,y4 = new_cords
         
    # Rotate by "angle "degrees
    # print(angle)
    angle_degrees = angle

    # Calculate the center of the rectangle
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2

    # Convert the angle to radians
    angle_radians = math.radians(angle_degrees)

    # Rotate the rectangle
    canvas_1.delete(car)

    x1,y1 = rotate_point(x1,y1,cx,cy,angle_radians)
    x2,y2 = rotate_point(x2,y2,cx,cy,angle_radians)
    x3,y3 = rotate_point(x3,y3,cx,cy,angle_radians)
    x4,y4 = rotate_point(x4,y4,cx,cy,angle_radians)
    # print(x1,y1,)

    car = canvas_1.create_polygon(x1,y1,x3,y3,x2,y2,x4,y4,fill="red")

    # new_cords = canvas_1.coords(car)
    # # print(new_cords)
    # for i in range(len(new_cords)):
    #     new_cords[i] = round(new_cords[i])
    # print(new_cords)
    # print(canvas_1.coords(car))

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

'''-------------------------------------------------'''


def do_seq(event):
    global car,cx,cy
    # canvas_1.delete(car)
    # car = canvas_1.create_rectangle(250,250,280,280,fill="red")

    #setting the initial rectangel pararmeters
    # x1, y1 = 250, 250
    # x2, y2 = 280, 280
    # x3, y3 = x1, y2
    # x4, y4 = x2, y1
    # cx = (x1 + x2) / 2
    # cy = (y1 + y2) / 2
    # car = canvas_1.create_polygon(x1, y1, x3, y3, x2, y2, x4, y4, fill="blue")
    root.update()
    # start_time = int(time()*1000)
    # print(f'start_time={start_time}')
    print("\ndo_seq starts in 3sec\n")
    sleep(3)
    # start_time = int(time()*1000)
    # global count
    # count = 0
    # rng = len(seq_move)
    print("Going back.")
    for i in range(index,-1,-1):
        sleep(sleep_time)
        if seq_move[i] == 1:
                go_backward()
        elif seq_move[i] == 2:
                go_forward()
        elif seq_move[i] == 3:
                go_left()
        elif seq_move[i] == 4:
                go_right()
        elif seq_move[i] == 5:
                go_rotate(-30)
        elif seq_move[i] == -5:
                go_rotate(30)
        elif seq_move[i] == 0:
            go_stop()
            # print("stop")
            # break
        else:
            root.update()
            break
        root.update()
    print("Playback starting in 3s.")
    sleep(3)
    for i in seq_move:
        print(cx,cy)
        # current_time = int(time()*1000)-start_time
        sleep(sleep_time)
        if i == 1:
                go_forward()
        elif i == 2:
                go_backward()
        elif i == 3:
                go_right()
        elif i == 4:
                go_left()
        elif i == 5:
                go_rotate(30)
        elif i == -5:
                go_rotate(-30)
        elif i == 0:
            go_stop()
            # print("stop")
            # break
        else:
            root.update()
            break
        root.update()
    print("Playback ended.")

def show_data(event):
    print(f'seq_move={seq_move}')
    print(f'Memory size={sys.getsizeof(seq_move)}')
    # print(f'seq_time={seq_time}')

def reset_data(event):
    # global seq_move,seq_time,index,state,count,st_time
    global seq_move,index
    print("Data reset!!")
    seq_move = [-1 for i in range(700)]
    # seq_time = [-1 for i in range(4)]
    index = -1
    # state = -1
    # count = 0
    # st_time = int(time()*1000)

canvas_1 = tk.Canvas(root,bg="gray",width=900,height=500)
canvas_1.pack()


#created some tables
table1 = canvas_1.create_rectangle(100,100,180,180,fill="brown")
canvas_1.create_text(140,140,text="Table1")
table2 = canvas_1.create_rectangle(260,100,340,180,fill="brown")
canvas_1.create_text(300,140,text="Table2")
table3 = canvas_1.create_rectangle(420,100,500,180,fill="brown")
canvas_1.create_text(460,140,text="Table3")
table4 = canvas_1.create_rectangle(580,100,660,180,fill="brown")
canvas_1.create_text(620,140,text="Table4")

table5 = canvas_1.create_rectangle(100,300,180,380,fill="brown")
canvas_1.create_text(140,340,text="Table5")

table6 = canvas_1.create_rectangle(260,300,340,380,fill="brown")
canvas_1.create_text(300,340,text="Table6")

table7 = canvas_1.create_rectangle(420,300,500,380,fill="brown")
canvas_1.create_text(460,340,text="Table7")

table8 = canvas_1.create_rectangle(580,300,660,380,fill="brown")
canvas_1.create_text(620,340,text="Table8")
# Create a rectangle
car = canvas_1.create_polygon(x1, y1, x3, y3, x2, y2, x4, y4, fill="red")
# car = canvas_1.create_rectangle(250,250,280,280,fill="red")
start_point = canvas_1.create_rectangle(250,250,260,260,fill="black")

root.bind("<Up>",up)
root.bind("<Down>",down)
root.bind("<Right>",right)
root.bind("<Left>",left)
root.bind("<d>", lambda event,a=30:rotate(a))
root.bind("<a>", lambda event,a=-30:rotate(a))

root.bind("<p>",do_seq)
root.bind("<s>",show_data)
root.bind("<r>",reset_data)


root.bind("<w>",stop)

# root.after(1000,stop)
# while True:
#     print("stop")
root.mainloop()