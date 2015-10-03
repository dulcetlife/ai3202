#Assignment 5



def inputAndRead():
	if len(sys.argv) != 3:
		print "Need to provide world and a value for ε!"
		return(False, False)
	elif sys.argv[1] != "World1.txt":
		print "Incorrect world provided! Need to be World1.txt"
		return(False, False)
	elif sys.argv[2] != int 
		print "Need to provide a value of ε!"
		return(False, False)
	else:
		m = sys.argv[1]
		return (m, sys.argv[2])