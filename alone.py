#!/usr/bin/env python

import argparse
import string
import random
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def living():
    l=["people like or unlike you",
       "fish",
       "dinosaurs",
       "wolves",
       "birds",
       "giant insects"]
    return random.choice(l)

def plants():
    l=["towering trees"
       "carnivorous pitchers",
       "giant ferns",
       "glowing weeds",
       "floating flowers",
       "oozing mushrooms"]
    return random.choice(l)

def ruins():
    l=["mysterious obelisks",
       "vine-covered temples",
       "abandoned dwellings for people bigger than you",
       "a wrecked spaceship, etc."]
    return random.choice(l)

def nature():
    l=["huge crystal formations",
       "mirages",
       "vividly colored lightning",
       "strange clouds",
       "rocks eroded in strange shapes",
       "veins of precious metals"]
    return random.choice(l)

what=[{ "label": "living beings", "example": living},
      { "label": "plants or other immobile forms of life", "example": plants},
      { "label": "ruins", "example": ruins },
      { "label": "natural phenomena", "example": nature}]

where=[
    "In a field taller than you",
    "Under the light of the moon(s)",
    "By a gentle river",
    "In a steep canyon",
    "In a treetop",
    "On the snowy peak of a mountain",
    "Near a volcano",
    "On a glacier",
    "Deep underground",
    "On a cliff face",
    "In the desert",
    "In deep water",
    "Floating in the air"]

difficulty=["It was arduous to get to:", "You come upon it suddenly:", "You spot it as you are resting:"]

def main():
    discoveries = random.choice(range(1, 6))
    name = ''.join(random.choice(string.ascii_uppercase) for _ in range(3)) + ''.join(random.choice(string.digits) for _ in range(3)) + "-" + ''.join(random.choice(string.digits) for _ in range(1))
    user_msg = "Planet " + name + '\n'
    user_msg += "(" + str(discoveries) + " discoveries to find)" + '\n'
    for i in range(discoveries):
        subject = random.choice(what)
        diff = random.choice(difficulty)
        user_msg += "Discovery " + str(i + 1) + ":" + '\n'
        user_msg += diff + " " + random.choice(where) + " you discover " + subject["label"] + ", such as " + subject["example"]() + '\n'
        if (i < discoveries - 1):
            user_msg += '\n'

    system_msg = 'The user is a deep space traveler. They are visiting incredibly distant unknown and unnamed worlds. This trip will take them through several words with unique ecosystems. They will share a log of notes from their journey. Describe this log and the planet settings with vibrant language and technical terminology.'
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            { "role": "system", "content": system_msg, },
            { "role": "user", "content": user_msg, },
        ],
    )
    print(completion.choices[0].message.content)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--about', action="store_true", help="About Alone Among the Stars")
    args = parser.parse_args()
    if args.about:
        print("""Alone Among the Stars
By Takuma Okada | noroadhome.itch.io

A solo roleplaying game about exploring fantastic planets

You are a solitary adventurer, hopping from planet to planet exploring. Each
world has unique features for you to discover and record.

In your ship's log, record a short description and your reaction in a few
sentences, and move on to the next discovery. Each time you complete a planet,
give it a name if it needs one, and find a new planet.
""")

    else:
        main()


