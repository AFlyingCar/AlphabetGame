#Tyler Robbins
#4/6/14
#Def_func
#Holds the definitions for all classes and functions

from string import *
from DatabaseReader import *
import urllib2 as u
from color import *
import pygame,sys,os
from pygame.locals import *
import platform as plat

def capture():
	s_num = 0
	for screen in os.listdir(screen_path):
		s_num = int(screen.split("-")[1].split(".")[0])

	name = 'screenshot-' + str((s_num + 1)) + ".png"
	pygame.image.save(display,os.path.join(screen_path,name))

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
				if event.type == KEYDOWN:
					if event.key == K_F4: #Take a screenshot
						capture()
						
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

				elif event.key == K_F4: #Take a screenshot
					capture()
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

		fps.tick(50)
		fpsdisp = fontObj.render(str(fps.get_fps())[:5] + " fps",True,BLACK)
		display.blit(fpsdisp,(display.get_width()-fpsdisp.get_width(),display.get_height()-fpsdisp.get_height()))

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
				
					fps.tick(50)
					fpsdisp = fontObj.render(str(fps.get_fps())[:5] + " fps",True,BLACK)
					display.blit(fpsdisp,(display.get_width()-fpsdisp.get_width(),display.get_height()-fpsdisp.get_height()))

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

def Start(menu,*args):
	display.fill(WHITE)
	startb = button((500, 180), True, "startb")
	optionb = button((500, 250), False, "optionb")
	creditb = button((500,320), False, "creditb")
	exitb = button((500, 390), False, "exitb")

	BKG = pygame.image.load(os.path.join(os.getcwd().split(SLASH)[0],"Images","StartBKGRD.png"))

	buttons = {1:startb, 4:exitb, 2:optionb, 3:creditb}
	selected = 1
	buttons[selected].setSelect(True)

	while menu:
		display.blit(BKG,(0,0))

		startdisp = fontObj.render("Start", True, startb.getSelect())
		exitdisp = fontObj.render("Exit", True, exitb.getSelect())
		optiondisp = fontObj.render("Options", True, optionb.getSelect())
		creditdisp = fontObj.render("Credits", True, creditb.getSelect())

		display.blit(startdisp, startb.getLoc())
		display.blit(exitdisp, exitb.getLoc())
		display.blit(optiondisp, optionb.getLoc())
		display.blit(creditdisp, creditb.getLoc())

		fps.tick(50)
		fpsdisp = fontObj.render(str(fps.get_fps())[:5] + " fps",True,BLACK)
		display.blit(fpsdisp,(display.get_width()-fpsdisp.get_width(),display.get_height()-fpsdisp.get_height()))

		for event in pygame.event.get():
			if event.type == QUIT:
				shutdown()

			elif event.type == KEYDOWN:
				if event.key == K_RETURN: #enter option
					for item in buttons:
						if buttons[item].getChoice():
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

				elif event.key == K_F4: #Take a screenshot
					capture()
		for item in buttons:
			buttons[item].setSelect(buttons[item].getChoice())

		pygame.display.update()

	display.fill(WHITE)

def Pause(menu,*args):
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

		display.fill(WHITE)
		display.blit(resumedisp, resumeb.getLoc())
		display.blit(exitdisp, exitb.getLoc())
		display.blit(optiondisp, optionb.getLoc())

		fps.tick(50)
		fpsdisp = fontObj.render(str(fps.get_fps())[:5] + " fps",True,BLACK)
		display.blit(fpsdisp,(display.get_width()-fpsdisp.get_width(),display.get_height()-fpsdisp.get_height()))

		for event in pygame.event.get():
			if event.type == QUIT:
				shutdown()

			elif event.type == KEYDOWN:
				if event.key == K_RETURN: #enter option
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

				elif event.key == K_F4: #Take a screenshot
					capture()
		for item in buttons:
			buttons[item].setSelect(buttons[item].getChoice())

		pygame.display.update()

	display.fill(WHITE)

