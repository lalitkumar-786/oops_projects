from package import activity

class Cult(activity.Activity):

	def __init__(self, center, activities=[]):
		 super().__init__(activities)
		 """
		 centerName <-- name of the CULT center
		 activityTimings <-- a dictionary containing list of timeslots
		 	eg:-    {
					"Cardio": ["6-7", "7-8" ....]
				 	}

		 userActivities <-- a dictionary containing list of activity with timeSlot
		 	eg:-    {
		 				#Every second el in list will contain TimeSLot
						"user1": ["Swimming","7-8", "cardio","9-10"]
				 	}
		 """
		 self.centerName = center
		 self.activityTimings = {}
		 self.userActivities = {}


	def getActivities(self, center):
		print(f" The following activities are available:")
		print(super().getActivities())


	def setActivityTimings(self, activityName, timings):
		"""
		1. Check if activity exists in that center
		2. Check if any existing timings for that activity.
			If yes, append to that list
			else, create a new list
		"""
		if self.isValidActivity(activityName):
			for time in timings:

				if not self.isActivityEmpty(activityName):
					self.activityTimings.update({activityName:[time]})
				else:
					self.activityTimings.get(activityName).append(time)
		else:
			print("Sorry! Please select only the available activities")


	def getActivityTimings(self):

		print("Following slots are available for the activities:-")

		for a,t in self.activityTimings.items():
			print(f" {a}: {t}")


	def registerForActivity(self, user, activityName,timeSlot):
		"""
		1. Check whether the activity exists
		2. Check whether the user is free in that slot
		3. Book it
		"""

		if self.isValidActivity(activityName):

			if self.isValidTimeSlot(activityName, timeSlot):

				if self.isUserFree(user,timeSlot):
					if user in self.userActivities.keys():
						self.userActivities.get(user).append(activityName)
						self.userActivities.get(user).append(timeSlot)

					else:
						self.userActivities.update({user:[activityName,timeSlot]})

					print(f"Woow! Your slot {timeSlot} has been booked")
				else:

					print(f"Sorry {user}! You have already enrolled to other activity at {timeSlot}")
			else:
				print(f"Sorry! The {timeSlot} entered is not allotted to {activityName}")

		else:
			print(f"Sorry! {activityName} doesn't exist in {self.centerName} center")



	def isUserAlreadyEnrolled(self,user):
		if user in self.userActivities.keys():
			return True
		else:
			return False


	def isUserFree(self, user, timeSlot):
		"""
		1. Checks is user is already enrolled to some other activity
		"""
		if self.isUserAlreadyEnrolled(user):
			curActivities = self.userActivities.get(user)
			if timeSlot in curActivities:
				return False
			else:
				return True
		else:
			return True


	def isValidActivity(self, activityName):

		if activityName in self.listOfActivities:
			return True
		else:
			return False


	def isActivityEmpty(self, activityName):
		if self.activityTimings.get(activityName):
			return True
		else:
			return False


	def isValidTimeSlot(self, activityName, timeSlot):
		if activityName in self.activityTimings.keys():
			if timeSlot in self.activityTimings.get(activityName):
				return True
			else:
				return False


	def listUserActivities(self,user):

		if self.isUserAlreadyEnrolled(user):
			print(f"{user}! Your activities are listed below:")

			curActivities = self.userActivities.get(user)
			for i in range(0,len(curActivities),2):
				print(">>>"+curActivities[i] + " Time: " + curActivities[i+1])

		else:
			print(f"Sorry {user} You have not been enrolled to any activity")


	def deregisterUser(self, user, activityName):

		if self.isUserAlreadyEnrolled(user):
			curActivities = self.userActivities.get(user)

			activityToBeDeleted = curActivities.index(activityName)
			activityTimeToBeDeleted = activityToBeDeleted+1

			self.userActivities.get(user).pop(activityToBeDeleted)
			self.userActivities.get(user).pop(activityTimeToBeDeleted)

			print(f"You have successfully deregistered for {activityName}")

		else:
			print(f"Sorry {user}!. You are not enrolled for any activity")




