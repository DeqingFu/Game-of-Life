from logic import new_board, count, update_board
from appJar import gui
from Tkinter import *
from Tkinter import Tk, Canvas, Frame, Button
from Tkinter import BOTH, W, NW, SUNKEN, TOP, X, FLAT, LEFT

canvas_width = 400
canvas_height = 400
colors = ("red", "blue")
master = Tk()
master.title("Game of Life")
w = Canvas(master, width=canvas_width, height=canvas_height)

# app=gui()


board = new_board(20,20)

def draw(L):
	for i in range(len(L)):
		for j in range (len(L[0])):
			if (L[i][j] == 0):
				w.create_rectangle(20*i, 20*j, 20*(i+1), 20*(j+1), fill = "red", outline = "black")
			else:
				w.create_rectangle(20*i, 20*j, 20*(i+1), 20*(j+1), fill = "blue", outline = "black")

def flip(event):
	x = event.x / 20
	y = event.y / 20
	if (board[x][y] == 0):
		board[x][y] = 1
	draw(board)

def handlekey(event):
	update_board(board)
	draw(board)

w.bind("<Button-2>", handlekey)
w.bind("<Button-1>", flip)
w.pack()

message = Label( master, text = "Press the mouse to draw" )
message.pack( side = BOTTOM )

mainloop()

# add a button
# app.addButton("One", update_board)

# app.go()

# function called by pressing the buttons
#def press(btn):
#    if btn=="Cancel":
#        app.stop()
#    else:
#        print("User:", app.getEntry('user'), "Pass:", app.getEntry('pass'))
