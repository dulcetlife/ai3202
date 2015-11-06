#CSCI3202
#Assignment 7
#Henrik Larsen
#Implemented in Python3


samples = [0.82, 0.56, 0.08, 0.81, 0.34, 0.22, 0.37, 0.99, 0.55, 0.61, 0.31, 0.66, 0.28, 1, 0.95, 0.71, 0.14, 0.1, 1.0,
	0.71, 0.1, 0.6, 0.64, 0.73, 0.39, 0.03, 0.99, 1.0, 0.97, 0.54, 0.8, 0.97, 0.07, 0.69, 0.43, 0.29, 0.61, 0.03, 0.13,
	0.14, 0.13, 0.4, 0.94, 0.19, 0.6, 0.68, 0.36, 0.67, 0.12, 0.38, 0.42, 0.81, 0.0, 0.2, 0.85, 0.01, 0.55, 0.3, 0.3,
	0.11, 0.83, 0.96, 0.41, 0.65, 0.29, 0.4, 0.54, 0.23, 0.74, 0.65, 0.38, 0.41, 0.82, 0.08, 0.39, 0.97, 0.95, 0.01, 0.62, 0.32,
	0.56, 0.68, 0.32, 0.27, 0.77, 0.74, 0.79, 0.11, 0.29, 0.69, 0.99, 0.79, 0.21, 0.2, 0.43, 0.81, 0.9, 0.0, 0.91, 0.01]

class Node(object):
	def __init__(self, name,prob):
		self.name = name
		self.prob = prob


def generatePriorSample(bayes):
	size = len(samples)
	genSample = []
	temp = []
	for i in range(0,size):
		if i % 4 == 0:
			temp = []
			cloudy = samples[i]
			sprinkler = samples[i+1]
			rain = samples[i+2]
			wet = samples[i+3]

			if cloudy < bayes["cloudy"].prob:
				temp.append(1)

				if sprinkler < bayes["sprinkler"].prob["c"]:
					temp.append(1)
				if sprinkler >= bayes["sprinkler"].prob["c"]:
					temp.append(0)
				if rain < bayes["rain"].prob["c"]:
					temp.append(1)
				if rain >= bayes["rain"].prob["c"]:
					temp.append(0)

			if cloudy >= bayes["cloudy"].prob:
				temp.append(0)

				if sprinkler < bayes["sprinkler"].prob["~c"]:
					temp.append(1)
				if sprinkler >= bayes["sprinkler"].prob["~c"]:
					temp.append(0)
				if rain < bayes["rain"].prob["~c"]:
					temp.append(1)
				if rain >= bayes["rain"].prob["~c"]:
					temp.append(0)
			
			if temp[1] == 1:
				if temp[2] == 1:
					if wet < bayes["wet"].prob["sr"]:
						temp.append(1)
					if wet >= bayes["wet"].prob["sr"]:
						temp.append(0)
				if temp[2] != 1:
					if wet < bayes["wet"].prob["s~r"]:
						temp.append(1)
					if wet >= bayes["wet"].prob["s~r"]:
						temp.append(0)

			if temp[1] != 1:
				if temp[2] == 1:
					if wet < bayes["wet"].prob["~sr"]:
						temp.append(1)
					if wet >= bayes["wet"].prob["~sr"]:
						temp.append(0)
				if temp[2] != 1:
					if wet < bayes["wet"].prob["~s~r"]:
						temp.append(1)
					if wet >= bayes["wet"].prob["~s~r"]:
						temp.append(0)
			genSample.append(temp)
	return genSample
	
def bayesNet():
	bayesNet = dict()
	bayesNet["cloudy"] = Node("cloudy", 0.5)
	bayesNet["rain"] = Node("rain", {"c":0.8, "~c":0.2 })
	bayesNet["sprinkler"] = Node("sprinkler", {"c":0.1, "~c":0.5})
	bayesNet["wet"] = Node("wet", {"sr":0.99, "s~r":0.9, "~sr":0.9, "~s~r":0})
	return bayesNet

def prob1(newSample):
	#1a
	clouda = 0.0
	for i in newSample:
		cloud = i[0]
		if cloud == 1:
			clouda += 1
	prob1a = clouda/len(newSample)

	#1b
	rainb = 0.0
	cloudb = 0.0
	for i in newSample:
		cloud = i[0]
		rain = i[2]
		if rain == 1:
			rainb +=1
			if cloud == 1:
				cloudb += 1
	prob1b = cloudb/rainb
	
	#1c
	sprinklerc = 0.0
	wetc = 0.0
	for i in newSample:
		sprinkler = i[1]
		wet = i[3]
		if wet == 1:
			wetc +=1
			if sprinkler == 1:
				sprinklerc +=1
	prob1c = sprinklerc/wetc
	
	#1d
	sprinklercountd = 0.0
	wetcloudyd = 0.0
	for i in newSample:
		cloud = i[0]
		sprinkler = i[1]
		wet = i[3]
		if cloud == 1:
			if wet == 1:
				wetcloudyd +=1
				if sprinkler == 1:
					sprinklercountd +=1
	prob1d = sprinklercountd/wetcloudyd

	return prob1a,prob1b,prob1c,prob1d

