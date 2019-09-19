# -*- coding:utf-8 -*-
'''
    五子棋程序
'''

import tkinter,math,copy
from tkinter import messagebox

# init root
root = tkinter.Tk()
global board
board = [[0 for i in range(19)] for i in range(19)]
global playstep
playstep = 1

def putchess(event):
    global board, playstep
    if event.x > 20 and event.x < 580 and event.y > 20 and event.y < 580:
        i = round((event.x - 30) / 30)
        j = round((event.y - 30) / 30)
        if board[i][j] == 0:
            if playstep % 2 != 0:
                canvas.create_oval(20 + (i * 30), 20 + (j * 30), 40 + (i * 30), 40 + (j * 30), fill='black',tags='stone')
                board[i][j] = playstep % 2
            else:
                canvas.create_oval(20 + (i * 30), 20 + (j * 30), 40 + (i * 30), 40 + (j * 30), fill='white',tags='stone')
                board[i][j] = playstep % 2 + 2
            playstep = playstep + 1
        checkwin()
        computer_think()
def checkwin():
    global board
    for i in range(14):
        for j in range(14):
            if board[i][j]==1 and board[i][j+1]==1 and board[i][j+2]==1 and board[i][j+3]==1 and board[i][j+4]==1 :
               annance_win(1)
            if board[i][j]==2 and board[i][j+1]==2 and board[i][j+2]==2 and board[i][j+3]==2 and board[i][j+4]==2 :
               annance_win(2)
            if board[i][j]==1 and board[i+1][j]==1 and board[i+2][j]==1 and board[i+3][j]==1 and board[i+4][j]==1 :
               annance_win(1)
            if board[i][j]==2 and board[i+1][j]==2 and board[i+2][j]==2 and board[i+3][j]==2 and board[i+4][j]==2 :
               annance_win(2)
            if board[i][j]==1 and board[i+1][j+1]==1 and board[i+2][j+2]==1 and board[i+3][j+3]==1 and board[i+4][j+4]==1:
                annance_win(1)
            if board[i][j]==2 and board[i+1][j+1]==2 and board[i+2][j+2]==2 and board[i+3][j+3]==2 and board[i+4][j+4]==2:
                annance_win(2)
            if board[i+4][j]==1 and board[i+3][j+1]==1 and board[i+2][j+2]==1 and board[i+1][j+3]==1 and board[i][j+4]==1:
                annance_win(1)
            if board[i+4][j]==2 and board[i+3][j+1]==2 and board[i+2][j+2]==2 and board[i+1][j+3]==2 and board[i][j+4]==2:
                annance_win(2)

def annance_win(a):
    if a == 1:
        tkinter.messagebox.askyesno('游戏结束','黑棋获胜,是否再来一盘？')
        newgame()
    if a == 2:
        tkinter.messagebox.askyesno('游戏结束','白棋获胜,是否再来一盘？')
        newgame()

def newgame():
    global board,playstep
    canvas.delete('stone')
    board = [[0 for i in range(19)] for i in range(19)]
    playstep = 1
    computer_think()

def computer_think():
    global board,playstep
    tboard = copy.deepcopy(board)
    tboard[9][9]=2
    for i in range(19):
        for j in range(19):
            tboard[i][j]=tboard[i][j]+checkplace(i,j,1,2,3,4,0,0,0,0)+checkplace(i,j,0,0,0,0,1,2,3,4)+checkplace(i,j,-1,-2,-3,-4,1,2,3,4)+checkplace(i,j,1,2,3,4,1,2,3,4)
    maxnum=0
    for i in range(19):
        for j in range(19):
            if tboard[i][j]>=maxnum and board[i][j]==0:
                maxnum=tboard[i][j]
    t=0
    for i in range(19):
        for j in range(19):
            if tboard[i][j]==maxnum and t==0 and playstep%2 !=0 and board[i][j]==0:
                t=t+1
                board[i][j]=1
                playstep=playstep+1
                canvas.create_oval(20 + (i * 30), 20 + (j * 30), 40 + (i * 30), 40 + (j * 30), fill='black',tags='stone')
    checkwin()
    return

