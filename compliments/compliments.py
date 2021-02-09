#! usr/bin/env python

"""

a function that gives a compliment or not based on your mood

"""
import random

sad_compliments = [
	"you are kind!",
	"you are beautiful!",
	"you are smart!",
	"your friends love you!"
]

angry_compliments = [
	"take three deep breaths and know you are loved",
	"go for a walk and think of sunflowers",
	"do you need a hug?"
]

def compliment_me(arg):
	if arg == "sad":
		print("I'm sorry to hear that, " + random.choice(sad_compliments))
	elif arg == "happy":
		print("I'm happy you're happy!")
	elif arg == "angry":
		print("We all get angry sometimes, " + random.choice(angry_compliments))

if __name__ == "__main__":
	compliment_me("angry")
	compliment_me("sad")
	compliment_me("happy")