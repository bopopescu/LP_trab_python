#!/usr/bin/python

import xml.etree.ElementTree as ET
import MySQLdb
import threading
import time

class MessageQueue:
	"""Fila de mensagens para ser consumida por thread. Tipo (objeto, label)"""
	mainQueue = []
	@classmethod
	def stack(cls, dataObject, label):
		cls.mainQueue.append((dataObject, label))
	@classmethod
	def pop(cls):
		return cls.mainQueue.pop()

class QueueConsumer(threading.Thread):
	#def ConsumeQueue(self):
	shutdown = False
	def run(self):
		while not self.shutdown:
			time.sleep(1)
			if MessageQueue.mainQueue:
				print MessageQueue.mainQueue
#				self.ConsumeObject(MessageQueue.pop())

	def ConsumeObject(self, obj):
		label = self.evaluateLabel(obj[1])
		
	def evaluateLabel(self, label):
		if label == 'DADOS-GERAIS':
			return 'dados'
		if label == 'DADOS-NUMERICOS':
			return 'dadosnumericos'

class dbCon:
    """BD connection class"""
    def openCon(void):
	return MySQLdb.connect(host='localhost', user='root', passwd='root',db='pythonTest')


def isDataOfInterest(data):
	dataOfInterest = ['NOME-COMPLETO', 'PERMISSAO-DE-DIVULGACAO', 'CIDADE-NASCIMENTO', 'PAIS-DE-NASCIMENTO', 'DATA-FALECIMENTO']
	return data[0] in dataOfInterest

#Main
tree = ET.parse('curriculo.xml')
root = tree.getroot()
qConsumer = QueueConsumer()
#try:
	#qConsumer.start()
#thread.start_new_thread(qConsumer.ConsumeQueue(), ())
#except:
#	print "Unable to start thread"
print "Started..."

#root[0].attrib.values() #valores do dict
root[0].attrib.items() #lista de tuplas do tipo(key, value)
someInterestingData = filter(isDataOfInterest, root[0].attrib.items())
someInterestingData.append(root.attrib['NUMERO-IDENTIFICADOR'])

messageQueue = MessageQueue()
MessageQueue.stack(someInterestingData, root[0].tag)
print MessageQueue.mainQueue
#time.sleep(5)
#MessageQueue.stack(MessageQueue(), someInterestingData, root[0].tag)

x = MessageQueue.pop()
print x
#time.sleep(5)
print MessageQueue.mainQueue

qConsumer.shutdown = True
#qConsumer.join()
#messageQueue.stack(someInterestingData, root[0].tag)

#len(list(root[1][1])) #numero de artigos publicados 'ARTIGOS-PUBLICADOS'
#len(list(root[1][0])) #numero de trabalhos em eventos	'TRABALHOS-EM-EVENTOS'
#len(list(root[3][0])) #numero de orientacoes concluidas	'ORIENTACOES-CONCLUIDAS'

#DbCon = dbCon()
#con = DbCon.openCon()
#cursor = con.cursor()
#cursor.execute("INSERT INTO pais VALUES(\""+name+"\","+rank+","+year+");")
#cursor.execute("SELECT * FROM Estudante")
#print(cursor.fetchall())
#con.commit()
