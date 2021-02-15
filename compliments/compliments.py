#! usr/bin/env python

"""

Setting up recieving a plant name and a complument based on mood

"""
# import numpy as np
import pandas as pd

# GLOBALS: write path to csv *relative to current file (__file__)*
# or you could just write the full path, the this relative mode will
# work even if you install it not in development mode.
CSVPATH = __file__.split(".py")[0] + ".csv"
COMPLIMENTS = pd.read_csv(CSVPATH, dtype="string")

# settings
pd.set_option("display.max_colwidth", 10000)


def compliment_me(mood):
    """
    The compliment_me function returns a compliment based on 1 of three moods: angry, sad, or happy
    """

    sad_compliments = COMPLIMENTS["sad"]
    angry_compliments = COMPLIMENTS["angry"]

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
    plants = COMPLIMENTS["plant"]
    print("Check out this house plant to make you smile: " 
        + plants.sample().to_string(index = False))



if __name__ == "__main__":
    compliment_me(mood = "sad")
    plant_me()
