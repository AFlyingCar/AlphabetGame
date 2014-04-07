#Tyler Robbins
#4/1/14
#Main 2
#Main file, runs the neccessary files from def_func

from def_func import *
import os

def main():
	os.environ["SDL_VIDEO_CENTERED"] = "1"
	InternetCheck(CLI)
	Start(True)

nuclear = u'\u2622'