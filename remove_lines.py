"""
Simple script to remove all non-text lines from the panopto captions and save manual time later on

"""

with open("lecture1.txt") as f:
	lines = f.readlines()

bad_chars = ["0","1","2","3","4","5","6","7","8","9", ""]

for line in lines:
	if line[0] in bad_chars:
		lines.remove(line)


#for line in lines:
#	print(line, "\n")

newfile = open("lecture1_modified.txt","w")
for line in lines:
	newfile.write(line)
newfile.close()
