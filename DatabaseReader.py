#Tyler Robbins
#3/31/14
#Database Reader
#Read Catalogue of Life XML database

from xml.etree import ElementTree as ET
import urllib2 as u

def read(animal,shutdown):
	if animal == "":
		print "no animal"
		return [False]

	animal = animal.upper()[0] + animal.lower()[1:]
	print animal

	URL = 'http://www.catalogueoflife.org/col/webservice?name=' + animal

	tree = ET.parse(u.urlopen(URL))
	root = tree.getroot()

	for i in root.iter('results'):
		if not i.attrib['error_message'] == "":
			if i.attrib['error_message'] == "No names found":
				print "does not exist"
				return [False]

			else:
				print "An error occured at catalogueoflife.org that we cannot control.\nThe website may be down.\nPlease try again later."
				shutdown()

		if int(i.attrib['total_number_of_results']) == 1 and i.attrib['name'] == animal:
			print "exists"
			return [True]

		if int(i.attrib['total_number_of_results']) >= 2:
			print i.attrib['total_number_of_results']
			print "too general"
			return [False,'gen']

nuclear = u'\u2622'