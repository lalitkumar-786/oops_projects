class Library:

	def __init__(self, name, books):

		self.libraryName = name
		self.listOfBooks = books
		self.lenderDetails = {}


	def addBook(self, book):

		self.listOfBooks.append(book)
		print(f" The Book {book} has been added to the {self.libraryName}")


	def getBooks(self):

		print("The following books are available:")
		for book in self.listOfBooks:
			print(book)


	def displayUserCollection(self, username):

		if(self.lenderDetails.get(username) and len(self.lenderDetails[username])):
			print(f"The User {username} has following books :")

			for book in self.lenderDetails[username]:
				print(book)
		else:
			print(f" No books have been alloted to {username}")


	def returnBook(self, user, book):

		for user,booklist in self.lenderDetails.items():
			for item in booklist:
				if(item == book):
					self.lenderDetails[user].remove(book)
					self.listOfBooks.append(book)
					print(f" Cool! The book-{book} has been added to {self.libraryName}")
					return

		print("Sorry! The book doesn't belong to you.")

	def lendBook(self, username, book):

		# Check if its alloted to some user
		for user,booklist in self.lenderDetails.items():
			for item in booklist:
				if(item == book):
					print(f"Sorry. The book is being used by {user}")
					return

		# Check if Book is there in list of not
		if(not self.checkBookinList(book)):
			print(f"\t Sorry, the book in not available in the Library {self.libraryName}\n")
			return

		# Else allot a book to the user		
		
		if(self.lenderDetails.get(username)):
			self.lenderDetails.get(username).append(book)
		else:
			self.lenderDetails.update({username:[book]})

		#Remove book from list
		self.listOfBooks.remove(book)
		print(f"\t Congrats ! {book} has been alloted to you. Please take it.\n")

	def checkBookinList(self, book):
		
		if book in self.listOfBooks:
			return True
		else:
			return False