#CSCI3202
#Assignment 8
#Henrik Larsen
#Implemented in Python3
#Sources: https://en.wikipedia.org/wiki/Viterbi_algorithm, https://github.com/hmmlearn/hmmlearn

import sys
import string
from decimal import *
from math import log10

def readFile():
	text = open(sys.argv[1])
	#states = []
	#observations = []
	both = []
	for line in text:
		inputt = line.split()
		both.append((inputt[0],inputt[1]))
	return both

def readTestFile():
	both = []
	with open(sys.argv[2]) as text:
		next(text)
		for line in text:
			inputt = line.split()
			both.append((inputt[0],inputt[1]))
	return both

def initprob(dict,both):
	s = list(map(chr, range(97,123)))
	s.append("_")
	init= {}
	for i in s:
		init[i] = {"Prob":0}
	for i in s:
		getcontext().prec = 10
		init[i] = Decimal(dict[i]["Total"]/Decimal(len(both)))
	return init
	
def emitprob(dicts):
	s = list(map(chr, range(97,123)))
	s.append("_")
	temp = 0
	emit = {}
	for i in s:
		emit[i] = {"Prob":0}
	for i in s:
		probs = []
		for j in s:
			temp = {}
			t = dicts[i]
			if t.has_key(j) == False:
				temp = 0
			else:
				temp[j] = float((t[j]+1)/float(t["Total"]+27))
				probs.append(temp)
				emit[i] = probs
	return emit


def transprob(dicts):
	s = list(map(chr, range(97,123)))
	s.append("_")
	temp = 0
	trans = {}
	for i in s:
		trans[i] = {"Prob":0}
	for i in s:
		probs = []
		for j in s:
			temp = {}
			t = dicts[i]
			if t.has_key(j) == False:
				temp = 0
			else:
				temp[j] = float((t[j]+1)/float(t["Total"]+27))
				probs.append(temp)
				trans[i] = probs
	return trans

def generateObservations(both):
	s = list(map(chr, range(97,123)))
	s.append("_")
	dictE = dict()
	t = 0
	for i in s:
		dictE[i] = {"Total" : 0}
	for i in range(0,len(both)-1):
			q = dictE[both[i][0]]
			if q.has_key(both[i][1]):
				q[both[i][1]] +=1
			else:
				q[both[i][1]] =1
			q["Total"] +=1
	for i in s:
		for j in s:
			if dictE[i].has_key(j) == False:
				dictE[i][j] = 0

	return dictE

def generateState(both):
	s = list(map(chr, range(97,123)))
	s.append("_")
	dictS = dict()

	for i in s:
		dictS[i] = {"Total" : 0}
	for i in range(0,len(both)-1):
		q = dictS[both[i][0]]
		if q.has_key(both[i+1][0]):
			q[both[i+1][0]] +=1
		else:
			q[both[i+1][0]] =1
		q["Total"] +=1
	for i in s:
		for j in s:
			if dictS[i].has_key(j) == False:
				dictS[i][j] = 0
	return dictS

def printInit(init):
	s = list(map(chr, range(97,123)))
	print "Initial Probabilities:"
	for i in s:
		print "P(",i,") = ",init[i] 
	print "P( _ ) = ",init["_"]

def printEmit(emit):
	s = list(map(chr, range(97,123)))
	t =0
	print "Emission Probabilities:\n"
	print "P(Et | Xt)\n"

	for i in s:
		for j in s:
			for k in range(0,len(emit[i])):
				if emit[i][k].has_key(j) == False:
					t = 0
				else:
					print "P(", j, "|", i, ")", emit[i][k][j]	
def printTrans(trans):
	s = list(map(chr, range(97,123)))
	t =0
	print "Transision Probabilities:\n"
	print "P(Xt+1 | Xt)\n"

	for i in s:
		for j in s:
			for k in range(0,len(trans[i])):
				if trans[i][k].has_key(j) == False:
					t = 0
				else:
					print "P(", j, "|", i, ")", trans[i][k][j]

