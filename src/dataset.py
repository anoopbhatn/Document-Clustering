# Python code to extract the document titles and the data of the count of words in documents
import csv

fileh=open('dataset.csv','r')

reader = csv.reader(fileh, delimiter=',')

i=1

# List to store title of documents
doc_title=[]

# List of lists that store the count of words
data=[]

for row in reader:
	# First row contains the words in all documents
	# That is not required currently for clustering
	if i==1:
		i+=1
		continue
		
	l=list(row)
	doc_title.append(l[0])
	data.append([float(x) for x in l[1:]])