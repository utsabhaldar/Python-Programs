import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
# TfidfVectorizer - This is used to convert text data into numerical values
from sklearn.metrics.pairwise import cosine_similarity
import os
display (os.getcwd())
os.chdir(r'C:\Users\DELL\Downloads\movies.csv')
data=open(r'C:\Users\DELL\Downloads\movies.csv')
movies_data =pd.read_csv('movies.csv')
data = csv.reader(data)
print(data)
# movies_data.head()