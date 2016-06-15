from urllib2 import urlopen
from json import load

from MovieInfoClass import *

movie_list = []

def fill_movie_data():
	apiUrl = "https://data.sfgov.org/resource/wwmu-gmzc.json"
	response = urlopen(apiUrl)
	json_obj = load(response)
	
	title = ""
	director = ""
	release_year = ""
	actor_1 = ""
	actor_2 = ""
	locations = ""
	for item in json_obj:
		if "title" in item:
			title = item["title"]
			#print title
		if "director" in item:
			director = item["director"]
			#print director
		if "release_year" in item:
			release_year = item["release_year"]
			#print release_year
		if "actor_1" in item:
			actor_1 = item["actor_1"]
			#print actor_1
		if "actor_2" in item:
			actor_2 = item["actor_2"]
			#print actor_2
		if "locations" in item:
			locations = item["locations"]
			#print locations
		movie_to_add = Movie_Info(director, release_year, title, actor_1, actor_2, locations)
		movie_list.append(movie_to_add)

def main():
	fill_movie_data()
	for movie_info in movie_list:
		print "Director: %s." % (movie_info.director)
		print "Title: %s." %(movie_info.title)
		print "Release Year: %s." %(movie_info.release_year)
		print "Actor 1: %s." %(movie_info.actor_1)
		print "Actor 2: %s." %(movie_info.actor_2)
		print "Locations: %s."%(movie_info.locations)

if __name__ == '__main__':
	main()




