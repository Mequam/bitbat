class GameBoard:
	def __init__(self,x=3,y=3):
		self.board = []
		for i in range(0,y):
			self.board.append([])
			for j in range(0,x):
				self.board[i].append(0)

		#we store the x and y variables for error checking la
	def setNode(self,node,xo):
		if node[0] < len(self.board[0]):

if __name__ == '__main__':
	gb = GameBoard(400,3)	
	for row in gb.board:
		print(row)
