#Tyler Robbins
#3/31/14
#Main
#Executes the program

from xml.etree import ElementTree as ET
import urllib2 as u
from pygame.locals import *
import pygame,sys,os
from Game import *
from Menu import *
from Init import *
from color import *
from string import *

if __name__ == '__main__':
	pygame.init()

	display = pygame.display.set_mode((720, 480)) #set screen size
	display.fill((WHITE))
	pygame.display.set_caption("Animal Game!") #set window caption
	fontObj = pygame.font.Font('freesansbold.ttf', 29) #Set game fonts

	vars = init(CLI)
	Start(True,vars=vars)

nuclear = u'\u2622'