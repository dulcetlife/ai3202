#Darren White
#Assignment 7



sample = [0.82,      0.56,      0.08,      0.81,      0.34,      0.22,      0.37,      0.99,      0.55,      0.61,      0.31,      0.66,      0.28,      1.0,      0.95,      
0.71,      0.14,      0.1,      1.0,      0.71,      0.1,      0.6,      0.64,      0.73,      0.39,      0.03,      0.99,      1.0,      0.97,      0.54,      0.8,      0.97,      
0.07,      0.69,      0.43,      0.29,      0.61,      0.03,      0.13,      0.14,      0.13,      0.4,      0.94,      0.19,
0.6,      0.68,      0.36,      0.67,      
0.12,      0.38,      0.42,      0.81,      0.0,      0.2,      0.85,      0.01,      0.55,      0.3,      0.3,      0.11,      0.83,      0.96,      0.41,      0.65,      
0.29,      0.4,      0.54,      0.23,      0.74,      0.65,      0.38,      0.41,      0.82,      0.08,      0.39,      0.97,      0.95,      0.01,      0.62,      0.32,      
0.56,      0.68,      0.32,      0.27,      0.77,      0.74,      0.79,      0.11,      0.29,      0.69,      0.99,      0.79,      0.21,      0.2,      0.43,      0.81,      
0.9,      0.0,      0.91,      0.01]


def number(list1):
	# just to make sure there are 100 samples, and that I copy / pasted correctly
	count = 0
	for item in list1:
		count+=1
		print count, item
	return count	


def c_true_sample(list1):
	#easy enough, if it's below .5 it gets counted as c
	count = 0.0
	i = 0
	while (i < len(list1)):
		if (list1[i] < 0.5):
			count +=1
		i += 3	
	count = count/25		
	return count	
	
	
def r_true_sample(list1):
	#take two samples, count is r is true, countbad is r is false
	rtrue = 0.0
	rfalse = 0.0
	i = 0
	size = len(list1)
	while (i < size):
		if (list1[i] < .5):
			i += 1
			if (list1[i] < .8):
					rtrue += 1
					i +=3
			else:
					rfalse +=1
					i+=3	
		else:
			i += 1
			if (list1[i] >= .8):
					rtrue += 1
					i+=3		
			else: 
					rfalse +=1
					i+=3
					
	denominator = rtrue+rfalse
	count = rtrue/denominator		 			
	return count		
	
		
def c_given_r_sample(list1):
	#like r_true above, but add another counter for when rc is true, which we will divide by all the r's.
	r = 0.0
	rc = 0.0
	i = 0
	size = len(list1)
	while (i < size):
		if (list1[i] < .5):
			#Cloudy
			i += 1
			if (list1[i] < .8):
				#rc
					r += 1
					rc += 1
		else:
			i += 1
			if (list1[i] >= .8):
					r += 1	
		i += 3			 			
	return rc/r		

def s_given_w_sample(list1):
	wtrue = 0.0
	swtrue = 0.0
	size = len(list1)
	i = 0
	while (i < size):
		if (list1[i] < .5):
			#is cloudy
			i += 1
			if (list1[i] < .1):
				#sc
				i += 1
				if (list1[i] < .8):
					#scr is true
					i += 1
					if (list1[i] < .99):
						wtrue += 1
						swtrue += 1
					i += 1	
				else:
					#sc~r
					i += 1		
					if (list1[i] < .90):
						wtrue += 1
						swtrue += 1
					i += 1	
			else :
				#~sc
				i += 1
				if (list1[i] <.8):
					#~scr
					i += 1
					if (list1[i] < .90):
						wtrue +=1	
					i += 1	
				else:
					#~sc~r
					i += 2	
		else:
			#not cloudy							
			i +=1
			if (list1[i] < .5):
				#s~c 
				i += 1
				if (list1[i] < .8):
					#s~cr
					i += 1
					if (list1[i] < .99):
						wtrue += 1
						swtrue += 1
					i += 1			
				else:
					#s~c~r
					i += 1
					if (list1[i] < .90):
						wtrue += 1
						swtrue += 1
					i += 1
			else:
				#~s~c
				i += 1
				if (list1[i] <.8):
					#~s~cr
					i += 1
					if (list1[i] < .90):
						wtrue +=1
					i += 1	
				else:
					#~s~c~r
					i += 2					
	count = swtrue / wtrue
	return count		
			
