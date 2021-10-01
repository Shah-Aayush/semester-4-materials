#!/usr/bin/python

a = 1

# Uses global because there is no local 'a' 
def f(): 
		print('Inside f() : ', a) 
	
# Variable 'a' is redefined as a local 
def g():
		a = 2
		print('Inside g() : ', a) 
	
# Uses global keyword to modify global 'a' 
def h():
		global a 
		a = 3
		print('Inside h() : ', a) 
	
# Global scope 
if __name__ == "__main__":
	print('original global var : ',a) 
	f() 
	print('After f() : global : ',a) 
	g() 
	print('After g() : global : ',a) 
	h() 
	print('After h() : global : ',a) 