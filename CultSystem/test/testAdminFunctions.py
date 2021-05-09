from package import activity
from package import cult
from package import user

def testAdmin(u,c):
	## Admin activity
	while True:
		print("\t1. Add a center ")
		print("\t2. Add timeslot for a center")
		print("\t3. List all centers")
		print("\t4. Exit\n-------------------------------\n")

		choice = int(input())

		if choice == 1:
			c.getActivityTimings()

		elif choice == 2:
			activityName = input("Enter the activity name\n")
			timeslot = input("Enter the timeslot\n")
			c.registerForActivity(u.getUserName(),activityName,timeslot)

		elif choice == 3:
			activityName = input("Enter the activity name\n")
			c.deregisterUser(u.getUserName(),activityName)

		elif choice == 4:
			c.listUserActivities(u.getUserName())

		elif choice == 5:
			exit(0)


	