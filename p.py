f = open("data/data.txt", "r")
fw = open("data/50k.txt", "w")

maxLines = 50000
n = 0
for line in f:
	fw.write(line)
	n += 1
	if(n >= maxLines):
		break