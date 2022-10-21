import sys

#http://www.scipy.org/
try:
	import numpy as np
	from numpy.linalg import norm
except:
	print("Error: Requires numpy from http://www.scipy.org/. Have you installed scipy?")
	sys.exit() 

def removeDuplicates(list):
	""" remove duplicates from a list """
	return set((item for item in list))


def cosine(vector1, vector2):
	""" related documents j and q are in the concept space by comparing the vectors :
		cosine  = ( V1 * V2 ) / ||V1|| x ||V2|| """
	A = np.array(vector1)
	B = np.array(vector2)
	cos = np.dot(A,B) / (norm(A, axis=1) * norm(B))
	return cos
