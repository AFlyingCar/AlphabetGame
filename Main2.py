#Tyler Robbins
#4/1/14
#Main 2
#Because importing from custom modules isn't working.

from xml.etree import ElementTree as ET
import urllib2 as u
from pygame.locals import *
import pygame,sys,os
from string import *
from DatabaseReader import *

GREEN = (16,119,30)
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (171,162,162)

def InternetCheck(CLI):
	display.fill(WHITE)

	try:
		u.urlopen("http://www.google.com")
	except Exception as e:
		print e
		print "An internet connection is required to play."
		print "Exiting."

		display.fill(WHITE)
		
		disp=[fontObj.render("An internet connection is required to play.",True,BLACK),
		fontObj.render("Exiting.",True,BLACK)]

		x = 0
		
		for i in disp:
			x += (i.get_height() + 10)
			display.blit(i,(display.get_width()/2-(i.get_width()/2),display.get_height()/2+x))
			pygame.display.update()

			for event in pygame.event.get():
				keycheck(event,True)

			pygame.time.delay(1000)

		display.fill(WHITE)

		prompt = [fontObj.render("Press any key to continue.",True,BLACK)]
		x=(display.get_width()/2)-(prompt[0].get_width()/2)
		y=(display.get_height()/2)-(prompt[0].get_height()/2)
		promptpos=[(x,y)]

		ask = CLI(promptpos, prompt, ((display.get_width()/2)-(prompt[0].get_width()/2),(display.get_height()/2)+prompt[0].get_height()),color=WHITE)

		shutdown()

class Player():
	def __init__(self, name=0):
		self.letters = []
		self.name = str(name)
		self.turn = False

	def addLetter(self, let):
		self.letters.append(let)

	def getLetter(self):
		return self.letters

	def getName(self):
		return self.name

	def setTurn(self,turn):
		self.turn = turn

	def getTurn(self):
		return self.turn

def CLI(promptpos,prompt,pos,uinput="",color=GREEN,game=False):
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
						continue

					except Exception:
						continue

				if event.key == K_ESCAPE or event.key == K_TAB:
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
			print "next letter"

			while not take:
				for i in players:
					print "next turn"
					if i.getTurn():
						prompt = [fontObj.render(TURN % i.getName(), True, BLACK),
						fontObj.render("Choose an animal that starts with the letter '" + item.upper() + "'.", True, BLACK),
						fontObj.render(">>> ", True, BLACK)]
						promptpos=[((display.get_width()/2)-(prompt[0].get_width()/2),0),(0, 125),(0, 151)]

						guess = CLI(promptpos, prompt, (prompt[2].get_width(),151),game=True)

						if guess.lower().startswith(item) and guess.lower() not in guesses and read(guess,shutdown)[0]:
							print "That's an animal!"
							guesses.append(guess)
							x=fontObj.render(guess + " is an animal!",True,BLACK)
							display.blit(x,(display.get_width()/2-(x.get_width()/2),display.get_height()/2))
							pygame.display.update()
							pygame.time.delay(2000)

							if players.index(i) == len(players)-1:
								players[0].setTurn(True)
							else:
								players[players.index(i)+1].setTurn(True)

							players[players.index(i)].setTurn(False)

						elif guess.lower() in guesses and guess.lower().startswith(item) and read(guess,shutdown)[0]:
							x=fontObj.render("That animal has already been said!",True,BLACK)
							display.blit(x,(display.get_width()/2-(x.get_width()/2),display.get_height()/2))
							pygame.display.update()
							pygame.time.delay(2000)

						elif len(read(guess,shutdown)) >= 2:
							if read(guess,shutdown)[1] == "gen":
								x=fontObj.render("To general, try being more specific.",True,BLACK)
								display.blit(x,(display.get_width()/2-(x.get_width()/2),display.get_height()/2))
								pygame.display.update()
								pygame.time.delay(2000)

						elif not guess.lower().startswith(item):
							x=fontObj.render("That does not start with " + item + "!",True,BLACK)
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

							if players.index(i) == len(players)-1:
								players[0].setTurn(True)
							else:
								players[players.index(i)+1].setTurn(True)

							players[players.index(i)].setTurn(False)
							break

						pygame.display.update()

					if len(i.getLetter()) >= 3:
						players.remove(i)
						players = filter(None, players)

					if len(players) == 1: break

			if len(players) == 1: break

		prompt = [fontObj.render("Player %s is the winner!" % players[0].getName(), True, BLACK),
		fontObj.render("Would you like to play again: ", True, BLACK)]
		promptpos=[(display.get_width()/2-(prompt[0].get_width()/2), 180),(0, display.get_height()/2)]

		ask = CLI(promptpos, prompt, pos=(prompt[1].get_width(),180))

		if ask.lower() == "y":
			players = init(numP)
		else:
			game = False

