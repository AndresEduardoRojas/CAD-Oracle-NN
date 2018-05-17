#!/usr/bin/env python3

#Representation of a Perceptron using nNode
import sys
sys.path.iappend('/home/andres/Desktop/Programming/python/CAD-Oracle-NN/NN_Implementation/Python Modules')
import nNode as node

class perceptron(object):
	"""docstring for perceptron"""
	def __init__(self, numNodes):
		self._layer = []
		for n in range(numNodes):
			self._layer.append(node.neuron())
	
	def output(self):
		


	#def setInputStream(self, filePointer):


def main():
	print("OK")

if __name__ == '__main__': main()		

