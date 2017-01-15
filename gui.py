from logic import new_board, count_by_player, update_board, get_num_player
from Tkinter import *
from Tkinter import Tk, Canvas, Frame, Button
from Tkinter import BOTH, W, NW, SUNKEN, TOP, X, FLAT, LEFT
import os
import time

canvas_width = 400
canvas_height = 600
colors = ("red", "blue")
master = Tk()
master.title("Game of Lives")
w = Canvas(master, width=canvas_width, height=canvas_height)
count = 0
players = 1
board = new_board(20,20)
var = 5

def draw(L):
	for i in range(len(L)):
		for j in range (len(L[0])):
			if (L[i][j] == 0):
                                color = "white"
                        elif (L[i][j] == 1):
                                color = "red"
                        else:
                                color = "blue"
			w.create_rectangle(20*i, 20*j, 20*(i+1), 20*(j+1), fill = color, outline = "black")
	report()

def player(ct):
        global players
        if players == 2:
                if count < var or (count % 2 == 0 and count >= var*2):
                        return "Red"
                else:
                        return "Blue"
        else:
                return "Red"

def reset():
        global board
        global count
        board = new_board(20,20)
        count = 0

def addplayer():
        global players
        reset()
        if players == 2:
                players = 1
                w.create_rectangle(220, 410, 260, 450, fill = "", outline = "white")
                w.create_rectangle(140, 410, 180, 450, fill = "", outline = "black")
        else:
                players = 2
                w.create_rectangle(220, 410, 260, 450, fill = "", outline = "black")
                w.create_rectangle(140, 410, 180, 450, fill = "", outline = "white")
 
                
def click(event):
        global count
        global players
        x = event.x / 20
        y = event.y / 20
        if y >= 20:
                if x >= 0 and x <= 5:
                        update_board(board)
                elif x >= 15 and x <= 20:
                        reset()
                elif x >= 7 and x <= 10:
                        addplayer()
                elif x > 10 and x <= 13:
                        addplayer()
        elif board[x][y] == 0:
                if player(count) == "Red":
                        board[x][y] = 1
                else:
                        board[x][y] = 2
                count += 1
        draw(board)
        if (players == 2):
                endgame(board)
                report()
                
def report():
        global count
	a = 0
	b = 0
	if players == 1:
                w.create_rectangle(0, 460, 400, 500, fill = "white", outline = "white")
        else:
                for i in range(len(board)):
                        for j in range (len(board[0])):
                                if board[i][j] == 1:
                                        a = a + 1
                                if board[i][j] == 2:
                                        b = b + 1
                w.create_rectangle(0, 460, 150, 500, fill = "white", outline = "white")
                w.create_text(75, 480, text = "Red Cells: " + str(a))
                w.create_rectangle(250, 460, 400, 500, fill = "white", outline = "white")
                w.create_text(325, 480, text = "Blue Cells: " + str(b))
                w.create_rectangle(150, 460, 250, 500, fill = "white", outline = "white")
                w.create_text(200, 480, text = player(count) + "'s turn")

def endgame(board):
        row = len(board)
        col = len(board[0])
        if get_num_player(board,1) <= 4 or get_num_player(board,2) >= 20:
                w.create_rectangle(150, 460, 250, 500, fill = "white", outline = "white")
                w.create_text(200, 480, text = "Red wins!")
        elif get_num_player(board,2) <= 4 or get_num_player(board,1) >= 20:
                w.create_rectangle(150, 460, 250, 500, fill = "white", outline = "white")
                w.create_text(200, 480, text = "Blue wins!")
                
        
addplayer()
draw(board)


outlinecol = ["black","white"]
w.bind("<Button-1>", click)
w.pack()
w.create_rectangle(0, 410, 100, 450, fill = "white", outline = "black")
w.create_text(50, 430, text = "update")
w.create_text(160, 430, text = "1P")
w.create_text(240, 430, text = "2P")
w.create_rectangle(300, 410, 400, 450, fill = "white", outline = "black")
w.create_text(350, 430, text = "reset")

message = Label( master, text = "Game of Lives\n\
\n\
\n\
Credits: Dingding Dong, Deqing Fu, Ziqi Ma, Shangxi Zhang " )
message.pack( side = BOTTOM )
mainloop()


