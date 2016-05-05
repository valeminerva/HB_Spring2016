"""HB ex. lecture 8 - code appetizer"""

def coward():

	answer_coward = raw_input("Are you a coward? \n 1 - I am not \n 2 - Yes, I am ")

	if answer_coward == "1":
		print ("Than eat it!")
	else: print ("Bacon will turn you into a real warrior!")



def feel_angels():
	
	answer_feel_angels = raw_input("Do you want to feel like angels are frolicking on your taste buds? \n 1 - yes \n 2 - no \n 3 - yes, but I'm afraid bacon will kill me.")
	
	if answer_feel_angels == "1":
		print ("Eat it!")

	elif answer_feel_angels == "2":
		print ("You've clearly never tasted bacon. Eat it!")

	else: coward()

	if __name__ == '__main__':
		feel_angels()


