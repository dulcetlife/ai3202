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
		if arg == "smoke":
			return "smoker", bayes[arg].prob
		elif arg == "pollution":
			return "pollution", bayes[arg].prob
	else:
		if arg == "cancer":
			marginal = bayes["cancer"].prob["ht"]*(1-bayes["pollution"].prob)*bayes["smoke"].prob+bayes["cancer"].prob["hf"]*(1-bayes["pollution"].prob)*(1-bayes["smoke"].prob)+bayes["cancer"].prob["lt"]*(bayes["pollution"].prob)*(bayes["smoke"].prob)+bayes["cancer"].prob["lf"]*(bayes["pollution"].prob)*(1-bayes["smoke"].prob)
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

def calcConditional(a,a1,a2, bayes):
	arg1 = converter(a1)
	arg2 = converter(a2)
	if a == "c|s":
		print bayes["pollution"].prob
		prob = (bayes["cancer"].prob["lt"]*bayes["pollution"].prob*bayes["smoke"].prob + bayes["cancer"].prob["ht"]*(1-bayes["pollution"].prob)*bayes["smoke"].prob)/bayes["smoke"].prob
		return prob
	elif a == "s|c":
		temp = calcMarginal("c",bayes)
		prob = ((bayes["cancer"].prob["lt"]*bayes["pollution"].prob*bayes["smoke"].prob + bayes["cancer"].prob["ht"]*(1-bayes["pollution"].prob)*bayes["smoke"].prob)/bayes["smoke"].prob)*bayes["smoke"].prob/temp[1]
		return prob
	elif a == "c|ds":
		n = bayes["dyspnoea"].prob["t"]*bayes["cancer"].prob["lt"]*bayes["pollution"].prob*bayes["smoke"].prob + bayes["dyspnoea"].prob["t"]*bayes["cancer"].prob["ht"]*(1-bayes["pollution"].prob)*bayes["smoke"].prob
		d1 = bayes["dyspnoea"].prob["t"]*bayes["cancer"].prob["lt"]*bayes["pollution"].prob*bayes["smoke"].prob + bayes["dyspnoea"].prob["t"]*bayes["cancer"].prob["ht"]*(1-bayes["pollution"].prob)*bayes["smoke"].prob
		d2 = bayes["dyspnoea"].prob["f"]*(1-bayes["cancer"].prob["lt"])*bayes["pollution"].prob*bayes["smoke"].prob + bayes["dyspnoea"].prob["f"]*(1-bayes["cancer"].prob["ht"])*(1-bayes["pollution"].prob)*bayes["smoke"].prob
		prob = n/(d1+d2)
		return prob
	elif a == "c|d":
		temp1 = calcMarginal("c",bayes)
		temp2 = calcMarginal("d", bayes)
		prob = bayes["dyspnoea"].prob["t"]*temp1[1]/temp2[1]
		return prob
	elif a == "d|s":
		n1 = bayes["dyspnoea"].prob["t"]*bayes["cancer"].prob["lt"]*bayes["smoke"].prob*bayes["pollution"].prob + bayes["dyspnoea"].prob["t"]*bayes["cancer"].prob["ht"]*bayes["smoke"].prob*(1-bayes["pollution"].prob) 
		n2 = bayes["dyspnoea"].prob["f"]*(1-bayes["cancer"].prob["lt"])*bayes["smoke"].prob*bayes["pollution"].prob + bayes["dyspnoea"].prob["f"]*(1-bayes["cancer"].prob["ht"])*bayes["smoke"].prob*(1-bayes["pollution"].prob) 
		d1 = bayes["cancer"].prob["lt"]*bayes["smoke"].prob*bayes["pollution"].prob + bayes["cancer"].prob["ht"]*bayes["smoke"].prob*(1-bayes["pollution"].prob)
		d2 = (1-bayes["cancer"].prob["lt"])*bayes["smoke"].prob*bayes["pollution"].prob + (1-bayes["cancer"].prob["ht"])*bayes["smoke"].prob*(1-bayes["pollution"].prob)
		prob = (n1+n2)/(d1+d2)
		return prob
	elif a == "s|d":
		temp = calcMarginal("d",bayes)
		n1 = bayes["dyspnoea"].prob["t"]*bayes["cancer"].prob["lt"]*bayes["smoke"].prob*bayes["pollution"].prob + bayes["dyspnoea"].prob["t"]*bayes["cancer"].prob["ht"]*bayes["smoke"].prob*(1-bayes["pollution"].prob) 
		n2 = bayes["dyspnoea"].prob["f"]*(1-bayes["cancer"].prob["lt"])*bayes["smoke"].prob*bayes["pollution"].prob + bayes["dyspnoea"].prob["f"]*(1-bayes["cancer"].prob["ht"])*bayes["smoke"].prob*(1-bayes["pollution"].prob) 
		d1 = bayes["cancer"].prob["lt"]*bayes["smoke"].prob*bayes["pollution"].prob + bayes["cancer"].prob["ht"]*bayes["smoke"].prob*(1-bayes["pollution"].prob)
		d2 = (1-bayes["cancer"].prob["lt"])*bayes["smoke"].prob*bayes["pollution"].prob + (1-bayes["cancer"].prob["ht"])*bayes["smoke"].prob*(1-bayes["pollution"].prob)
		p1 = (n1+n2)/(d1+d2)
		prob = (p1*bayes["smoke"].prob)/temp[1]

		return prob
	elif a == "c|p":
		t = bayes["cancer"].prob["ht"]*(1-bayes["pollution"].prob)*bayes["smoke"].prob + bayes["cancer"].prob["hf"]*(1-bayes["pollution"].prob)*(1-bayes["smoke"].prob)
		prob = t/(1-bayes["pollution"].prob)
		return prob
	elif a == "p|c":
		t = bayes["cancer"].prob["ht"]*(1-bayes["pollution"].prob)*bayes["smoke"].prob + bayes["cancer"].prob["hf"]*(1-bayes["pollution"].prob)*(1-bayes["smoke"].prob)
		p1 = t/(1-bayes["pollution"].prob)
		temp = calcMarginal("c",bayes)
		prob = p1*(1-bayes["pollution"].prob)/temp[1]
		return prob
	elif a == "d|p":
		n1 = bayes["dyspnoea"].prob["t"]*bayes["cancer"].prob["ht"]*(1-bayes["pollution"].prob)*bayes["smoke"].prob + bayes["dyspnoea"].prob["t"]*bayes["cancer"].prob["hf"]*(1-bayes["pollution"].prob)*(1-bayes["smoke"].prob)
		n2 = bayes["dyspnoea"].prob["f"]*(1-bayes["cancer"].prob["ht"])*(1-bayes["pollution"].prob)*bayes["smoke"].prob + bayes["dyspnoea"].prob["f"]*(1-bayes["cancer"].prob["hf"])*(1-bayes["pollution"].prob)*(1-bayes["smoke"].prob)
		d1 = bayes["cancer"].prob["ht"]*(1-bayes["pollution"].prob)*bayes["smoke"].prob + bayes["cancer"].prob["hf"]*(1-bayes["pollution"].prob)*(1-bayes["smoke"].prob)
		d2 = (1-bayes["cancer"].prob["ht"])*(1-bayes["pollution"].prob)*bayes["smoke"].prob + (1-bayes["cancer"].prob["hf"])*(1-bayes["pollution"].prob)*(1-bayes["smoke"].prob)
		prob = (n1+n2)/(d1+d2)
		return prob
	elif a == "p|d":
		n1 = bayes["dyspnoea"].prob["t"]*bayes["cancer"].prob["ht"]*(1-bayes["pollution"].prob)*bayes["smoke"].prob + bayes["dyspnoea"].prob["t"]*bayes["cancer"].prob["hf"]*(1-bayes["pollution"].prob)*(1-bayes["smoke"].prob)
		n2 = bayes["dyspnoea"].prob["f"]*(1-bayes["cancer"].prob["ht"])*(1-bayes["pollution"].prob)*bayes["smoke"].prob + bayes["dyspnoea"].prob["f"]*(1-bayes["cancer"].prob["hf"])*(1-bayes["pollution"].prob)*(1-bayes["smoke"].prob)
		d1 = bayes["cancer"].prob["ht"]*(1-bayes["pollution"].prob)*bayes["smoke"].prob + bayes["cancer"].prob["hf"]*(1-bayes["pollution"].prob)*(1-bayes["smoke"].prob)
		d2 = (1-bayes["cancer"].prob["ht"])*(1-bayes["pollution"].prob)*bayes["smoke"].prob + (1-bayes["cancer"].prob["hf"])*(1-bayes["pollution"].prob)*(1-bayes["smoke"].prob)
		p1 = (n1+n2)/(d1+d2)
		temp = calcMarginal("d",bayes)
		prob = p1*(1-bayes["pollution"].prob)/temp[1]
		return prob
	elif a == "p|cs":
		n = bayes["cancer"].prob["ht"]*bayes["smoke"].prob*(1-bayes["pollution"].prob)
		d = bayes["cancer"].prob["ht"]*bayes["smoke"].prob*(1-bayes["pollution"].prob) + bayes["cancer"].prob["lt"]*bayes["smoke"].prob*(bayes["pollution"].prob)
		prob = n/d
		return prob
	elif a == "d|c":
		temp1 = calcMarginal("c",bayes)
		temp2 = calcMarginal("d", bayes)
		prob1 = bayes["dyspnoea"].prob["t"]*temp1[1]/temp2[1]
		prob = (prob1*temp2[1])/temp1[1]
		return prob
	elif a == "p|ds":
		n = bayes["dyspnoea"].prob["t"]*bayes["cancer"].prob["ht"]*(1-bayes["pollution"].prob)*bayes["smoke"].prob + bayes["dyspnoea"].prob["f"]*(1-bayes["cancer"].prob["ht"])*(1-bayes["pollution"].prob)*bayes["smoke"].prob
		d1 = bayes["dyspnoea"].prob["t"]*bayes["cancer"].prob["ht"]*(1-bayes["pollution"].prob)*bayes["smoke"].prob + bayes["dyspnoea"].prob["t"]*bayes["cancer"].prob["lt"]*bayes["pollution"].prob*bayes["smoke"].prob
		d2 = bayes["dyspnoea"].prob["f"]*(1-bayes["cancer"].prob["ht"])*(1-bayes["pollution"].prob)*bayes["smoke"].prob + bayes["dyspnoea"].prob["f"]*(1-bayes["cancer"].prob["lt"])*bayes["pollution"].prob*bayes["smoke"].prob
		prob = n/(d1+d2)
		return prob
	elif a == "x|ds":
		n1 = bayes["xray"].prob["t"]*bayes["dyspnoea"].prob["t"]*bayes["cancer"].prob["ht"]*(1-bayes["pollution"].prob)*bayes["smoke"].prob + bayes["xray"].prob["f"]*bayes["dyspnoea"].prob["f"]*(1-bayes["cancer"].prob["ht"])*(1-bayes["pollution"].prob)*bayes["smoke"].prob
		n2 = bayes["xray"].prob["t"]*bayes["dyspnoea"].prob["t"]*bayes["cancer"].prob["lt"]*bayes["pollution"].prob*bayes["smoke"].prob + bayes["xray"].prob["f"]*bayes["dyspnoea"].prob["f"]*(1-bayes["cancer"].prob["lt"])*bayes["pollution"].prob*bayes["smoke"].prob
		d1 = bayes["dyspnoea"].prob["t"]*bayes["cancer"].prob["ht"]*(1-bayes["pollution"].prob)*bayes["smoke"].prob + bayes["dyspnoea"].prob["f"]*(1-bayes["cancer"].prob["ht"])*(1-bayes["pollution"].prob)*bayes["smoke"].prob 
		d2 = bayes["dyspnoea"].prob["t"]*bayes["cancer"].prob["lt"]*bayes["pollution"].prob*bayes["smoke"].prob + bayes["dyspnoea"].prob["f"]*(1-bayes["cancer"].prob["lt"])*bayes["pollution"].prob*bayes["smoke"].prob
		prob = (n1+n2)/(d1+d2)
		return prob
	elif a == "x|s":
		n1 = bayes["xray"].prob["t"]*bayes["cancer"].prob["lt"]*bayes["pollution"].prob*bayes["smoke"].prob + bayes["xray"].prob["t"]*bayes["cancer"].prob["ht"]*(1-bayes["pollution"].prob)*bayes["smoke"].prob
		n2 = bayes["xray"].prob["f"]*(1-bayes["cancer"].prob["lt"])*bayes["pollution"].prob*bayes["smoke"].prob + bayes["xray"].prob["f"]*(1-bayes["cancer"].prob["ht"])*(1-bayes["pollution"].prob)*bayes["smoke"].prob
		d1 = bayes["cancer"].prob["lt"]*bayes["pollution"].prob*bayes["smoke"].prob + bayes["cancer"].prob["ht"]*(1-bayes["pollution"].prob)*bayes["smoke"].prob 
		d2 = (1-bayes["cancer"].prob["lt"])*bayes["pollution"].prob*bayes["smoke"].prob + (1-bayes["cancer"].prob["ht"])*(1-bayes["pollution"].prob)*bayes["smoke"].prob
		prob = (n1+n2)/(d1+d2)
		return prob
	elif a == "p|s":
		prob = (1-bayes["pollution"].prob)
		return prob
	elif a == "x|x" or a == "p|p" or a == "s|s" or a == "c|c" or a == "d|d" or a == "s|cs" or a == "s|ds" or a == "c|ct" or a == "d|ds":
		prob = 1
		return prob
	else:
		print "Not a valid input"
		return False


