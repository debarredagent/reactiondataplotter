#!/bin/python3
import math
from matplotlib import pyplot as plt
import threading
a = int(input("Please enter the number of inputs: "))
n = 1
x = []
y = []
z = []
p = []
q = []
r = []
s = []
while n <= a:
	if n ==1:
		c = float(input(f"Please enter the {n}st concentration: "))
	elif n ==2:
		c = float(input(f"Please enter the {n}nd concentration: "))
	else :
		c = float(input(f"Please enter the {n}th concentration: "))
	y.append(c)
	if n ==1:
                c = float(input(f"Please enter the {n}st time instance: "))
	elif n ==2:
                c = float(input(f"Please enter the {n}nd time instance: "))
	else :
                c = float(input(f"Please enter the {n}th time instance: "))

	x.append(c)
	n = n+1
def zero():
	plt.xlabel("t")
	plt.ylabel("Ca")
	plt.plot(x, y)
	plt.show()

def first():
	for a in y:
		z.append(math.log(a))
	plt.xlabel("t")
	plt.ylabel("ln(Ca)")
	plt.plot(x, z)
	plt.show()
def second():
	for a in y:
		r.append(1/a)
	plt.xlabel("t")
	plt.ylabel("1/(Ca)")
	plt.plot(x, r)
	plt.show()
	p = []
def third():
	for a in y:
		s.append(1/(a**2))
	plt.xlabel("t")
	plt.ylabel("1/(Ca)")
	plt.plot(x, s)
	plt.show()
	q = []

zero()
first()
second()
third()
