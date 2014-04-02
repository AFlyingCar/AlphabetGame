import pygame, sys
from pygame.locals import *
from string import *
from DatabaseReader import *
#from Main import *
from color import *
import Menu

class Player():
	def __init__(self, name=0):
		self.letters = []
		self.name = str(name)

	def addLetter(self, let):
		self.letters.append(let)

	def getLetter(self):
		return self.letters

	def getName(self):
		return self.name

def CLI(promptpos, prompt, pos, uinput="",color=GREEN,game=False):
	while True:
		for event in pygame.event.get():
			keycheck(event,game)

			if event.type == KEYDOWN:
				if event.key == K_RETURN:
					display.fill(color)
					print ">> " + uinput
					return uinput

				if event.key == K_BACKSPACE:
					try:
						uinput = uinput[:-1]
						print ">> " + uinput

					except Exception:
						continue

				if event.key == K_ESCAPE:
					continue

				else:
					uinput += event.unicode
					print ">> "+ uinput

		i = fontObj.render(uinput,True,BLACK)

		display.fill(color)
		display.blit(i,pos)

		prompts = {}

		x = 0
		for p in prompt:
			prompts[p] = x
			x += 1

		for p in promptpos:
			num = promptpos.index(p)
			for key in prompts:
				if prompts[key] == num:
					prompts[key] = p

		for item in prompts:
			display.blit(item,prompts[item])

		pygame.display.update()

def Game(game,players):
	guesses = []
	take = False
	TURN = "Player %s's turn!"
	guess = ""
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

					guess = CLI(promptpos, prompt, (prompt[2].get_width(),151))

					if guess.lower().startswith(item) and guess.lower() not in guesses and read(guess)[0]:
						print "That's an animal!"
						guesses.append(guess)

					elif guess.lower() in guesses and guess.lower().startswith(item) and read(guess)[0]:
						x=fontObj.render("That animal has already been said!",True,BLACK)
						display.blit(x,(display.get_width()/2-(x.get_width()/2),display.get_height()/2))
						pygame.display.update()
						pygame.time.delay(2000)

					elif read(guess)[1] == "gen":
						x=fontObj.render("To general, try being more specific.",True,BLACK)
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

nuclear = u'\u2622'