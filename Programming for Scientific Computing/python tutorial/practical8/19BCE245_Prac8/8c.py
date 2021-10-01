#!/usr/bin/env python3

# Design a python program that generates the 100 random variables and finds out the mean, median and mode for the same.
import random
import statistics

randomlist = random.sample(range(100000000), 100)
print("Random generated list : ",randomlist)
print("Mean : ",statistics.mean(randomlist))
print("Median : ",statistics.median(randomlist))
print("Mode : ",statistics.mode(randomlist))