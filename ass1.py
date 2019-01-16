f = open("data.txt", "r")

X = []
Y = []

for line in f:
	line = line.strip()
	tokens = line.split(',')
	x = []
	for token in tokens:
		x.append(float(token))
	X.append(x)
print(len(X))
print(len(X[0]))