def Option(menu,*args):
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

		display.fill(WHITE)
		display.blit(backdisp, backb.getLoc())
		display.blit(resodisp, resob.getLoc())

		fps.tick(50)
		fpsdisp = fontObj.render(str(fps.get_fps())[:5] + " fps",True,BLACK)
		display.blit(fpsdisp,(display.get_width()-fpsdisp.get_width(),display.get_height()-fpsdisp.get_height()))

		for event in pygame.event.get():
			if event.type == QUIT:
				shutdown()

			elif event.type == KEYDOWN:
				if event.key == K_RETURN: #enter option
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

				elif event.key == K_F4: #Take a screenshot
					capture()
		for item in buttons:
			buttons[item].setSelect(buttons[item].getChoice())

		pygame.display.update()
	
	display.fill(WHITE)

def Resolution(menu,*args):
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

		display.fill(WHITE)
		display.blit(backdisp, backb.getLoc())
		display.blit(fulldisp, fullb.getLoc())
		display.blit(defdisp, defb.getLoc())

		fps.tick(50)
		fpsdisp = fontObj.render(str(fps.get_fps())[:5] + " fps",True,BLACK)
		display.blit(fpsdisp,(display.get_width()-fpsdisp.get_width(),display.get_height()-fpsdisp.get_height()))

		for event in pygame.event.get():
			if event.type == QUIT:
				shutdown()

			elif event.type == KEYDOWN:

				if event.key == K_RETURN: #enter option
					for item in buttons:
						if buttons[item].getChoice():							
							if buttons[item].getName() == "fullb":
								info = pygame.display.Info()
								return pygame.display.set_mode((info.current_w,info.current_h), FULLSCREEN)

							elif buttons[item].getName() == "backb":
								display.fill(WHITE)
								return True

							elif buttons[item].getName() == "defb":
								return pygame.display.set_mode((720,480))

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

				elif event.key == K_F4: #Take a screenshot
					capture()
		for item in buttons:
			buttons[item].setSelect(buttons[item].getChoice())

		pygame.display.update()

	display.fill(WHITE)

def Credits(menu):
	display.fill(WHITE)
	credit = open(os.path.join("lib","CREDITS.TXT"), "r").read().split("\n")
	creditList = []
	credits = {}
	posy = display.get_height()
	num = 1
	items = 0

	for i in credit:
		creditList.append(fontObj.render(i,True,BLACK))

	for i in creditList:
		credits[num] = [i,posy+(num*i.get_height())]
		num += 1
		items += 1

	while menu:
		display.fill(WHITE)

		for event in pygame.event.get():
			if event.type == QUIT:
				shutdown()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					return None

				elif event.key == K_F4: #Take a screenshot
					capture()
		for i in credits:
			credits[i][1]-=1
		
		for i in credits:
			posx = display.get_width()/2 - credits[i][0].get_width()/2
			posy -= 1
			display.blit(credits[i][0], (posx,credits[i][1]))

		if credits[items][1] <= 0-credits[items][0].get_height():
			menu = False

		fps.tick(50)

		pygame.display.update()

	display.fill(WHITE)

def shutdown():
	pygame.mouse.set_visible(0)
	pygame.quit()
	sys.exit()

def keycheck(event,game,*args):
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

pygame.init()

display = pygame.display.set_mode((720, 480)) #set screen size
display.fill((WHITE))
pygame.display.set_caption("Animal Game!") #set window caption
fontObj = pygame.font.Font('freesansbold.ttf', 29) #Set game fonts
fps = pygame.time.Clock()
pygame.mouse.set_visible(0)

if plat.system == "Windows": SLASH = "\\"
else: SLASH = "//"

c_path = os.getcwd()
screen_path = os.path.abspath(os.path.join(c_path,'Screenshots'))
print screen_path

nuclear = u'\u2622'