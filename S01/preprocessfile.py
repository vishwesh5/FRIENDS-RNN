f = open('0101.txt')
lines = f.readlines()

file_ = open('0101_new.txt', 'w')

for line in lines:
	if(len(line) != 1):
		print(len(line))
		file_.write(line.strip("\n"))
file_.close()