class button():
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
	creditb = button((500,320), False, "creditb")
	exitb = button((500, 390), False, "exitb")

	buttons = {1:startb, 4:exitb, 2:optionb, 3:creditb}
	selected = 1
	buttons[selected].setSelect(True)

	while menu:
		startdisp = fontObj.render("Start", True, startb.getSelect())
		exitdisp = fontObj.render("Exit", True, exitb.getSelect())
		optiondisp = fontObj.render("Options", True, optionb.getSelect())
		creditdisp = fontObj.render("Credits", True, creditb.getSelect())

		display.blit(startdisp, startb.getLoc())
		display.blit(exitdisp, exitb.getLoc())
		display.blit(optiondisp, optionb.getLoc())
		display.blit(creditdisp, creditb.getLoc())

		for event in pygame.event.get():
			if event.type == QUIT:
				shutdown()

			elif event.type == KEYDOWN:
				if event.key == K_z: #enter option
					for item in buttons:
						if buttons[item].getChoice():
							#print buttons[item].getName() + " has been selected."
							if buttons[item].getName() == "exitb":
								shutdown()

							elif buttons[item].getName() == "optionb":
								Option(True)

							elif buttons[item].getName() == "startb":
								p = get_players(CLI)
								Game(True,p)

							elif buttons[item].getName() == "creditb":
								Credits(True)

				elif event.key == K_DOWN: #move down through menu
					buttons[selected].setChoice(False)
					if selected == 1:
						selected = 2
					elif selected == 2:
						selected = 3
					elif selected == 3:
						selected = 4
					elif selected == 4:
						selected = 1
					buttons[selected].setChoice(True)
				
				elif event.key == K_UP: #move up through menu
					buttons[selected].setChoice(False)
					if selected == 1:
						selected = 4
					elif selected == 2:
						selected = 1
					elif selected == 3:
						selected = 2
					elif selected == 4:
						selected = 3
					buttons[selected].setChoice(True)
		
		for item in buttons:
			buttons[item].setSelect(buttons[item].getChoice())

		pygame.display.update()

	display.fill(WHITE)

def Pause(menu,vars=[]):
	display.fill(WHITE)
	pygame.display.update()

	resumeb = button((500, 180), True, "resumeb")
	optionb = button((500, 250), False, "optionb")
	exitb = button((500, 320), False, "exitb")

	buttons = {1:resumeb, 3:exitb, 2:optionb}
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
				if event.key == K_z: #enter option
					for item in buttons:
						if buttons[item].getChoice():
							if buttons[item].getName() == "exitb":
								Start(True)

							elif buttons[item].getName() == "optionb":
								Option(True)

							elif buttons[item].getName() == "resumeb":
								return None

				elif event.key == K_DOWN: #move down through menu
					buttons[selected].setChoice(False)
					if selected == 1:
						selected = 2
					elif selected == 2:
						selected = 3
					elif selected == 3:
						selected = 1
					buttons[selected].setChoice(True)
				
				elif event.key == K_UP: #move up through menu
					buttons[selected].setChoice(False)
					if selected == 1:
						selected = 3
					elif selected == 2:
						selected = 1
					elif selected == 3:
						selected = 2
					buttons[selected].setChoice(True)
		
		for item in buttons:
			buttons[item].setSelect(buttons[item].getChoice())

		pygame.display.update()

	display.fill(WHITE)

