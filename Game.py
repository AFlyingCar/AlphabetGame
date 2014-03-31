import pygame, sys
from pygame.locals import *
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
	pygame.quit()
	sys.exit()

def keycheck(event):
    if event.type == QUIT:
        shutdown()

    if event.type == KEYDOWN:
        print event.unicode

        if event.key == K_ESCAPE:
            shutdown()

def init(numP):
	players = []
	for i in range(numP):
		name = raw_input("What is Player %d's name: " % i)
		x = player(name)
		x.attr = i
		players.append(x)

	return players

def CLI(promptpos, prompt, pos, uinput=""):
	while True:
		for event in pygame.event.get():
			keycheck(event)

			if event.type == KEYDOWN:
				if event.key == K_RETURN:
					display.fill(GREEN)
					print ">> " + uinput
					return uinput

				if event.key == K_BACKSPACE:
					try:
						uinput = uinput[:-1]
						print ">> " + uinput

					except Exception:
						continue

				else:
					uinput += event.unicode
					print ">> "+ uinput

		#print uinput
		i = fontObj.render(uinput,True,BLACK)

		display.fill(GREEN)
		display.blit(i,pos)
		display.blit(prompt[0],promptpos[0])
		display.blit(prompt[1],promptpos[1])
		display.blit(prompt[2],promptpos[2])

		pygame.display.update()

numP = None

animals = ["cow", "rabbit", "animal", "bunny", "duck", "eagle", "bee", "armadillo", "arch", "asdf"]
guesses = []
game = True
take = False
TURN = "Player %s's turn!"
guess = ""
GREEN = (16,119,30)
BLACK = (0,0,0)

while not str(numP).isdigit():
	try:
		numP = int(raw_input("How many players: "))
		if numP <= 1:
			print "Too low!"
			numP = None
	except ValueError:
		print "Not a number!"

players = init(numP)

pygame.init()

display = pygame.display.set_mode((720, 480)) #set screen size
display.fill((GREEN))
pygame.display.set_caption("Animal Game!") #set window caption
fontObj = pygame.font.Font('freesansbold.ttf', 29) #Sent game fonts

while True:
	while game:
		for item in letters[:26]:
			take = False

			while not take:
				for i in players:
					if len(i.getLetter()) >= 3:
						players.remove(i)
						players = filter(None, players)

					prompt = [fontObj.render(TURN % i.getName(), True, BLACK),
					fontObj.render("Choose an animal that starts with the letter '" + item.upper() + "'.", True, BLACK),
					fontObj.render(">>> ", True, BLACK)]
					promptpos=[((display.get_width()/2)-(prompt[0].get_width()/2),0),(0, 125),(0, 151)]

					guess = CLI(promptpos, prompt, pos=(prompt[2].get_width(),151))

					if guess.lower() in animals and guess.lower()[0] == item and guess.lower() not in guesses:
						print "That's an animal!"
						guesses.append(guess)

					elif guess.lower() in guesses and guess.lower() in animals and guess.lower()[0] == item:
						x=fontObj.render("That animal has already been said!",True,BLACK)
						display.blit(x,(display.get_width()/2-(x.get_width()/2),display.get_height()/2))
						pygame.display.update()
						pygame.time.delay(2000)

					else:
						print "Take!"
						x=fontObj.render("Take the letter %s!" % i.getName(),True, BLACK)
						i.addLetter(item)
						guesses = []
						take = True
						display.fill(GREEN)
						display.blit(x,(display.get_width()/2-(x.get_width()/2),display.get_height()/2))
						pygame.display.update()
						pygame.time.delay(2000)
						break

					pygame.display.update()

			if len(players) == 1:
				break

		prompt = [fontObj.render("Player %s is the winner!" % players[0].getName(), True, BLACK),
		fontObj.render("Would you like to play again: ", True, BLACK)]
		promptpos=[(display.get_width()/2-(prompt[0].get_width()/2), 180),(0, display.get_height()/2)]

		ask = CLI(promptpos, prompt, pos=(prompt[1].get_width(),180))

		if ask.lower() == "y":
			players = init(numP)
		else:
			game = False

shutdown()

nuclear = u'\u2622'