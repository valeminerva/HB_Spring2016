"""This program analyses the syntax of a regular SOV-Latin sentence including regular words from the first and second declination."""
# Adapt/change docstring

def sentence():
	sentence = raw_input("Please, type the sentence you want to be analysed.")
	# sentence.split() REALLY NECESSARY? COULD ACCESS STRING DIRECTLY
	print "Thank you. And what would you like to do?"
	menu()

def menu():
	print "1 - Find verb \n 2 - Find Subject \n 3 - Find Object \n 4 - Analyse word \n 5 - Analyse all \n 6 - Exit" 
	user_choice = int(raw_input("Please, type the number of your choice."))
	if user_choice == 1:
		verb()
	elif user_choice == 2:
		subject()
	elif user_choice == 3:
		object()
	elif user_choice == 4:
		word()
	elif user_choice == 5:
		analyse_sentence()
	else exit()

des_pres_ind_1_conj = {"1a pers. sg.": "o", "2a pers. sg.": "s", "3a pers. sg.": "t", "1a pers. pl.": "mus", "2a pers. pl.":"tis", "3a pers. pl.": "nt"}
des_subst_first_decl = {"1a decl. nom. sg.":"a"}
des_subst_second_decl = {}

def verb():
# come accedo a un dictionary definito fuori della funzione?
	for word in sentence:
		for pers in des_pres_ind_1_conj:
			if word[-1:-2] in des_pres_ind_1_conj
	#CHECK: 1) how to access last two idx in string 2) access value at key

def subject():
	pass
	# for che analizzi tutte le parole
	# if / elif :
	# se trova una parola che corrisponde
	# se trova soggetto singolare: continua a cercare: forse due soggetti!
	# se no: il soggetto è implicito o il verbo è impersonale

def object():
	pass

def word():
	word_to_anayse = raw_input("What word do you want me to analyse for you?")

def analyse_sentence():
	verb()
	subject()
	object()

def exit():
	pass
