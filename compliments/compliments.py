#! usr/bin/env python

"""

Setting up recieving a plant name and a complument based on mood

"""
import numpy as np
import pandas as pd


compliments = pd.read_csv("compliments.csv", dtype = "string")
pd.set_option("display.max_colwidth", 10000)

def compliment_me(mood):
	"""
	The compliment_me function returns a compliment based on 1 of three moods: angry, sad, or happy
	"""

	sad_compliments = compliments["sad"]
	angry_compliments = compliments["angry"]

	if mood == "sad":
		print("I'm sorry to hear that, " + sad_compliments.sample().to_string(index = False))
	elif mood == "happy":
		print("I'm happy you're happy!")
	elif mood == "angry":
		print("We all get angry sometimes, " + str(angry_compliments.sample()))
	
		
def plant_me():
	"""
	Function that returns a randomly selected house plant
	"""
	plants = compliments["plant"]
	print("Check out this house plant to make you smile: " 
		+ plants.sample().to_string(index = False))



if __name__ == "__main__":
	compliment_me(mood = "sad")
	plant_me()
