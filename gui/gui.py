import tkinter as tk
class Default:
	
	def __init__(self, master):
		frame = master
		H = int(input("height: "))
		W = int(input("width: "))		

		
		for i in range(0, H*W):
			tk.Checkbutton(frame).grid(row=divmod(i,H)[1],column=divmod(i,H)[0])
			print(i, "\n", divmod(i,H)[1], divmod(i,H)[0])
		
root = tk.Tk()
b = Default(root)
root.mainloop()
