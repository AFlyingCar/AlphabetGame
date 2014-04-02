import pygame, sys
from pygame.locals import *
import urllib2 as u
from color import *
from Menu import *
from Game import *

def init(CLI):
	players = []
	numP = None
	y=0

	try:
		u.urlopen("http://www.google.com")

	except Exception as e:
		print e
		print "An internet connection is required to play."
		print "Exiting."
		shutdown()

	while not str(numP).isdigit():
		prompt = [fontObj.render("How many players: ",True,BLACK)]
		numP = CLI([(0, 151)],prompt,[prompt[0].get_width(),151],color=WHITE)

		if str(numP).isdigit():
			numP=int(numP)

		else:
			y+=1
			print "Not a number!"
			if y>=5:
				shutdown()

			display.fill(WHITE)
			x=fontObj.render(numP + " is not a number!",True,BLACK)
			display.blit(x,(display.get_width()/2-(x.get_width()/2),display.get_height()/2))
			pygame.display.update()
			pygame.time.delay(2000)
			continue

		if numP <= 1:
			print "Too low!"
			numP = None

			display.fill(WHITE)
			x=fontObj.render("Sorry, but a minimum of 2 players is required.",True,BLACK)
			display.blit(x,(display.get_width()/2-(x.get_width()/2),display.get_height()/2))
			pygame.display.update()
			pygame.time.delay(2000)

	for i in range(numP):
		prompt = [fontObj.render("What is Player %d's name: "%i,True,BLACK)]
		name = CLI([(0, 151)],prompt,[prompt[0].get_width(),151],color=WHITE)
		x = Player(name)
		x.attr = i
		players.append(x)

	return players

nuclear = u'\u2622'