def calcJoint(a,a1,a2,bayes):
	arg1 = converter(a1)
	arg2 = converter(a2)
	
	s = "|"
	cond = a1+s+a2
	
	if type(calcConditional(cond,a1,a2,bayes)) == int or type(calcConditional(cond,a1,a2,bayes)) == float :
		t1 = calcMarginal(a2, bayes)
		t2 = calcConditional(cond,a1,a2,bayes)
		temp = t1[1]
		prob = temp*t2
		return prob
	else:
		cond = a2+s+a1
		t1 = calcMarginal(a1, bayes)
		t2 = calcConditional(cond,a1,a2,bayes)
		temp = t1[1]
		prob = temp*t2
		return prob

	



def setPrior(bayes,node,probi):
	bayes[node].prob = probi
	print "Prior for", node, "set to:",bayes[node].prob
	

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
	pollprob = 0.9
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

			t = calcConditional(a, a[:p], a[p+1:], bayes)
			print "The conditinal probability for P(",a,") is {0:.3f}".format(round(t,3)) 
		elif o in ("-j"):
			print "flag", o
			print "args", a[0]
			t = calcJoint(a, a[0],a[1],bayes)
			print "The joint probability for P(", a, ") is {0:.3f}".format(round(t,3))
		else:
			assert False, "unhandled option"



if __name__ == '__main__':
	main()