def checkplace(a,b,i1,i2,i3,i4,j1,j2,j3,j4):
    global board
    r=[0,0,0,0,0,0,0,0]
    aa=0
    if a+i1>=0 and b+j1>=0 and a+i1<=18 and b+j1<=18:
        r[4]=board[a+i1][b+j1]
    if a+i2>=0 and b+j2>=0 and a+i2<=18 and b+j2<=18:
        r[5]=board[a+i2][b+j2]
    if a+i3>=0 and b+j3>=0 and a+i3<=18 and b+j3<=18:
        r[6]=board[a+i3][b+j3]
    if a+i4>=0 and b+j4>=0 and a+i4<=18 and b+j4<=18:
        r[7]=board[a+i4][b+j4]
    if a-i1>=0 and b-j1>=0 and a-i1<=18 and b-j1<=18:
        r[3]=board[a-i1][b-j1]
    if a-i2>=0 and b-j2>=0 and a-i2<=18 and b-j2<=18:
        r[2]=board[a-i2][b-j2]
    if a-i3>=0 and b-j3>=0 and a-i3<=18 and b-j3<=18:
        r[1]=board[a-i3][b-j3]
    if a-i4>=0 and b-j4>=0 and a-i4<=18 and b-j4<=18:
        r[0]=board[a-i4][b-j4]
    if r[4:8]==[1,1,1,1] or r[0:4]==[1,1,1,1] or r[3:7]==[1,1,1,1] or r[1:5]==[1,1,1,1] or r[2:6]==[1,1,1,1]:return 10000
    if r[4:8]==[2,2,2,2] or r[0:4]==[2,2,2,2] or r[1:5]==[2,2,2,2] or r[2:6]==[2,2,2,2] or r[3:7]==[2,2,2,2]: return 3000
    if r[2:7]==[0,1,1,1,0] or r[1:6]==[0,1,1,1,0] or r[0:5]==[0,1,1,1,0] or r[3:8]==[0,1,1,1,0]:return 600
    if r[3:8]==[0,2,2,2,0] or r[0:5]==[0,2,2,2,0] or r[2:7]==[0,2,2,2,0] or r[1:6]==[0,2,2,2,0]:return 250
    if r[4:8]==[1,1,1,2] or r[4:8]==[2,2,2,1] or r[0:4]==[2,1,1,1] or r[0:4]==[1,2,2,2]: return -20
    if r[1:4]==[0,1,1] or r[1:4]==[0,2,2] or r[4:7]==[1,1,0] or r[4:7]==[2,2,0]:return 30
    if r[1:4]==[2,1,1] or r[1:4]==[1,2,2] or r[4:7]==[1,1,2] or r[4:7]==[2,2,1]:return -30
    if r[2:4]==[0,1] or r[2:4]==[0,2] or r[4:6]==[1,0] or r[4:6]==[2,0]:return 10
    if r[2:4]==[2,1] or r[2:4]==[1,2] or r[4:6]==[1,2] or r[4:6]==[2,1]:return -10
    if r[3]==1 or r[3]==2 or r[4]==1 or r[4]==2:return 2
    return 0

canvas = tkinter.Canvas(root, width=800, height=600)
for i in range(19):
    canvas.create_line(30, 30 + i * 30, 571, 30 + i * 30)
    canvas.create_line(30 + i * 30, 30, 30 + i * 30, 571)
canvas.pack()
canvas.bind('<Button-1>', putchess)

menu = tkinter.Menu(root)
submenu = tkinter.Menu(menu, tearoff=0)
submenu.add_command(label='New',command=newgame)
menu.add_cascade(label='Game', menu=submenu)
root.config(menu=menu)
computer_think()
root.mainloop()
