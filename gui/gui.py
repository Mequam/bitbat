#!/bin/python
import tkinter as tk


class Default:

	def __init__(self, master):
		frame = master
		self.H = int(input("height: "))
		self.W = int(input("width: "))
		boardvars = []
		self.playorder = 0
		self.TICTACGRID = []
		self.TicVar = tk.IntVar()
		self.TicVar.set(0)
		# TicTac = tk.Radiobutton(frame, variable=TicVar)
		# TicTac.grid(row=0, column=0)
		self.buttonFrame = tk.Frame(frame)
		self.buttonFrame.grid(row=0)
		self.GameFrame = tk.Frame(frame)
		self.GameFrame.grid(row=1)
		self.turnButton = tk.Button(self.buttonFrame, text="End Turn", command=self.EndTurn).pack()
		self.booleanButtontest = tk.BooleanVar
		for i in range(0, self.H*self.W):
		# 	boardvars += [tk.BooleanVar()]
		# 	boardvars[i].set(False)
		# 	#TICTACGRID += [tk.Radiobutton(frame, variable=boardvars[i], value=i).grid(row=divmod(i,H)[1],column=divmod(i,H)[0])]
			self.TICTACGRID += [tk.Radiobutton(self.GameFrame, variable=self.TicVar, value=i)]
			self.TICTACGRID[i].grid(row=divmod(i, self.W)[0], column=divmod(i, self.W)[1])

			print(i, "\n", divmod(i,self.H)[1], divmod(i,self.H)[0])
	def EndTurn(self):
		playmove = self.TicVar.get()
		print(playmove)
		neworder = 0
		if self.playorder is 0:
			print(self.TICTACGRID[playmove])
			self.TICTACGRID[playmove] = tk.Label(self.GameFrame, text="X")
			self.TICTACGRID[playmove].grid(row=divmod(playmove, self.W)[0], column=divmod(playmove, self.W)[1])
			print(self.TICTACGRID[playmove])
			neworder = 1
		if self.playorder is 1:
			print(self.TICTACGRID[playmove])
			self.TICTACGRID[playmove] = tk.Label(self.GameFrame, text="O")
			self.TICTACGRID[playmove].grid(row=divmod(playmove, self.W)[0], column=divmod(playmove, self.W)[1])
			print(self.TICTACGRID[playmove])
			neworder = 0
		self.playorder = neworder
		print(self.TICTACGRID)

root = tk.Tk()
b = Default(root)
root.mainloop()
