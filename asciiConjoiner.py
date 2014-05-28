
def main():
	fileA = open("fileA.txt").readlines()
	fileB = open("fileB.txt").readlines()
	fileC = open("fileC.txt",'w')

	startFileB = len(fileA) - len(fileB)

	if startFileB < 0:
		for i in range(startFileB, 0):
			fileC.write("\t\t\t\t\t\t"+fileB[i-startFileB])


		for index,line in enumerate(fileA):
			print line,
			print fileB[index]
			write = line.rstrip()+"\t\t\t\t"+fileB[index-startFileB]
			fileC.write(write),

	else:
		for i in range(0, startFileB):
			fileC.write(fileA[i])

		for index, line in enumerate(fileB):
			write = fileA[index+startFileB].rstrip() +"\t\t\t\t"+ line
			fileC.write(write),

if __name__ == '__main__':
	main()