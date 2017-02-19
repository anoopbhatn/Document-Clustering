import os
import re

# executes ls command and stores the filenames in this directory in sample.txt
os.system("ls > sample.txt")

# Places the filenames in a list
files= [line.rstrip('\n') for line in open('sample.txt')]

# Common words that are to be ignored in the data matrix
common=['and','but','that','this','the','for','its','are','such']

# List that contains all the words collected from all documents
wordlist=[]

# Dictionary that keeps counts of words present in a document : {document:{word:count}...}
dataset={}

for i in files:
	i=i.lower()
	# Ignore these files since they are not part of documents to be clustered 
	if i=="sample.txt" or i=="dataset.py" or i=="dataset.csv":
		continue
	f1=open(i,"r")

	# Place the data read from the file in a string
	data = f1.read()

	# Split the data into words
	split_data=re.split('[^a-zA-Z\']',data)
	
	for j in split_data:
		# convert the word to lowercase
		j=j.lower()
		# Ignore the words with length less than 3 and also the common words
		if len(j) <= 2 or j in common:
			continue

		# Place the words into wordlist without repeatition
		if j not in wordlist:
			wordlist.append(j)

		# Build the dictionary as mentioned above
		dataset.setdefault(i,{})
		dataset[i].setdefault(j,0)
		dataset[i][j]+=1

# Generate a comma separated string of all words 
line1=','.join(wordlist)

# Write the generated string of words to the dataset file
f2=open("dataset.csv","a")
f2.write(line1+'\n')

# Loop for every document
for (k,v) in dataset.items():
	linen=k
	# Loop for every word
	for i in wordlist:
		if i in v:
			# Place the count of occurence of word if present
			linen+=(','+str(v[i]))
		else:
			# Place zero if the word is not present
			linen+=(','+str(0))
	linen+='\n'
	# Write this line to dataset file
	f2.write(linen)

f2.close()
