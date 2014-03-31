#Tyler Robbins
#3/25/14
#Alphabet Test

import sys
from string import *

class player():
	def __init__(self, name=0):
		self.letters = []
		self.name = str(name)

	def addLetter(self, let):
		self.letters.append(let)

	def getLetter(self):
		return self.letters

	def getName(self):
		return self.name

def shutdown():
	sys.exit()

def init(numP):
	players = []
	for i in range(numP):
		name = raw_input("What is Player %d's name: " % i) 
		x = player(name)
		x.attr = i
		players.append(x)

	return players

numP = None

animals = ["cow", "rabbit", "animal", "bunny", "duck", "eagle", "bee", "armadillo", "arch", "asdf"]
guesses = []
game = True
take = False

while not str(numP).isdigit():
	try:
		numP = int(raw_input("How many players: "))
		if numP <= 1:
			print "Too low!"
			numP = None
	except ValueError:
		print "Not a number!"

players = init(numP)

while game:
	for item in letters[:26]:
		take = False

		while not take:
			for i in players:
				if len(i.getLetter()) >= 3:
					players.remove(i)
					players = filter(None, players)

				print "Player %s's turn!" % i.getName()
				guess = raw_input("Choose an animal that starts with the letter '" + item.upper() + "': ")

				if guess.lower() in animals and guess.lower()[0] == item:
					print "That's an animal!"
					guesses.append(guess)

				else:
					print "Take the letter %s!" % i.getName()
					i.addLetter(item)
					guesses = []
					take = True
					continue

		if len(players) == 1:
			break

	print "Player %s is the winner!" % players[0].getName()

	ask = raw_input("Would you like to play again? ")

	if ask.lower() == "y":
		players = init(numP)
	else:
		game = False

shutdown()

nuclear = u'\u2622'