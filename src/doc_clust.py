# Document Clustering using K-means clustering algorithm

import random
import math
from dataset import data,doc_title

# Distance calculation using Pearson Correlation Score
def distance(v1,v2):
	# Sums 
	sum1=sum(v1)
	sum2=sum(v2)

	# Sums of the squares
	sum1Sq=sum([pow(v,2) for v in v1])
	sum2Sq=sum([pow(v,2) for v in v2])

	# Sum of the products
	pSum=sum([v1[i]*v2[i] for i in range(len(v1))])

	# Calculate r (Pearson score)
	num=pSum-(sum1*sum2/len(v1))
	den=math.sqrt((sum1Sq-pow(sum1,2)/len(v1))*(sum2Sq-pow(sum2,2)/len(v1)))

	if den==0:
		return 0
	
	return 1.0-num/den


# The kmeans algorithm 
def kmeans(data,k):
	# To generate points for each word : (min count,maximum count)
	points=[]
	for i in range(len(data[0])): # For every word
		word_freq=[]
		for row in data:
			word_freq.append(row[i])
		points.append((min(word_freq),max(word_freq)))

	# Generate random centroids
	cluster=[]
	for i in range(k):
		cluster.append([])
		for j in range(len(data[0])):
			cluster[i].append(random.random()*(points[i][1]-points[i][0])+points[i][0])

	# Finds centroid for each row
	prev=None
	curr=[]
	while True:
		for i in range(k):
			curr.append([])

		for j in range(len(data)):
			row=data[j]

			minrow=0
			for i in range(k):
				d=distance(cluster[i],row)
				if d<distance(cluster[minrow],row): 
					minrow=i
			curr[minrow].append(j)

		# If clusters remain the same, break and come out of loop
		if prev==curr:
			break
		prev=curr

		# Move the centroids to the average of their members
		for i in range(k):
			avgs=[0.0]*len(data[0])
			if len(curr[i])>0:
				for rowid in curr[i]:
					for m in range(len(data[rowid])):
						avgs[m]+=data[rowid][m]
				for j in range(len(avgs)):
					avgs[j]/=len(curr[i])
				cluster[i]=avgs

	return curr

print 'Enter the number of clusters required'
k=input()


clusters=kmeans(data,k)

# To obtain the names of documents in cluster
doc_cluster=[]
for i in range(k):
	doc_cluster.append([])
	for j in clusters[i]:
		if doc_title[j] not in doc_cluster[i]:
			doc_cluster[i].append(doc_title[j])

for i in doc_cluster:
	print i