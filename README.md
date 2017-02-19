# Document-Clustering
Given set of documents are clustered into required number of clusters using K-means clustering algorithm

********************************************************************************************************

There are two sub directories in this repository:

1. src

2. documents

src contains the source code in doc_clust.py file. The dataset.py file in this directory is used to extract the data from the dataset.csv into lists that are used by the main code.

documents contains the documents : cs1.txt,cs2.txt,ec1.txt,ec2.txt,mech1.txt,mech2.txt . These are the documents used for clustering purpose. The dataset.py file in this sub-directory extracts the documents in the directory, to generate a csv file that contains count of all words pressent in all the documents.


********************************************************************************************************

The documents to be clustered can be placed in documents directory and dataset.py is run using the terminal command - "python dataset.py" to generate the dataset.csv file.

This dataset.csv file must be placed in the src directory and doc_clust.py must be run using terminal command - "python doc_clust.py". Then in the output, specify the number of clusters required. 

Thus lists of clusters are displayed on the terminal and the documents are clustered.

********************************************************************************************************
