class User:

	def __init__(self, name, mailid, mobilenumber):
		self.userName = name
		self.userMailId = mailid
		self.userMobileNumber = mobilenumber

	def getUserName(self):
		return self.userName

	def getUserMailId(self):
		return self.userMailId

	def getUserMobileNumber(self):
		return self.userMobileNumber