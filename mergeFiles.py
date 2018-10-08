import os

def get_files(prefix):
	return sorted([f for f in os.listdir(prefix) if f.endswith(".txt")])

f = open("mergedfile.txt",'w')

for i in range(1,4):
	season="S0{}".format(i)
	prefix = "./"+season
	episodes = get_files(prefix)
	for f_t in episodes:
		fname = prefix+"/"+f_t
		with open(fname,'r') as epi:
			for line in epi.readlines():
				f.write(line.strip("\n"))
f.close()
