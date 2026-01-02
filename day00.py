"""
PYTHON JOURNEY GETTING STARTED

Date: 01/01/2026
Author: Drawts

Description: I know a little bit about Python, however I want to get started so I can better understand
what Python is from scratch, I'll learn by reading books, watching tutorials, gathering information on 
Internet, as well as getting some help from the AI, I'll do my best to keep on track each day by adding 
a pushing commits to the repository and at the same time creating new projects in order to test my knowledge,
It is for me a pleasure to start over again, I'll ensure this is going to be the last time starting over,
I'm writting this down for me to create the first file and add it to the new repository just created.

In case I need to add anything else to the description, I'll do it, in the meantime, I'm gonna finish setting
things up. This first file is gonna include a python code from a source, I'll copy it, however I'm gonna
change it once I got some specific knowledge or even if I have a little bit.

"""

import random
import time

def year2026(knowledge=0, perseverance=0):

    giving_up = False
    mood = ["I'm so good!", "I like this", "Burnout", "AI is better than me", "Imposter syndrome",
            "I don't know anything", "I want to quit", "I have to try", "Now I understand", "I can do it!"]
    
    for day in range(1,365):

        print(f"Day {day} of 2026")
        print(random.choice(mood))

        if giving_up: #This code will NEVER be executed
            raise Exception()
        if day < 365:
            print("Do not deploy to production")

        time.sleep(60 * 60 * 24)

        knowledge += 1
        perseverance += 1

    print(f"You are a {knowledge + perseverance}% better")
    print("YOU CAN DO IT. HAPPY 2026, COMMUNITY!")
    year2026 (knowledge, perseverance)