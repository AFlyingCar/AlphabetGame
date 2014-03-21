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

pygame.init()
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

print letters
game = True
numP = 2
exitFlag = True

while True:
	while game:
		for i in range(numP):
			animal = raw_input("What is your animal: ")
			thread.start_new_thread(wait, (exitFlag,))

pygame.quit()

nuclear = u'\u2622'