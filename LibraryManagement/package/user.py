
class User:
	
	def __init__(self, name, age, mail_id):
		self.name = name
		self.age = age
		self.mail_id = mail_id

	def getUserDetails(self):
		print("\tUser Information: ")
		print("\tName :", self.name)
		print("\tAge :", self.age)
		print("\tMail ID :", self.mail_id)

	def getUsername(self):
		return self.name



