import tkinter as tk
from functions import *

root = tk.Tk()
root.geometry("900x500")

canvas_1 = tk.Canvas(root,bg="grey",width=900,height=500)
canvas_1.pack()

# Rectangle coordinates
x1, y1 = 250, 250
x2, y2 = 280, 280
x3, y3 = x1, y2
x4, y4 = x2, y1

# car = canvas_1.create_rectangle(250,250,280,280,fill="red")
car = canvas_1.create_polygon(x1, y1, x3, y3, x2, y2, x4, y4, fill="red")
start_point = canvas_1.create_rectangle(250,250,260,260,fill="black")

# button.bind("<Button-1>", lambda event, arg1="Hello", arg2="World": my_function(arg1, arg2))

#canvas_1,car
root.bind("<Up>",lambda event, master=canvas_1, item=car: up(master,item))
root.bind("<Down>",lambda event, master=canvas_1, item=car: down(master,item))
root.bind("<Right>",lambda event, master=canvas_1, item=car: right(master,item))
root.bind("<Left>",lambda event, master=canvas_1, item=car: left(master,item))

car = root.bind("<p>",lambda event,root=root,master1=canvas_1,master1_item1=car: do_seq(root,master1,master1_item1))
print(car)
root.bind("<s>",show_data)
root.bind("<r>",reset_data)
root.bind("<w>",lambda event,master=canvas_1,item=car: stop(master,item))

# root.after(1000,stop)
# while True:
#     print("stop")
root.mainloop()

