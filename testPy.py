#!/usr/bin/python
import sys
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
			if MessageQueue.mainQueue:
				print MessageQueue.mainQueue
				self.ConsumeObject(MessageQueue.pop())
			time.sleep(1)

	def ConsumeObject(self, obj):
		label = self.evaluateLabel(obj[1])
		data = dict(obj[0])
		insertIntoTable(label, data)
	def evaluateLabel(self, label):
		if label == 'DADOS-GERAIS':
			return 'dadosGerais'
		if label == 'DADOS-NUMERICOS':
			return 'dadosNumericos'

class DaoQueueConsumer:
	"""Data responsible class"""
	def openCon(void):
		return MySQLdb.connect(host='localhost', user='root', passwd='root',db='pythonTest')
	#def prepareStatement(attDict, table):

def insertIntoTable(label,data):
	if label=='dadosGerais':
		attList = [data['NUMERO-IDENTIFICADOR'], data['NOME-COMPLETO'], data['CIDADE-NASCIMENTO'], data['PERMISSAO-DE-DIVULGACAO']]
		cursor.execute("""INSERT INTO dadosGerais VALUES (%s, %s, %s, %s)""", attList)
		con.commit()
def isDataOfInterest(data):
	dataOfInterest = ['NOME-COMPLETO', 'PERMISSAO-DE-DIVULGACAO', 'CIDADE-NASCIMENTO', 'PAIS-DE-NASCIMENTO']
	return data[0] in dataOfInterest

#Main
tree = ET.parse('curriculo.xml')
root = tree.getroot()
daoQueueConsumer = DaoQueueConsumer()
con = daoQueueConsumer.openCon()
cursor = con.cursor()
qConsumer = QueueConsumer()
try:
	qConsumer.start()
#thread.start_new_thread(qConsumer.ConsumeQueue(), ())
except:
	print "Unable to start thread"
print "Started..."

#root[0].attrib.values() #valores do dict
root[0].attrib.items() #lista de tuplas do tipo(key, value)
someInterestingData = filter(isDataOfInterest, root[0].attrib.items())
someInterestingData.append(('NUMERO-IDENTIFICADOR', root.attrib['NUMERO-IDENTIFICADOR']))

MessageQueue.stack(someInterestingData, root[0].tag)

time.sleep(5)

qConsumer.shutdown = True
qConsumer.join()

#len(list(root[1][1])) #numero de artigos publicados 'ARTIGOS-PUBLICADOS'
#len(list(root[1][0])) #numero de trabalhos em eventos	'TRABALHOS-EM-EVENTOS'
#len(list(root[3][0])) #numero de orientacoes concluidas	'ORIENTACOES-CONCLUIDAS'

#cursor.execute("INSERT INTO pais VALUES(\""+name+"\","+rank+","+year+");")
#cursor.execute("SELECT * FROM Estudante")
#print(cursor.fetchall())
#con.commit()