def prob2(bayes):
	#p(c)
	prob2a = bayes["cloudy"].prob

	#p(c|r)
	prob2b = (bayes["rain"].prob["c"]*bayes["cloudy"].prob)/((bayes["rain"].prob["c"]*bayes["cloudy"].prob)
		+(bayes["rain"].prob["~c"]*bayes["cloudy"].prob))

	#p(s|w)
	sprinkler = bayes["sprinkler"].prob["c"]*bayes["cloudy"].prob + bayes["sprinkler"].prob["~c"]*bayes["cloudy"].prob
	rain = bayes["rain"].prob["c"]*bayes["cloudy"].prob + bayes["rain"].prob["~c"]*bayes["cloudy"].prob
	sprinklerAndRain = sprinkler*rain

	
def prob3(bayes):
	sampleRejection = []

	for i in samples:
		sampleRejection.append(i)
		
	#3a
	count3a = 0.0
	cloudy3a = 0.0
	for i in range(0,len(sampleRejection)):
		cloudya = sampleRejection[i]
		count3a +=1
		if cloudya < bayes["cloudy"].prob:
			cloudy3a+=1
		
	prob3a = cloudy3a/count3a

	#3b
	cloudy3b = 0.0
	rain3b = 0.0
	for i in range(0,len(sampleRejection)-1):
		if i % 2 == 0:
			cloudyb = sampleRejection[i]
			rainb = sampleRejection[i+1]
			if cloudyb < bayes["cloudy"].prob:
				if rainb < bayes["rain"].prob["c"]:
					cloudy3b += 1
					rain3b += 1
			else:
				if rainb < bayes["rain"].prob["~c"]:
					rain3b +=1
	prob3b = cloudy3b/rain3b

	#3c
	sprinkler3c = 0.0
	wet3c = 0.0
	for i in range(0, len(sampleRejection)-3):
		if i % 4 == 0:
			cloudyc = sampleRejection[i]
			sprinklerc = sampleRejection[i+1]
			rainc = sampleRejection[i+2]
			wetc = sampleRejection[i+3]

			if cloudyc < bayes["cloudy"].prob:
				cloudyc = 1
				if sprinklerc < bayes["sprinkler"].prob["c"]:
					sprinklerc = 1
				else:
					sprinklerc = 0

				if rainc < bayes["rain"].prob["c"]:
					rainc = 1
				else:
					rainc = 0
			else:
				cloudyc = 0
				if sprinklerc < bayes["sprinkler"].prob["~c"]:
					sprinklerc = 1
				else:
					sprinklerc = 0

				if rainc < bayes["rain"].prob["~c"]:
					rainc = 1
				else:
					rainc = 0
			if sprinklerc == 1:
				if rainc == 1:
					if wetc < bayes["wet"].prob["sr"]:
						wet3c +=1
						sprinkler3c +=1
				else:
					if wetc < bayes["wet"].prob["s~r"]:
						wet3c +=1
						sprinkler3c +=1
			else:
				if rainc == 1:
					if wetc < bayes["wet"].prob["~sr"]:
						wet3c +=1
				else:
					if wetc < bayes["wet"].prob["~s~r"]:
						wet3c +=1
	prob3c = sprinkler3c/wet3c

	#3d
	sprinkler3d = 0.0
	wet3d = 0.0
	for i in range(0, len(sampleRejection)-3):
		if i % 4 == 0:
			cloudyd = sampleRejection[i]
			sprinklerd = sampleRejection[i+1]
			raind = sampleRejection[i+2]
			wetd = sampleRejection[i+3]

			if cloudyd < bayes["cloudy"].prob:
				if sprinklerd < bayes["sprinkler"].prob["c"]:
					sprinklerd = 1
				else:
					sprinklerd = 0
				if raind < bayes["rain"].prob["c"]:
					raind = 1
				else:
					raind = 0
			if sprinklerd == 1:
				if raind == 1:
					if wetd < bayes["wet"].prob["sr"]:
						sprinkler3d +=1
						wet3d +=1
				else:
					if wetd < bayes["wet"].prob["s~r"]:
						sprinkler3d +=1
						wet3d +=1
			else:
				if raind == 1:
					if wetd < bayes["wet"].prob["~sr"]:
						wet3d +=1
				else:
					if wetd < bayes["wet"].prob["~s~r"]:
						wet3d +=1
	prob3d = sprinkler3d/wet3d

	return prob3a,prob3b,prob3c,prob3d


def printer(prob1,prob3):
	print "Problem 1: Prior Sampling"
	print "P(c = True) =", prob1[0]
	print "P(c = True | r = True) =", prob1[1]
	print "P(s = True | w = True) =", prob1[2]
	print "P(s = True | c = True, w = True) =", prob1[3]
	print "\nProblem 3: Rejection Sampling"
	print "P(c = True) =", prob3[0]
	print "P(c = True | r = True) =", prob3[1]
	print "P(s = True | w = True) =", prob3[2]
	print "P(s = True | c = True, w = True) =", prob3[3]

def main():
	bayes = bayesNet()
	newSample = generatePriorSample(bayes)
	prob1List = prob1(newSample)
	prob3List = prob3(bayes)
	prob2(bayes)
	printer(prob1List, prob3List)
	
	


if __name__ == '__main__':
	main()