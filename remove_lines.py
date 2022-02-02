"""
Simple script to remove all non-text lines from the panopto captions and save manual time later on

"""
def remove_lines_containing(word, verbose=True):
	"""
	this function was deprecated in favour of a one-liner on the internet
	"""
	for line in lines:
		# remove filler words
		if word in line:
			if verbose:
				print("Original line: \n", line)
				seps = line.split(word)
				print("Separated strings: \n", seps)
				if len(seps)==2:
					line=seps[0]+seps[-1]
				elif len(seps)==1:
					line=seps[0]
				print("New line: \n", line)
				print("\n")
			else:
				#print("Original line: \n", line)
				seps = line.split(word)
				#print("Separated strings: \n", seps)
				if len(seps)==2:
					line=seps[0]+seps[-1]
				elif len(seps)==1:
					line=seps[0]
				#print("New line: \n", line)
				#print("\n")

def remove_lines_containing_quick(excludedWord, strlist):
	"""
	pretty self-explanatory
	"""
	newLines = []
	for line in strlist:
    		newLines.append(' '.join([word for word in line.split() if word != excludedWord]))
	return newLines


### end of function definitions

# setup
with open("lecture1.txt") as f:
	lines = f.readlines()
newfile = open("lecture1_modified.txt","w")
bad_chars = ["0","1","2","3","4","5","6","7","8","9", ""]


# remove non-text lines
for line in lines:
	if line[0] in bad_chars:
		lines.remove(line)

	
newlines = remove_lines_containing_quick("like", strlist=lines)	
newlines = remove_lines_containing_quick("So", strlist=newlines)


#for i in range(50,60):
#	print(newlines[i], "\n")



# write modifications to new file
for line in newlines:
	newfile.write(line)
newfile.close()
