f = open("data/data.txt", "r")
fw = open("data/small.txt", "w")

maxLines = 10000
n = 0
for line in f:
	fw.write(line)
	n += 1
	if(n >= maxLines):
		break