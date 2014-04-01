#Tyler Robbins
#3/31/14
#Database Reader
#Read Catalogue of Life XML database

from xml.etree import ElementTree as ET
import urllib2 as u

def read(animal):
	animal = animal.upper()[0] + animal.lower()[1:]
	print animal

	URL = 'http://www.catalogueoflife.org/col/webservice?name=' + animal

	tree = ET.parse(u.urlopen(URL))
	root = tree.getroot()

	try:
		print root[0][1].text
	except IndexError:
		print "Too general!"
		return [False,'gen']

	if animal == root[0][1].text:
		print "exists!"
		return [True]
	else:
		print "does not exist"
		return [False]

read("aPuS")

nuclear = u'\u2622'