def writeToFile(trans,emit,init,path,t,error):
	s = list(map(chr, range(97,123)))
	t =0
	f = open("Larsen_Assignment8.txt", "w")

	f.write("Initial Probabilities:\n")
	for i in s:
		f.write("P(")
		f.write(i)
		f.write(") = ")
		f.write(str(init[i]))
		f.write("\n") 
	f.write("P( _ ) = ")
	f.write(str(init["_"]))
	f.write("\n")

	f.write("\nEmission Probabilities:\n")
	f.write("P(Et | Xt)\n")
	for i in s:
		for j in s:
			for k in range(0,len(emit[i])):
				if emit[i][k].has_key(j) == False:
					t = 0
				else:
					d = str(emit[i][k][j])
					f.write("P(")
					f.write(j)
					f.write("|")
					f.write(i)
					f.write(") =")
					f.write(d)
					f.write("\n")
			
	f.write("\nTransition Probabilities:\n")
	f.write("P(Xt+1 | Xt)\n")
	s.append("_")
	for i in s:
		for j in s:
			for k in range(0,len(trans[i])):
				if trans[i][k].has_key(j) == False:
					t = 0
				else:
					temp = str(trans[i][k][j])
					f.write("P(")
					f.write(j)
					f.write("|")
					f.write(i)
					f.write(") =")
					f.write(temp)
					f.write("\n")
	for i in range(len(path)):
		f.write(path[i])
		f.write("\n")

	f.write("Error rate without viterbi algorithm: ")
	t1 = str(error[0])
	t2 = str(error[1])
	f.write(t1)
	f.write("\nError rate with viterbi algorithm: ")
	f.write(t2)


def changeDictS(trans, both):
	
	for i in trans:
		for j in trans[i]:
			trans[i][j] = (trans[i][j]+1)/(float(trans[i]["Total"])+27)
	return trans

def changeDictE(emit,both):
	for i in emit:
		for j in emit[i]:
			emit[i][j] = (emit[i][j] + 1)/(float(emit[i]["Total"])+27)
	return emit
def viterbi(both, init, emit, trans):
	v = [{}]
	path = {}
	states = []
	observations = []
	states = list(map(chr, range(97,123)))
	states.append("_")
	
	for i in range(0,len(both)-1):
		observations.append(both[i][1])

	for i in states:
		v[0][i] = log10(init[i]) + log10(emit[i][observations[0]])
		path[i] = [i]

	for t in range(1,len(observations)):
		v.append({})
		newpath = {}
		for j in states:
			(prob,state) = max((v[t-1][n]+log10(trans[n][j])+log10(emit[j][observations[t]]),n) for n in states)
			v[t][j] = prob
			newpath[j] = path[state] + [j]
		path = newpath

	nn = len(observations)-1
	(prob,state) = max((v[nn][y],y) for y in states)
	return (prob,path[state])

def errorRate(path,t):
	obsPath = 0.0
	viterbiPath = 0.0
	for i in range(len(path)):
		if t[i][0] == t[i][1]:
			obsPath += 1
		if path[i] == t[i][0]:
			viterbiPath +=1
	obsPath = 1 - float((obsPath/len(path)))
	viterbiPath = 1 - float((viterbiPath/len(path)))
	return obsPath,viterbiPath

def fixTransProb(trans,s):
	states = list(map(chr, range(97,123)))
	states.append("_")
	t = 0
	for i in states:
		for j in states:
			for k in range(0,26):
				if trans[i][k].has_key(j):
					if s[i][j] != trans[i][k][j]:
						s[i][j] = trans[i][k][j]
	return s

def fixEmitProb(emit,e):
	states = list(map(chr, range(97,123)))
	states.append("_")
	t = 0
	for i in states:
		for j in states:
			for k in range(0,26):
				if emit[i][k].has_key(j):
					if e[i][j] != emit[i][k][j]:
						e[i][j] = emit[i][k][j]
	return e

def printPath(path,t,error):
	for i in range(len(path)):
		print path[i]

	print "Error rate without viterbi algorithm:", error[0]
	print "Error rate with viterbi algorithm:", error[1]


def main():
	both = readFile()
	dictS = generateState(both)
	dictE = generateObservations(both)
	init = initprob(dictS,both)
	emit = emitprob(dictE)
	trans = transprob(dictS)
	s = changeDictS(dictS,both)
	e = changeDictE(dictE,both)
	newS = fixTransProb(trans,s)
	newE = fixEmitProb(emit,e)
	t = readTestFile()
	prob,path = viterbi(t, init, e, newS)
	error = errorRate(path,t)
	writeToFile(trans,emit,init,path,t,error)


if __name__ == '__main__':
	main()