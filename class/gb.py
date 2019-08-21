def checkSame(arr):
	val0 = arr[0]
	for i in range(1,len(arr)):
		if arr[i] != val0:
			#return false if we find any value that does not equal
			return False
	return True
class GameBoard:
	def __init__(self,x=3,y=3):
		self.board = []
		for i in range(0,y):
			self.board.append([])
			for j in range(0,x):
				self.board[i].append(0)

		#we store the x and y variables for error checking la
	def setNode(self,node,xo):
		#make sure that we are not given an invalid index
		if node[0] < len(self.board) and node[1] < len(self.board[0]):
			#parse out the data that we want to use for setting the node	
			if xo.lower() == 'x':
				print('setting ' + str(node) + ' to 1')
				xo = 1
			elif xo.lower() == 'o':
				xo = 2
			elif xo not in [0,1,2]:
				#if we are given data that we do not understand, return false
				return False

			#set the gameboard node based on xo
			self.board[node[1]][node[0]] = xo
			return True
		else:
			#return false if we get an invalid index
			return False
	def checkWin(self):
		for i in range(0,len(self.board)):
			#check the rows
			if 0 not in self.board[i]:
				if 1 in self.board[i] and 2 not in self.board[i]:
					return 1
				else:
					return 2
		for i in range(0,len(self.board[0])):
			#check columns
			
		
		return False

if __name__ == '__main__':
	gb = GameBoard(3,3)
	gb.setNode((0,0),'o')
	gb.setNode((1,0),'o')
	gb.setNode((2,0),'o')
	for row in gb.board:
		print(row)
	print(gb.checkWin())
