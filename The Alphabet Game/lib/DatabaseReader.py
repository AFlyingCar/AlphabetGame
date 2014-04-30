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

	#animal = animal.upper()[0] + animal.lower()[1:]
	animal = animal.lower()
	print animal

	if " " in animal:
		animal = animal.split(" ")
		animal = "%20".join(animal)

	animal += "%20"*(3-len(animal))

	print animal

	URL = 'http://www.catalogueoflife.org/col/webservice?name=' + animal

	if "%20" in animal:
		animal = animal.split("%20")
		animal = " ".join(animal)

	tree = ET.parse(u.urlopen(URL))
	root = tree.getroot()

	for i in root.iter('results'):
		if not i.attrib['error_message'] == "":
			if i.attrib['error_message'] == "No names found":
				print "does not exist"
				return [False]

			else:
				print "An error occurred at catalogueoflife.org that we cannot control.\nThe website may be down.\nPlease try again later."
				return [False, 'err', i.attrib['error_message']]

		if int(i.attrib['total_number_of_results']) == 1 and i.attrib['name'] == animal:
			print "exists"
			return [True]

		if int(i.attrib['total_number_of_results']) >= 2:
			print i.attrib['total_number_of_results']
			print "too general"
			return [False,'gen']

		else:
			print "A fatal error occurred."
			return [False, 'err', 'Generic Error']

if __name__ == "__main__":
	import time
	print "\n\n" + str(read("black bear","foo"))
	time.sleep(2)

nuclear = u'\u2622'