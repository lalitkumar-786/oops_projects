# main
from package import user
from package import library


if __name__ == '__main__':

	user = user.User("Lalit", 25, "lalit@gmail.com")
	library = library.Library("CodingStuff",['c++','java','Py'])

	while(True):
		print("\n##################################")
		print("--- Welcome to the library ---")
		print(" Enter your choice ")
		print("1. See user profile")
		print("2. Get lists of books")
		print("3. Add a book")
		print("4. Return a book")
		print("5. Lend a  Book")
		print("6. Get User collections ")

		choice = int(input())
		
		if choice == 1:
			user.getUserDetails()

		elif choice == 2:
			library.getBooks()

		elif choice == 3:
			b=input("Add a book to enter in the database\n")
			library.addBook(b)

		elif choice == 4:
			b=input("Enter the book you want to return \n")
			library.returnBook(user.getUsername(),b)

		elif choice == 5:
			
			b = input("Which book you want: \n")
			library.lendBook(user.getUsername(), b)

		elif choice == 6:

			library.displayUserCollection(user.getUsername())

		else:
			print("Invalid choice. Please try again..")