def s_given_c_w(list1):
	cwtrue = 0.0
	scwtrue = 0.0
	size = len(list1)
	w = 0
	i = 0
	while (i < size):
		if (list1[i] < .5):
			#is cloudy
			i += 1
			if (list1[i] < .1):
				#sc is true
				i += 1
				if (list1[i] < .8):
					#scr is true
					i += 1
					if (list1[i] < .99):
						cwtrue += 1
						scwtrue += 1
					i += 1
					w += 1	
				else:
					#sc~r
					i += 1		
					if (list1[i] < .90):
						cwtrue += 1
						scwtrue += 1
					i += 1
					w += 1
			else :
				#~sc
				i += 1
				if (list1[i] <.8):
					#~scr
					i += 1
					if (list1[i] < .90):
						cwtrue +=1	
					i += 1	
					w += 1
				else:
					#~sc~r
					i += 2
					w += 1		
		else:
			#not cloudy							
			i +=1
			if (list1[i] < .5):
				#s~c 
				i += 1
				if (list1[i] < .8):
					#s~cr
					i += 1
					if (list1[i] < .99):
						i += 1			
				else:
					#s~c~r
					i += 1
					if (list1[i] < .90):
						i += 1
			else:
				#~s~c
				i += 1
				if (list1[i] <.8):
					#~s~cr
					i += 1
					if (list1[i] < .90):
						i += 1	
						w += 1
					else:
						i += 1
						w += 1		
				else:
					#~s~c~r
					i += 2		
					w += 1						
	count = scwtrue / cwtrue
	return count
	
def c_exact():
	exact = .50
	return exact	
	
def c_given_r_exact():
	#P(c|r) = P(r|c)*P(C)/P(r)
	#realized after coding, this is just given to us, but oh well, confirmed my coding.
	numerator = (0.8)*(0.5)
	denominator = (.5)*(.8)+(.5)*(.2)
	exact = numerator / denominator
	return exact	
	
def s_given_w_exact():
	#first calculate weighted values of each table
	s = (.5)*.1 + (.5)*.5
	r = (.5)*.8 + (.5)*.2
	sr = s*r
	s_not_r = s*(1-r)
	not_s_r = (1-s)*(r)
	w = .99*sr+.9*s_not_r+.9*not_s_r #this is the total prob of w
	numerator = .99*sr+.9*s_not_r #only look at those including s
	exact = numerator / w
	return exact	
	
def s_given_c_w_exact():
	#first calculate weighted values of each table
	sc = .1
	rc = .8
	sr = sc*rc
	s_not_r = sc*(1-rc)
	not_s_r = (1-sc)*(rc)
	w = .99*sr+.9*s_not_r+.9*not_s_r #this is the total prob of wc
	numerator = .99*sr+.9*s_not_r #only look at those including sc
	exact = numerator / w
	return exact	

def c_reject_sample(list1):
	#easy enough, if it's below .5 it gets counted as c
	count = 0.0
	for item in list1:
		if (item < 0.5):
			count +=1		
	return count/(len(list1))

	
def c_r_reject(list1):
	NewSample=[]
	cr = 0.0
	r = 0.0
	i = 0
	size = len(list1)
	#make a loop to create sample
	while (i < size):
		if (list1[i] < 0.5):
			#cloudy
			i += 1
			if (list1[i] < 0.8):
				NewSample.append(list1[i-1])
				NewSample.append(list1[i])
			i += 1
				
		else:
			#not cloudy
			i += 1
			if (list1[i] >= .8):
				NewSample.append(list1[i-1])
				NewSample.append(list1[i])
			i += 1	
			
	size2 = len(NewSample)
	j = 0
	while (j < size2):
		if (NewSample[j] < 0.5):
			#cloudy
			j += 1
			if (NewSample[j] < 0.8):
				r += 1
				cr += 1
			j += 1
		else:
			#not cloudy
			j += 2	
			r += 1					
	return cr / r			
	
			
	
def s_w_reject(list1):
	sw = 0.0
	w = 0.0	
	size = len(list1)
	i = 0
	NewSample = []
	while (i < size):
		if (list1[i] < .5):
			#Cloudy
			i += 1
			if (list1[i] <.1):
				#CS
				i += 1
				if (list1[i] < .8):
					#CSR
					i +=1
					if (list1[i] < .99):
						#WCSR
						NewSample.append(list1[i-3])
						NewSample.append(list1[i-2])
						NewSample.append(list1[i-1])
						NewSample.append(list1[i])
					i += 1	
				else:
					#CS~R
					i += 1
					if (list1[i] < .90):
						NewSample.append(list1[i-3])
						NewSample.append(list1[i-2])
						NewSample.append(list1[i-1])
						NewSample.append(list1[i])
					i += 1	
			else:
				#C~s
				i +=1
				if (list1[i] < .8):
					#C~SR
					i += 1
					if (list1[i] < .9):
						NewSample.append(list1[i-3])
						NewSample.append(list1[i-2])
						NewSample.append(list1[i-1])
						NewSample.append(list1[i])
					i += 1	
				else:
					i += 2			
		else:
			#not cloudy
			i += 1
			if (list1[i] < .5):
				#~CS
				i += 1
				if (list1[i] < .8):
					#~CSR
					i += 1
					if (list1[i] < .99):
						NewSample.append(list1[i-3])
						NewSample.append(list1[i-2])
						NewSample.append(list1[i-1])
						NewSample.append(list1[i])
					i += 1	
				else:
					#~CS~R
					i += 1
					if (list1[i] < .9):
						NewSample.append(list1[i-3])
						NewSample.append(list1[i-2])
						NewSample.append(list1[i-1])
						NewSample.append(list1[i])
					i += 1	
			else:
				#~C~SR
				i += 1
				if (list1[i] < .8):
					#~C~SR
					i += 1
					if (list1[i] < .99):
						NewSample.append(list1[i-3])
						NewSample.append(list1[i-2])
						NewSample.append(list1[i-1])
						NewSample.append(list1[i])
					i += 1	
				else:
					i += 2	
	j = 0
	while (j < len(NewSample)):
		if (NewSample[j] < .5):
			#Cloudy
			j += 1
			if (NewSample[j] < .1):
				sw += 1
		else:
			#Not Cloudy
			j += 1
			if (NewSample[j] < .5):
				sw += 1
				
		j += 3				
					
	return sw / (len(NewSample)/4)		
	