def Option(menu,vars=[]):
	display.fill(WHITE)
	pygame.display.update()

	backb = button((500, 180), True, "backb")
	resob = button((500, 250), False, "resob")

	buttons = {2:backb, 1:resob}
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
				if event.key == K_z: #enter option
					for item in buttons:
						if buttons[item].getChoice():							
							if buttons[item].getName() == "resob":
								Resolution(True)
								display.fill(WHITE)

							elif buttons[item].getName() == "backb":
								display.fill(WHITE)
								return None

				elif event.key == K_DOWN: #move down through menu
					buttons[selected].setChoice(False)
					if selected == 1:
						selected = 2
					elif selected == 2:
						selected = 1
					buttons[selected].setChoice(True)
				
				elif event.key == K_UP: #move up through menu
					buttons[selected].setChoice(False)
					if selected == 1:
						selected = 2
					elif selected == 2:
						selected = 1
					buttons[selected].setChoice(True)
		
		for item in buttons:
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

				if event.key == K_z: #enter option
					for item in buttons:
						if buttons[item].getChoice():							
							if buttons[item].getName() == "fullb":
								return pygame.display.set_mode((640,480), FULLSCREEN)

							elif buttons[item].getName() == "backb":
								display.fill(WHITE)
								return True

							elif buttons[item].getName() == "defb":
								return pygame.display.set_mode((640,480))

				elif event.key == K_DOWN: #move down through menu
					buttons[selected].setChoice(False)
					if selected == 1:
						selected = 2
					elif selected == 2:
						selected = 3
					elif selected == 3:
						selected = 1
					buttons[selected].setChoice(True)
				
				elif event.key == K_UP: #move up through menu
					buttons[selected].setChoice(False)
					if selected == 1:
						selected = 3
					elif selected == 2:
						selected = 1
					elif selected == 3:
						selected = 2
					buttons[selected].setChoice(True)
		
		for item in buttons:
			buttons[item].setSelect(buttons[item].getChoice())

		pygame.display.update()

	display.fill(WHITE)

def Credits(menu):
	display.fill(WHITE)
	credit = open("CREDITS.TXT", "r").read().split("\n")
	credits = []
	posy = display.get_height()

	for i in credit:
		credits.append(fontObj.render(i,True,BLACK))

	for i in range(len(credits)): prev = 5 * i

	while menu:
		display.fill(WHITE)
		
		for i in credits:
			posx = display.get_width()/2 - i.get_width()/2
			display.blit(i, (posx,posy + prev))
			prev += i.get_height()
			pygame.display.update()
			pygame.time.delay(100)

			if posy - prev <= 0:
				credits.remove(i)

			filter(None,credits)

		if len(credits) == 0:
			menu = False

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

def get_players(CLI):
	players = []
	numP = None
	y=0

	while not str(numP).isdigit():
		prompt = [fontObj.render("How many players: ",True,BLACK)]
		numP = CLI([(0, 151)],prompt,[prompt[0].get_width(),151],color=WHITE,game=True)

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

	players[0].setTurn(True)

	return players

if __name__ == '__main__':
	pygame.init()

	display = pygame.display.set_mode((720, 480)) #set screen size
	display.fill((WHITE))
	pygame.display.set_caption("Animal Game!") #set window caption
	fontObj = pygame.font.Font('freesansbold.ttf', 29) #Set game fonts

	InternetCheck(CLI)

	Start(True)

nuclear = u'\u2622'