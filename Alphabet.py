#####################
#Tyler Robbins		#
#3/14/14			#
#Aphabet Game		#
#####################

import pygame, sys
import threading
import Queue
from pygame.locals import *
from string import *
import thread

GREEN = (16,119,30) #set the color GREEN to a variable
BLACK = (0,0,0)

class myThread(threading.Thread):
    def __init__(self, threadID, name, q, e):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
        self.e = e
    
    def run(self):
        while e:
        	pygame.time.delay(10000)
        	e = False

def wait(e):
	while e:
		pygame.time.delay(10000)
		e = False

def keycheck():
    if event.type == QUIT:
        shutdown()

    if event.type == KEYDOWN:
        print event.unicode

        if event.key == K_ESCAPE:
            shutdown()

def shutdown():
    pygame.quit()
    sys.exit()

pygame.init()

game = True
numP = int(raw_input("How many players: "))
exitFlag = True
guess = ""
turn = True
letter = "a"
letternum = 0
keypress = False
prompt = "Choose an animal that starts with the letter " + letter + ":"
animals = ["cow", "rabbit"]

display = pygame.display.set_mode((640, 480)) #set screen size
display.fill((GREEN))
pygame.display.set_caption("Animal Game!") #set window caption
fontObj = pygame.font.Font('freesansbold.ttf', 29) #Sent game fonts

while True:    
    while game:
        promptdisp = fontObj.render(prompt, True, BLACK)
        
        for event in pygame.event.get():
            keycheck()

        pygame.display.update()

        for i in range(numP):
            while turn:
                print guess
                display.fill(GREEN)
                choice = fontObj.render(">>> " + guess, True, BLACK)
                display.blit(choice, (0,180))
                display.blit(promptdisp, (0, 151))
                
                for event in pygame.event.get():
                    keycheck()

                    if event.type == KEYDOWN:
                        if event.key == K_RETURN:
                            turn = False

                        if event.key == K_BACKSPACE:
                            try:
                                guess = guess[:-1]

                            except Exception:
                                pass

                        else:
                            guess += event.unicode
                
                pygame.display.update()

            for i in animals:
                if str(guess).lower() == str(i).lower():
                    print i
                    print "Correct!"

                else:
                    print animals
                    print i
                    print guess.lower()
                    print "meh, wrong!"
                    shutdown()

            turn = True

shutdown()

nuclear = u'\u2622'