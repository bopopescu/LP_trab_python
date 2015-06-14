#!/usr/bin/python

import xml.etree.ElementTree as ET
import MySQLdb

tabs = 0

class dbCon:
    """BD connection class"""
    def openCon(void):
	return MySQLdb.connect(host='localhost', user='root', passwd='root',db='python')

def iterAllLevels(node):
	global tabs
	for child in node.iter('*'):
		hasChildren = list(child)
		if hasChildren:
			tabs = tabs + 1
	#		for gran in child.iter('*'):
			print hasChildren
#			print ' ' * tabs,  child.tag, child.attrib, child.text
#			iterAllLevels(child)
		else:
			tabs = tabs - 1
#		print child.tag, child.attrib, child.text

DbCon = dbCon()
con = DbCon.openCon()

tree = ET.parse('sampleData.xml')
root = tree.getroot()

iterAllLevels(root)

#for child in root.iter('*'):
#	print(child.tag, child.attrib, child.text)
#	if list(child):
#		print child.tag, child.attrib, child.text
#		for gran in list(child):
#			print '-->', gran.tag, gran.attrib, gran.text
#		for gran in child.list()
#			print(gran.tag, gran.text)


#for child in root:
#	for gran in child:
#		print (gran.text)
#    cont = 0
#    for element in parent.iterdescendants():
#        if element.tag == 'country':
#            if element.text == str(id_number):
#                cont = 1
#        if element.getchildren() == []:
#	 print(element.text)
#            insert[element.tag] = element.text
#    if cont:
#        inserts.append(insert)

#print inserts

#cursor = con.cursor()
#cursor.execute("SELECT * FROM Estudante")
#print(cursor.fetchall())


