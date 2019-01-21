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
print "Loading data.."
X = np.loadtxt('data/data.txt', delimiter=',')
Y = np.zeros((l, X.shape[1]))
d = X.shape[1]
n = X.shape[0]

print "Data loaded."
print "l = " + str(l)
print "n = " + str(n)
print "d = " + str(d)
print "X is " + str(X.shape)
print "Y is " + str(Y.shape)
i = 0
while i < n:
	rowWasZero = False
	# get first zero row
	firstZeroRow = 0
	for j in range(l):
		if(isRowZero(Y[j])):
			firstZeroRow = j
			break
	# got first zero row in firstZeroRow. Fill it till the end. i should not exceed n-1
	for j in range(firstZeroRow, l):
		if(i < n):
			Y[j] = X[i]
			i += 1
		else:
			break
	# matrix filled
	# print ('Filled matrix. i = ' + str(i))
	u, s, vh = np.linalg.svd(Y, full_matrices=True)
	delta = (s[l/2])*(s[l/2])
	new_s = np.zeros((min(l,d)))
	for j in range(min(l,d)):
		temp = s[j]*s[j] - delta
		if(temp > 0):
			new_s[j] = math.sqrt(temp)
	# create 100x90 diagonal matrix
	new_s_matrix = np.zeros((l, d))
	for j in range(len(new_s)):
		new_s_matrix[j][j] = new_s[j]
	Y = np.matmul(new_s_matrix, vh)

print "Calculating norms for comparison:"
yty = np.matmul(Y.T, Y)
xtx = np.matmul(X.T, X)
norm = np.linalg.norm(xtx - yty)
print "xtx - yty norm = \t" + str(norm)
print "norm(X)^2/l = \t\t" + str(math.pow(np.linalg.norm(X), 2)/l)