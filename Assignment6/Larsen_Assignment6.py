#CSCI3202
#Assignment 6
#Henrik Larsen
#Implemented in Python3

import sys
import getopt

class Node(object):
	"""docstring for Node"""
	def __init__(self, name, parents, prob):
		self.name = name
		self.parents = parents
		self.prob = prob

	def getProb(self):
		return self.prob

#WORKS		
def calcMarginal(a, bayes):
	arg = converter(a)
	marginal = 0
	if a.isupper():
		if a == "C":
			temp = calcMarginal("c",bayes)
			return "Marginal probability distribution of Cancer: True:", temp[1], "False:", (1- temp[1])
		if a == "X":
			temp = calcMarginal("x", bayes)
			return "Marginal probability distribution of X-ray: True:", temp[1], "False:", (1- temp[1])
		if a == "D":
			temp = calcMarginal("d", bayes)
			return "Marginal probability distribution of Dyspnoea: True:", temp[1], "False:", (1- temp[1])
		if a == "P":
			temp = calcMarginal("p", bayes)
			return "Marginal probability distribution of Pollution: True:", temp[1], "False:", (1- temp[1])
		if a == "S":
			temp = calcMarginal("s", bayes)
			return "Marginal probability distribution of Smoker: True:", temp[1], "False:", (1- temp[1])

	if bayes[arg].parents == None:
		if a == "s":
			return "smoker", bayes[arg].prob
		elif a == "p":
			return "pollution", bayes[arg].prob
	else:
		if arg == "cancer":
			marginal = bayes["cancer"].prob["ht"]*(bayes["pollution"].prob)*bayes["smoke"].prob+bayes["cancer"].prob["hf"]*(bayes["pollution"].prob)*(1-bayes["smoke"].prob)+bayes["cancer"].prob["lt"]*(1-bayes["pollution"].prob)*(bayes["smoke"].prob)+bayes["cancer"].prob["lf"]*(1-bayes["pollution"].prob)*(1-bayes["smoke"].prob)
			return "Cancer",marginal
		elif arg == "xray":
			temp = calcMarginal("c", bayes)
			marginal = bayes["xray"].prob["t"]*temp[1] + bayes["xray"].prob["f"]*(1-temp[1])
			return "Xray", marginal
		elif arg == "dyspnoea":
			temp = calcMarginal("c", bayes)
			marginal = bayes["dyspnoea"].prob["t"]*temp[1]+bayes["dyspnoea"].prob["f"]*(1-temp[1])
			return "Dyspnoea", marginal
		return marginal

def calcConditional(a1,a2, bayesNet):
	return

def calcJoint(a):
	return

def setPrior(bayes,node,probi):
	bayes[node].prob = probi
	print bayes[node].prob
	

def bayesNet(smokeprob, pollprob):
	bayesNet = dict()

	bayesNet["pollution"] = Node("Pollution", None, pollprob)
	bayesNet["smoke"] = Node("Smoke", None, smokeprob)
	bayesNet["cancer"] = Node("Cancer", ["pollution","smoke"], {"ht":0.05, "hf":0.02, "lt":0.03, "lf":0.001 })
	bayesNet["xray"] = Node("X-ray", ["cancer"], {"t":0.9, "f":0.20})
	bayesNet["dyspnoea"] = Node("Dyspnoea", ["cancer"], {"t":0.65,"f":0.30})
	return bayesNet

def converter(a):
	a = a.lower()
		#print a
	if a  == "p":
		a = "pollution"
	elif a == "s":
		a = "smoke"
	elif a == "c":
		a = "cancer"
	elif a == "x":
		a = "xray"
	elif a == "d":
		a = "dyspnoea"

	return a
	



def main():
	smokeprob = 0.3
	pollprob = 0.1
	bayes = bayesNet(smokeprob, pollprob)
	try:
		opts, args = getopt.getopt(sys.argv[1:], "m:g:j:p:")
	except getopt.GetoptError as err:
		print str(err)
		sys.exit(2)
	for o,a in opts:
		if o in ("-p"):
			print "flag", o
			print "args", a
			print a[0]
			print float(a[1:])
			temp = converter(a[0])
			#setting the prior here works if the Bayes net is already built in
			setPrior(bayes,temp, float(a[1:]))
		elif o in ("-m"):
			print "flag", o
			print "args", a
			print type(a)
			if len(a) == 1:
				prob= calcMarginal(a, bayes)
				print prob
			elif len(a) != 1:
				t = a[1]
				temp = calcMarginal(t, bayes)
				prob = (temp[0], 1- temp[1])
				print prob
		elif o in ("-g"):
			print "flag", o
			print "args", a
			print type(a)
			#you may want to parse a here and pass the left of | and right of | as arguments to calcConditional
			p = a.find("|")
			print a[:p]
			print a[p+1:]
			calcConditional(a[:p], a[p+1:], bayesNet)
		elif o in ("-j"):
			print "flag", o
			print "args", a[0]
			calcJoint(bayesNet)
		else:
			assert False, "unhandled option"


	

if __name__ == '__main__':
	main()
