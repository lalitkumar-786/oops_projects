######################################################
#
# Mini Cult System
#
######################################################

Entities:
1. User: (username, mailId, mobileNumber)

	Methods:
	- Constructor
	- getUsername
	- getMailId
	- getMobileNumber

2. Activity: (listOfActivities=[])

	Methods:
	- Constructor
	- getListOfActivities

3. Cult(Activity): (centerName, listOfActivities=[])

	Methods:
	- Constructor
	- setActivityTimings
	- userActivities