
from __future__ import division
from math import *

def csv(cfile):
	import csv
	with open(cfile) as file:
		reader = csv.reader(file)
		data=list(reader)
		liste=[]
		for i in data:
			for j in i[:4]:
				liste.append(float(j))
			liste.append(i[4])
		return liste

def helper():
	data=csv("iris.csv")
	liste=[]
	k=0
	while(k<=len(data)-1):
		liste.append(tuple(data[k:k+5]))
		k=k+5
	return liste


#Contract:
#tuple tuple -> number
#Purpose: find distance between two points
#Examples:
#distance((2,3,4,5,(1,3,4,5))-> 1.0
def distance(p1,p2):
	dist=pow((p2[0]-p1[0]),2)+pow((p2[1]-p1[1]),2)+pow((p2[2]-p1[2]),2)+pow((p2[3]-p1[3]),2)
	a=sqrt(dist)
	return a

#print distance((2,3,4,5),(1,3,4,5))
#print distance((1,1,1,1),(1,1,1,1))

#Contract:
#list tuple->tuple
#Purpose: return the nearest point to the given point in the list 
#Examples:
#[(1,1,1,1),(2,2,2,2)],(1,1,1,1)->(1,1,1,1)
def function(lon,tup):
	liste = []
	for i in lon:
		x=distance(tup,i)
		liste.append(x)
	a=min(liste)
	i=liste.index(a)
	return lon[i]

print function([(1,1,1,1),(2,2,2,2)],(1,1,1,1))


def crossvalidation(test,training):
	print "Actual Class"," "*17,"Predicted Class"
	liste=[]
	for j in test:
		a=function(training,j)
		print j,a
		liste.append(a)



#Traning and Test sets
data=helper()
test1=data[:15]
training1=data[15:]
test2=data[:5]+data[140:]
training2=data[5:140]
test3=data[29:50]
training3=data[:29]+data[50:]

crossvalidation(test1,training1)
crossvalidation(test2,training2)
crossvalidation(test3,training3)
crossvalidation([(4.7, 3.2, 1.6, 0.2, 'setosa'),(5.0, 3.3, 1.4, 0.2, 'setosa')],[(4.6, 3.1, 1.5, 0.2, 'verticolor'),(5.0, 3.4, 1.5, 0.2, 'setosa')])

