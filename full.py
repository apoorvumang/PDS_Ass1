import numpy as np
import math
import datetime
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression

epsilon = 0.00000001
def isRowZero(row):
	global epsilon
	for entry in row:
		if(entry < 0):
			entry = -entry
		if(entry > epsilon):
			return False
	return True


def getAlgoScores(reg, x_train, y_train, x_test, y_test):
	reg.fit(x_train, y_train)
	y_pred = reg.predict(x_test)
	score = r2_score(y_test, y_pred)
	return score


X = np.load("data/data_full_numpy.npy")

#Y is first column
Y = X.T[0]
#removing first column
X = X.T[1:].T


num_test = (len(X)*2)/10

#divide test and train
X_train = X[:-num_test]
X_test = X[-num_test:]

Y_train = Y[:-num_test]
Y_test = Y[-num_test:]

print "Starting training"
clf = LogisticRegression(random_state=0, solver='lbfgs',
                         multi_class='multinomial', verbose=1).fit(X_train, Y_train)
print "Training done."

y_predict = clf.predict(X_test)
print y_predict[:20]
print Y_test[:20]

score = r2_score(Y_test, y_predict)
print score

# print("Doing linear regression.")
# reg = linear_model.LinearRegression()
# print getAlgoScores(reg, X_train, Y_train, X_test, Y_test)

# # reg = linear_model.RidgeCV(alphas=[0.1, 1.0, 10.0], cv=3)
# # print getAlgoScores(reg, X_train, Y_train, X_test, Y_test)

# # reg = linear_model.Lasso(alpha=0.1)
# # print getAlgoScores(reg, X_train, Y_train, X_test, Y_test)

# #apply PCA on X

# print("Doing PCA")
# pca = PCA(n_components=90, svd_solver='full')
# X_new = pca.fit_transform(X)

# X_train = X_new[:-num_test]
# X_test = X_new[-num_test:]

# print("Doing linear regression on reduced dimension X")
# reg = linear_model.LinearRegression()
# print getAlgoScores(reg, X_train, Y_train, X_test, Y_test)
