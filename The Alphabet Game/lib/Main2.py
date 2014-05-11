#Tyler Robbins
#4/1/14
#Main 2
#Main file, runs the neccessary files from def_func

from def_func import *
import os

SCREEN_PATH = os.path.abspath(os.path.join(os.getcwd(),'Screenshots'))

def main():
	#Make sure that screenshots can be saved.
	if not os.path.exists(SCREEN_PATH):
		os.mkdir(SCREEN_PATH)

	os.environ["SDL_VIDEO_CENTERED"] = "1"
	InternetCheck(CLI)
	Start(True)

nuclear = u'\u2622'