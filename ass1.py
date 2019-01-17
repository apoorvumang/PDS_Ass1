import numpy as np
import math
epsilon = 0.00000001
def isRowZero(row):
	global epsilon
	for entry in row:
		if(entry < 0):
			entry = -entry
		if(entry > epsilon):
			return False
	return True


l = 100
X = np.loadtxt('data/small.txt', delimiter=',')
Y = np.zeros((l, X.shape[1]))
d = X.shape[1]
n = X.shape[0]
print X.shape
print Y.shape

# print len(Y[0])
# exit(0)
# print isRowZero(X[0])
# lastRowChecked = -1
for i in range(n):
	rowWasZero = False
	for j in range(l):
		if isRowZero(Y[j]):
			Y[j] = X[i]
			rowWasZero = True
			break
	if(rowWasZero == False):
		print ('Filled matrix')
		u, s, vh = np.linalg.svd(Y, full_matrices=True)
		delta = (s[l/2])*(s[l/2])
		new_s = np.zeros((d))
		for j in range(d):
			temp = s[j]*s[j] - delta
			if(temp > 0):
				new_s[j] = math.sqrt(temp)
		# create 100x90 diagonal matrix
		new_s_matrix = np.zeros((l, d))
		for j in range(len(new_s)):
			new_s_matrix[j][j] = new_s[j]
		Y = np.matmul(new_s_matrix, vh)

yty = np.matmul(Y.T, Y)
xtx = np.matmul(X.T, X)

norm = np.linalg.norm(xtx - yty)
print norm