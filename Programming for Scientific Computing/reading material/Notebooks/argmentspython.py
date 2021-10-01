import sys
def myfunction(arg1,*argv):
	print ("First argument :", arg1) 
	n = len(sys.argv)
	for i in range(n-1):
		print("Next argument through *argv :", sys.argv[i+1])
		# print(sys.argv[i])
		
if __name__=="__main__":
	myfunction(sys.argv[1],sys.argv)
	print(sys.argv[0])