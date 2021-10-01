#!/usr/bin/env python3

import sys 
from scipy.constants import g
#from scipy import constants

def compute_d(initial_velocity,friction_coeff):
	return ((1/2)*(initial_velocity**2)/(friction_coeff*(scipy.constants.g)))
	
if __name__ == "__main__":
	initial_velocity = float(sys.argv[1])	#to be enetered in km/h
	friction_coeff = float(sys.argv[2])		
	initial_velocity = initial_velocity/3.6	#converting it into m/s
	print("Braking distance : ", compute_d(initial_velocity, friction_coeff))

#sample input 1 : 120 0.3
#sample input 2 : 50 0.3
