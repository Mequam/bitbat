#!/bin/python
import tkinter as tk
import threading as mt
import random as r
import time as t

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
		self.turnButton = tk.Button(self.buttonFrame, text="End Turn", command=self.EndTurn)
		self.turnButton.pack()
		self.turnButton.bind("<Button-3>", self.bruteForce)
		self.booleanButtontest = tk.BooleanVar
		for i in range(0, self.H*self.W):
		# 	boardvars += [tk.BooleanVar()]
		# 	boardvars[i].set(False)
		# 	#TICTACGRID += [tk.Radiobutton(frame, variable=boardvars[i], value=i).grid(row=divmod(i,H)[1],column=divmod(i,H)[0])]
			self.TICTACGRID += [tk.Radiobutton(self.GameFrame, variable=self.TicVar, value=i, bg="black")]
			self.TICTACGRID[i].grid(row=divmod(i, self.W)[0], column=divmod(i, self.W)[1])

			print(i, "\n", divmod(i,self.H)[1], divmod(i,self.H)[0])

	def EndTurn(self):
		playmove = self.TicVar.get()
		#print(playmove)
		neworder = 0
		if self.playorder is 0:
			#print(self.TICTACGRID[playmove])
			self.TICTACGRID[playmove] = tk.Label(self.GameFrame, text="X", background="red")
			self.TICTACGRID[playmove].grid(row=divmod(playmove, self.W)[0], column=divmod(playmove, self.W)[1])
			#print(self.TICTACGRID[playmove])
			neworder = 1
		if self.playorder is 1:
			#print(self.TICTACGRID[playmove])
			self.TICTACGRID[playmove] = tk.Label(self.GameFrame, text="O", background="blue")
			self.TICTACGRID[playmove].grid(row=divmod(playmove, self.W)[0], column=divmod(playmove, self.W)[1])
			#print(self.TICTACGRID[playmove])
			neworder = 0
		self.playorder = neworder
		#print(self.TICTACGRID)

	def bruteForce(self, event):
		def bruteThread():
			t0 = t.process_time()
			TurnTable = []
			i = 0
			while i < self.W*self.H:
				TurnTable += [i]
				#print(i)
				i += 1
			turn_N = i
			print(turn_N,"turns")
			while i > 0:
				k = r.randint(0, len(TurnTable)-1)
				#print(TurnTable)
				#print("k", k)
				K = TurnTable[k]
				TurnTable.pop(k)
				self.TicVar.set(K)
				#print("K |", K)
				self.EndTurn()
				#print("i:", i)
				#t.sleep(0.5)
				i -= 1
			t1 = t.process_time()
			print(t1-t0, "seconds")
			if t1 == t0:
				print("too fast to measure")
			else:
				print(turn_N/(t1-t0), "turns per second")
		mt.Thread(target=bruteThread).start()


root = tk.Tk()
b = Default(root)
root.mainloop()
