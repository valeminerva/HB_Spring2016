import string
import json

def open_file():
	with open("LoremIpsum.txt") as my_file:
		words_list = my_file.read()
	return words_list

def split_words():
	words_list = open_file()
	return words_list.replace(".", "").replace("\xef\xbb\xbf", "").replace(",", "").replace ("\r\n", "").split(" ")

def fix_upper():
	words = split_words()
	words_lower = []
	for i in range(len(words)):
		words[i] = words[i].lower()
		words_lower.append(words[i])
	return words_lower


def count_words():
	words_lower = fix_upper()
	list_words = {}
	for word in words_lower:
		if word not in list_words:
			list_words[word] = 1
		else:
			list_words[word] += 1
	return list_words

def write_dict():
	dictionary = count_words()
	with open("Word_Dictionary.txt", "w") as my_file:
		for key,value in dictionary.items():
			input_str = key + " occurs: " + str(value) + " times \n"
			my_file.write(input_str)
			# my_file.write(value)





split_words()
fix_upper()
count_words()
write_dict()




