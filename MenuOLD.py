#Tyler Robbins
#3/31/14
#Menu Test
#Define the behaviors of the menus

import pygame, sys
from pygame.locals import *

WHITE = (255,255,255) #set the color WHITE to a variable
BLACK = (0,0,0) #set the color BLACK to a variable
GRAY = (171,162,162) #set the color GRAY to a variable

class button():
	def __init__(self, loc, select, name): #all button start not self.selected
		self.bcolor = GRAY
		self.select = select
		self.name = name
		self.loc = loc

	def getSelect(self):
		return self.bcolor
		
	def setSelect(self, select):
		if select:
			self.bcolor = BLACK
		else:
			self.bcolor = GRAY

	def setChoice(self, pressed):
		self.select = pressed

	def getChoice(self):
		return self.select

	def getName(self):
		return self.name

	def getLoc(self):
		return self.loc

class Menu():
	def __init__(self, name, buttons,bpos=[],names=[]):
		self.buttonum = buttons
		self.buttonObjs = {}
		self.selected = 1
		for i in range(buttons):
			x = button(bpos[i],False,names[i])
			x.attr = i
			self.buttonObjs[i] = x
		self.buttonObjs[0].setChoice(True)

	def draw(self):
		######Draws buttons to the screen######
		for i in self.buttonObjs:
			x = fontObj.render(self.buttonObjs[i].getName(), True, self.buttonObjs[i].getSelect())
			display.blit(x,self.buttonObjs[i].getLoc())

		pygame.display.update()

	def keys(self):
		######Check for keypresses######
		for event in pygame.event.get():
			keycheck(event)

			if event.type == KEYDOWN:
				print "keydown"

				if event.key == K_z: #enter option
					print "z"
					for item in self.buttonObjs:
						return item

				elif event.key == K_DOWN: #move down through menu
					self.buttonObjs[self.selected].setChoice(False)
					if self.selected == 1:
						self.selected += 2
					elif self.selected == 2:
						self.selected -= 1
					else:
						self.selected -= 1
					self.buttonObjs[self.selected].setChoice(True)
				
				elif event.key == K_UP: #move up through menu
					self.buttonObjs[self.selected].setChoice(False)
					if self.selected == 1:
						self.selected += 1
					elif self.selected == 2:
						self.selected += 1
					else:
						self.selected -= 2
					self.buttonObjs[self.selected].setChoice(True)

		for item in self.buttonObjs:
			print self.buttonObjs[item].getName(), self.buttonObjs[item].getChoice()
			self.buttonObjs[item].setSelect(self.buttonObjs[item].getChoice())

	def getButton(self):
		return self.buttonObjs

def StartMenu(menu=True):
	start = Menu("start",3,[(500,180),(500,250),(500,320)],["Start","Options","Exit"])
	start.draw()
	buttons = start.getButton()
	while menu:
		item = start.keys()
		if buttons[item].getChoice():
			print buttons[item].getName() + " has been selected."
			if buttons[item].getName() == "exitb":
				print "closing"
				shutdown()

			elif buttons[item].getName() == "optionb":
				print "options"

			elif buttons[item].getName() == "startb":
				print "starting game!"
				menu=False

def keycheck(event):
    if event.type == QUIT:
        shutdown()

    if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            shutdown()

def shutdown():
	pygame.quit()
	sys.exit()

pygame.init()

display = pygame.display.set_mode((720, 480)) #set screen size
display.fill((WHITE))
pygame.display.set_caption("Menu!") #set window caption
fontObj = pygame.font.Font('freesansbold.ttf', 29) #Set game fonts

StartMenu()

nuclear = u'\u2622'