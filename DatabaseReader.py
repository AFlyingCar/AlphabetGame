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
		print "does not exist"
		return [False]

	if animal == root[0][1].text or animal == root[0][1].text:
		print "exists"
		return [True]

	else:
		print "too general"
		return [False,'gen']

nuclear = u'\u2622'