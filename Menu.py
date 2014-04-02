import pygame, sys
from pygame.locals import *
from Game import *
from color import *
from Main import *

class Button():
	def __init__(self, loc, select, name): #all buttons start not selected
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

	def setLoc(self, loc):
		self.loc = loc

def Start(menu,vars=[]):
	display.fill(WHITE)
	startb = button((500, 180), True, "startb")
	optionb = button((500, 250), False, "optionb")
	exitb = button((500, 320), False, "exitb")

	buttons = {1:startb, 2:exitb, 3:optionb}
	selected = 1
	buttons[selected].setSelect(True)

	while menu:
		startdisp = fontObj.render("Start", True, startb.getSelect())
		exitdisp = fontObj.render("Exit", True, exitb.getSelect())
		optiondisp = fontObj.render("Options", True, optionb.getSelect())

		display.blit(startdisp, startb.getLoc())
		display.blit(exitdisp, exitb.getLoc())
		display.blit(optiondisp, optionb.getLoc())

		for event in pygame.event.get():
			if event.type == QUIT:
				shutdown()

			elif event.type == KEYDOWN:
				print selected

				if event.key == K_z: #enter option
					for item in buttons:
						if buttons[item].getChoice():
							print buttons[item].getName() + " has been selected."
							if buttons[item].getName() == "exitb":
								shutdown()

							elif buttons[item].getName() == "optionb":
								Option(True)

							elif buttons[item].getName() == "startb":
								Game(True,vars)

				elif event.key == K_DOWN: #move down through menu
					buttons[selected].setChoice(False)
					if selected == 1:
						selected += 2
					elif selected == 2:
						selected -= 1
					else:
						selected -= 1
					buttons[selected].setChoice(True)
				
				elif event.key == K_UP: #move up through menu
					buttons[selected].setChoice(False)
					if selected == 1:
						selected += 1
					elif selected == 2:
						selected += 1
					else:
						selected -= 2
					buttons[selected].setChoice(True)
		
		for item in buttons:
			print buttons[item].getName(), buttons[item].getChoice()
			buttons[item].setSelect(buttons[item].getChoice())

		pygame.display.update()

	display.fill(WHITE)

def Pause(menu,vars=[]):
	display.fill(WHITE)
	pygame.display.update()

	resumeb = button((500, 180), True, "resumeb")
	optionb = button((500, 250), False, "optionb")
	exitb = button((500, 320), False, "exitb")

	buttons = {1:resumeb, 2:exitb, 3:optionb}
	selected = 1
	buttons[selected].setSelect(True)

	while menu:
		resumedisp = fontObj.render("Resume", True, resumeb.getSelect())
		exitdisp = fontObj.render("Back to Main Menu", True, exitb.getSelect())
		optiondisp = fontObj.render("Options", True, optionb.getSelect())

		exitb.setLoc((display.get_width()-exitdisp.get_width() + 5, 320))

		display.blit(resumedisp, resumeb.getLoc())
		display.blit(exitdisp, exitb.getLoc())
		display.blit(optiondisp, optionb.getLoc())

		for event in pygame.event.get():
			if event.type == QUIT:
				shutdown()

			elif event.type == KEYDOWN:
				print selected

				if event.key == K_z: #enter option
					for item in buttons:
						if buttons[item].getChoice():
							print buttons[item].getName() + " has been selected."
							if buttons[item].getName() == "exitb":
								Start(True)

							elif buttons[item].getName() == "optionb":
								Option(True)

							elif buttons[item].getName() == "resumeb":
								return None

				elif event.key == K_DOWN: #move down through menu
					buttons[selected].setChoice(False)
					if selected == 1:
						selected += 2
					elif selected == 2:
						selected -= 1
					else:
						selected -= 1
					buttons[selected].setChoice(True)
				
				elif event.key == K_UP: #move up through menu
					buttons[selected].setChoice(False)
					if selected == 1:
						selected += 1
					elif selected == 2:
						selected += 1
					else:
						selected -= 2
					buttons[selected].setChoice(True)
		
		for item in buttons:
			print buttons[item].getName(), buttons[item].getChoice()
			buttons[item].setSelect(buttons[item].getChoice())

		pygame.display.update()

	display.fill(WHITE)

