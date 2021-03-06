"""
Simple script to remove all non-text lines from the panopto captions and save manual time later on

"""
def replace_word(oldWord, newWord, strlist):
	"""
	Does what it says on the tin
	"""
	newLines = []
	for line in strlist:
		newLines.append(line.replace(oldWord, newWord))
	return newLines




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

def remove_lines_containing_quick(excludedWord, strlist, newWord = ""):
	"""
	pretty self-explanatory, want to add ability to change a bad word into a better one too.
	"""
	newLines = []
	for line in strlist:
    		newLines.append(' '.join([word for word in line.split() if word != excludedWord]))
	return newLines


### end of function definitions

# setup
filename=input("Please type the (.txt) filename you want to modify in this directory: ")
with open(filename) as f:
	lines = f.readlines()
newname = filename.split(".txt")[0] + "_modified.txt"
newfile = open(newname,"w")
bad_chars = ["0","1","2","3","4","5","6","7","8","9", ""]


# remove non-text lines
for line in lines:
	if line[0] in bad_chars:
		lines.remove(line)

	
newlines = remove_lines_containing_quick("like", strlist=lines)	
newlines = remove_lines_containing_quick("So", strlist=newlines)
newlines = remove_lines_containing_quick("kind of", strlist=newlines)
newlines = remove_lines_containing_quick("right", strlist=newlines)
newlines = replace_word("Hubbert", "Hubbard", strlist=newlines)
newlines = replace_word("side", "site", strlist=newlines)
newlines = replace_word("letters", "lattice", strlist=newlines)
newlines = replace_word("face", "phase", strlist=newlines)
newlines = replace_word("metaphysics", "matter physics", strlist=newlines)
newlines = replace_word("block", "Bloch", strlist=newlines)
newlines = replace_word("election", "electron", strlist=newlines)
newlines = replace_word("Oh", "", strlist=newlines)
newlines = replace_word("caution", "Gaussian", strlist=newlines)
newlines = replace_word("week", "weak", strlist=newlines)
newlines = replace_word("Crown State", "ground state", strlist=newlines)
newlines = replace_word("feminisation", "thermalisation", strlist=newlines)
newlines = replace_word("kind of", "", strlist=newlines)
newlines = replace_word("lettuce", "lattice", strlist=newlines)
newlines = replace_word("letters", "lattice", strlist=newlines)
newlines = replace_word("London", "$\lambda", strlist=newlines)
newlines = replace_word("HBK", "$\hbar k$", strlist=newlines)
newlines = replace_word("cue", "$q$", strlist=newlines)
newlines = replace_word("Harvard", "Hubbard", strlist=newlines)
newlines = replace_word("ABC", "a BEC", strlist=newlines)
newlines = replace_word("B.C", "BEC", strlist=newlines)
newlines = replace_word("value function", "Wannier function", strlist=newlines)
newlines = replace_word("letter", "lattice", strlist=newlines)
newlines = replace_word("venue", "Wannier", strlist=newlines)
newlines = replace_word(" q ", " $q$ ", strlist=newlines)
newlines = replace_word(" p ", " $p$ ", strlist=newlines)
newlines = replace_word(" K ", " $k$ ", strlist=newlines)
newlines = replace_word(" minus K", " $-k$", strlist=newlines)
newlines = replace_word("Bunya", "Wannier", strlist=newlines)
newlines = replace_word("vanua", "Wannier", strlist=newlines)
newlines = replace_word("Letha", "lattice", strlist=newlines)
newlines = replace_word("crown states", "ground states", strlist=newlines)
newlines = replace_word("modern insulator", "MI", strlist=newlines)
newlines = replace_word("mild insulator", "MI", strlist=newlines)
newlines = replace_word("way function", "wavefunction", strlist=newlines)





#for i in range(50,60):
#	print(newlines[i], "\n")



# write modifications to new file
for line in newlines:
	newfile.write(line+"\n")
newfile.close()
