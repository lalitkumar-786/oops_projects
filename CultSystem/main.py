from package import activity
from package import cult
from package import user

## For testing purpose
from test.testUserFunctions import testUser
from test.testAdminFunctions import testAdmin

if __name__ == '__main__':
	print("\t------ Welcome ----------")

	## Admin Activity
	u = user.User("lalit", "123456789","lk@gmail.com")

	c = cult.Cult("Bellandur", ["Cardio", "Swimming"])
	c.setActivityTimings("Cardio",['6-7','7-8','8-9'])
	c.setActivityTimings("Swimming",['6-7','10-11','11-12'])
	#c.getActivityTimings()

	testUser(u,c)