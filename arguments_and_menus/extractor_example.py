# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import sys, getopt, os

class Person(object):
	def __init__(self, id, vorname, name, zusage, vegetarier):
		self.id = id
		self.vorname = vorname
		self.name = name
		self.zusage = zusage
		self.vegetarier = vegetarier
		

class Invitation(object):
	def __init__(self, id, anrede, fest, registered, persons):
		self.id = id
		self.anrede = anrede
		self.fest = fest
		self.registered = registered
		self.persons = persons

def loadXML(path):
	tree = ET.parse(path)
	root = tree.getroot()
	invitations = []
	
	for element in root.getiterator('entry'):
		for value in element.getiterator('value'):
			persons = []
			for person in value.getiterator('Eingeladene_Person'):
				persons.append(Person(person.find('ID').text,\
				person.find('Name').text, person.find('Vorname').text,\
				person.find('Zusage').text, person.find('Vegetarier').text))
			
			invitations.append(Invitation(value.find('ID').text, value.find('Anrede').text, value.find('Einladung_mit_Fest').text, value.find('Registration_Finished').text, persons))
	
	return invitations


def writeGuestsToOutputCSV(invitations, outputfile):
	myfile=open(outputfile, 'w')
	mystr=','.join(['ID','Einladung_mit_Fest','Registration_Finished','Vorname','Name','Zusage','Vegetarier']) + '\n'
	myfile.write(mystr.encode('mac_roman'))
	for i in invitations:
		for p in i.persons:
			mystr=','.join([p.id, i.fest, i.registered, p.vorname, p.name, p.zusage, p.vegetarier]) + '\n'
			mystr=mystr.replace('true', 'WAHR').replace('false', 'FALSCH')
			myfile.write(mystr.encode('iso-8859-1'))
	
	myfile.close()


def main(argv):
	usage='usage: test.py -i <inputfile> -o <outputfile>'
	inputfile = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print usage
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print usage
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
	
	if inputfile=="" or outputfile=="":
		print usage
		sys.exit(2)
	
	if not os.path.isfile(inputfile):
		print 'Input file does not exist:%s' % (inputfile)
		sys.exit(3)
	
	print 'start reading xml:%s' % (inputfile)
	invitations = loadXML(inputfile)
	writeGuestsToOutputCSV(invitations, outputfile)
	print 'finished writing:%s' % (outputfile)

if __name__ == "__main__":
   main(sys.argv[1:])
	