def s_c_w_reject(list1):
	scw = 0.0
	w = 0.0	
	size = len(list1)
	i = 0
	NewSample = []
	while (i < size):
		if (list1[i] < .5):
			#Cloudy
			i += 1
			if (list1[i] <.1):
				#CS
				i += 1
				if (list1[i] < .8):
					#CSR
					i +=1
					if (list1[i] < .99):
						#WCSR
						NewSample.append(list1[i-3])
						NewSample.append(list1[i-2])
						NewSample.append(list1[i-1])
						NewSample.append(list1[i])
					i += 1	
				else:
					#CS~R
					i += 1
					if (list1[i] < .90):
						NewSample.append(list1[i-3])
						NewSample.append(list1[i-2])
						NewSample.append(list1[i-1])
						NewSample.append(list1[i])
					i += 1	
			else:
				#C~s
				i +=1
				if (list1[i] < .8):
					#C~SR
					i += 1
					if (list1[i] < .9):
						NewSample.append(list1[i-3])
						NewSample.append(list1[i-2])
						NewSample.append(list1[i-1])
						NewSample.append(list1[i])
					i += 1	
				else:
					i += 2	
		else: i += 3					
		
	j = 0
	while (j < len(NewSample)):
		if (NewSample[j] < .5):
			#Cloudy
			j += 1
			if (NewSample[j] < .1):
				scw += 1		
		j += 3				
	return scw / (len(NewSample)/4)					
					
									


def main():
	
	print "1 A) Prior Sampling P(c=true) =",(c_true_sample(sample))
	print "1 B) Prior Sampling P(c=true | rain=true) =",(c_given_r_sample(sample))
	print "1 C) Prior Sampling P(s=true | w=true) =",(s_given_w_sample(sample))
	print "1 D) Prior Sampling P(s=true | c=true, w=true) =",(s_given_c_w(sample))
	print "\n2 A) Exact P(c=true) =", c_exact()
	print "2 B) Exact P(c=true | rain=true) = ",(c_given_r_exact())
	print "2 C) Exact P(s=true | w = true) =",(s_given_w_exact())
	print "2 D) Exact P(s=true | c=true,w=true) =",(s_given_c_w_exact())
	print "\n For Prior Sampling Errors are:"
	print "A)Error is",(abs((c_true_sample(sample)-c_exact())))
	print "B)Error is",(abs((c_given_r_sample(sample))-(c_given_r_exact())))
	print "C)Error is",(abs(((s_given_w_sample(sample))-(s_given_w_exact()))))
	print "D)Error is",(abs((s_given_c_w_exact())-(s_given_c_w(sample))))
	print "\n3 A) Rejection Sampling P(c=true) =",(c_reject_sample(sample))
	print "3 B) Rejection Sampling P(c=true | rain= true) =",(c_r_reject(sample))
	print "3 C) Rejection Sampling P(s=true | w= true) =",(s_w_reject(sample))
	print "3 D) Rejection Sampling P(s=true | c=true, w= true) =",(s_c_w_reject(sample))
	print "\nFor Rejection Sampling Errors are:"
	print "A)Error is",(abs(((c_reject_sample(sample)))-c_exact()))
	print "B)Error is",(abs(((c_r_reject(sample)))-(c_given_r_exact())))
	print "C)Error is",(abs(((s_w_reject(sample)))-(s_given_w_exact())))
	print "D)Error is",(abs(((s_c_w_reject(sample)))-s_given_c_w_exact()))
	print "Errors are the same when w is a condition, since all 4 variables are necessary \nOtherwise, Rejection Sampling has better error because of a higher sample size"
	
	
main()