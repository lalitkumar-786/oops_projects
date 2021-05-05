class Board:

	def __init__(self):
		self.grid = ["-" for i in range(9)]

	def display(self):
		#print("\t ---- Grid -----")
		print("\t",self.grid[0] + " | " + self.grid[1] + " | " + self.grid[2])
		print("\t",self.grid[3] + " | " + self.grid[4] + " | " + self.grid[5])
		print("\t",self.grid[6] + " | " + self.grid[7] + " | " + self.grid[8])

	def playerMove(self, char):
		pos=int(input("Enter the position inclusive[1,9] \n"))

		if(self.isValid(pos)):
			self.grid[pos-1] = char
		else:
			self.playerMove(char)
			
	
	def flipPlayer(self, name, char):
		print(f"{name}'s turn :{char}")


	def isValid(self, pos):

		if pos-1>8 or pos-1<0:
			print("--> Invalid choice! You can't select out of Board.")
			return False
		elif self.grid[pos-1] != "-":
			print("--> The selected position has been taken. Please select other")
			return False
		else:
			return True

	def isWinner(self, char):

		count = 0

		## check for all rows
		for i in range(0,9):
			if ((i)%3)==0:
				count=0
			if self.grid[i] == char:
				count+=1
				if(count==3):
					return True

		return False

	def isTie(self, char):

		if self.isWinner(char) or self.grid.count('-')==0:
			return True
		else:
			return False
		