def Option(menu,vars=[]):
	display.fill(WHITE)
	pygame.display.update()

	backb = button((500, 180), True, "backb")
	resob = button((500, 250), False, "resob")

	buttons = {1:backb, 2:resob}
	selected = 1
	buttons[selected].setSelect(True)

	while menu:
		backdisp = fontObj.render("Back", True, backb.getSelect())
		resodisp = fontObj.render("Resolution", True, resob.getSelect())

		display.blit(backdisp, backb.getLoc())
		display.blit(resodisp, resob.getLoc())

		for event in pygame.event.get():
			if event.type == QUIT:
				shutdown()

			elif event.type == KEYDOWN:
				print selected

				if event.key == K_z: #enter option
					for item in buttons:
						if buttons[item].getChoice():
							print buttons[item].getName() + " has been selected."
							
							if buttons[item].getName() == "resob":
								Resolution(True)

							elif buttons[item].getName() == "backb":
								return None

				elif event.key == K_DOWN: #move down through menu
					buttons[selected].setChoice(False)
					if selected == 1:
						selected += 1
					else:
						selected -= 1
					buttons[selected].setChoice(True)
				
				elif event.key == K_UP: #move up through menu
					buttons[selected].setChoice(False)
					if selected == 1:
						selected += 1
					else:
						selected -= 1

					buttons[selected].setChoice(True)
		
		for item in buttons:
			print buttons[item].getName(), buttons[item].getChoice()
			buttons[item].setSelect(buttons[item].getChoice())

		pygame.display.update()
	
	display.fill(WHITE)

def Resolution(menu,vars=[]):
	display.fill(WHITE)
	pygame.display.update()

	backb = button((500, 180), True, "backb")
	fullb = button((500, 250), False, "fullb")
	defb = button((500, 320), False, "defb")

	buttons = {1:backb, 2:fullb, 3:defb}
	selected = 1
	buttons[selected].setSelect(True)

	while menu:
		backdisp = fontObj.render("Back", True, backb.getSelect())
		fulldisp = fontObj.render("FullScreen", True, fullb.getSelect())
		defdisp = fontObj.render("Default", True, defb.getSelect())

		display.blit(backdisp, backb.getLoc())
		display.blit(fulldisp, fullb.getLoc())
		display.blit(defdisp, defb.getLoc())

		for event in pygame.event.get():
			if event.type == QUIT:
				shutdown()

			elif event.type == KEYDOWN:
				print selected

				if event.key == K_z: #enter option
					for item in buttons:
						if buttons[item].getChoice():
							print buttons[item].getName() + " has been selected."
							
							if buttons[item].getName() == "fullb":
								return pygame.display.set_mode(FULLSCREEN)

							elif buttons[item].getName() == "backb":
								return pygame.display.set_mode((640,480))

							elif buttons[item].getName() == "defb":
								return True

				elif event.key == K_DOWN: #move down through menu
					buttons[selected].setChoice(False)
					if selected == 1:
						selected += 2
					elif selected == 2:
						selected -= 1
					else:
						selected -= 1
					buttons[selected].setChoice(True)
				
				elif event.key == K_UP: #move up through menu
					buttons[selected].setChoice(False)
					if selected == 1:
						selected += 1
					elif selected == 2:
						selected += 1
					else:
						selected -= 2
					buttons[selected].setChoice(True)
		
		for item in buttons:
			print buttons[item].getName(), buttons[item].getChoice()
			buttons[item].setSelect(buttons[item].getChoice())

		pygame.display.update()

	display.fill(WHITE)

def shutdown():
	pygame.quit()
	sys.exit()

def keycheck(event,game):
    if event.type == QUIT:
        shutdown()

    if event.type == KEYDOWN:
        print event.unicode

        if event.key == K_ESCAPE:
            if game:
            	Pause(True)
            else:
            	shutdown()


nuclear = u'\u2622'