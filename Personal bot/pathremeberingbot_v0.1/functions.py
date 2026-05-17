from time import *
import sys
#varibles i need
# state = -1
pause = 1
index = -1
# count = 0
'''The maximum size of an array on an arduino is 32767 bytes'''
'''one int = 2byte => 16,383.5 ints we can u '''
seq_move = [-1 for i in range(700)]
# seq_time = [-1 for i in range(4)]
# st_time = int(time()*1000)

sleep_time = 0.055 #the constant speed


#--record movements----#
def stop(master,item):
    global index
    # while pause:
    #     root.update()
    #     sleep(0.5)
    print(f'index={index}')
    index +=1
    seq_move[index] = 0
    go_stop(master,item)

def up(master,item):
    global index,pause
    # pause=0
    print(f'index={index}')
    index +=1
    seq_move[index] = 1
    go_forward(master,item)    

def down(master,item):
    global index
    print(f'index={index}')
    index +=1
    seq_move[index] = 2
    go_backward(master,item)
        
def right(master,item):
    global index
    print(f'index={index}')
    index +=1
    seq_move[index] = 3
    go_right(master,item)
    
def left(master,item):
    global index
    print(f'index={index}')
    index +=1
    seq_move[index] = 4
    go_left(master,item)

'''--------------------------------------------'''    

#------do movements-------------
def go_stop(master,item):
    print("go_stop")

def go_forward(master,item):
    global pause
    print("go_forward")
    x=0
    y=-5
    master.move(item,x,y)
    # master.move(car,x,y)
    # pause = 1
    # stop()

def go_backward(master,item):
    print("go_backward")
    x=0
    y=5
    master.move(item,x,y)
    # canvas_1.move(car,x,y)

def go_right(master,item):
    print("go_right")
    x=5
    y=0
    # canvas_1.move(car,x,y)
    master.move(item,x,y)

def go_left(master,item):
    print("go_left")
    x=-5
    y=0
    # canvas_1.move(car,x,y)
    master.move(item,x,y)

'''-------------------------------------------------'''


def do_seq(root,master1,master1_item1):
    # global car
    master1.delete(master1_item1)
    master1_item1 = master1.create_rectangle(250,250,280,280,fill="red")
    root.update()
    # start_time = int(time()*1000)
    # print(f'start_time={start_time}')
    print("\ndo_seq starts in 3sec\n")
    print("Playing in 3s...")
    sleep(3)
    # rng = len(seq_move)
    # print(rng)
    '''
    actual correct sequence symbols: 1 for forward, 2 for backward, 3 for right, 4 for left, 0 for stop
    '''
    for i in seq_move:
        # current_time = int(time()*1000)-start_time
        sleep(sleep_time)
        if i == 1:
                go_forward(master1,master1_item1)
        elif i == 2:
                go_backward(master1,master1_item1)
        elif i == 3:
                go_right(master1,master1_item1)
        elif i == 4:
                go_left(master1,master1_item1)
        elif i == 0:
            go_stop(master1,master1_item1)
            # print("stop")
            # break
        else:
            root.update()
            break
        root.update()
    print("Playing ENDED.")
    print("Starting retracting in 3sec...")
    sleep(3)
    for i in range(index,-1,-1):
        sleep(sleep_time)
        if seq_move[i] == 1:
                go_backward(master1,master1_item1)
        elif seq_move[i] == 2:
                go_forward(master1,master1_item1)
        elif seq_move[i] == 3:
                go_left(master1,master1_item1)
        elif seq_move[i] == 4:
                go_right(master1,master1_item1)
        elif seq_move[i] == 0:
            go_stop(master1,master1_item1)
            # print("stop")
            # break
        else:
            root.update()
            break
        root.update()
    print("retracing ENDED.")
    # return master1_item1
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