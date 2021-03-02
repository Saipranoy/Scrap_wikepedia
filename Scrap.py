# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 11:02:38 2021

@author: Sai Praneeth S
"""
import nltk
import bs4 as bs
import urllib
import re

# to remove all the words like {the, is , was, etc.}
from nltk.corpus import stopwords
nltk.download('punkt')

# get the data source
source = urllib.request.urlopen('https://en.wikipedia.org/wiki/Milton_Keynes').read()

#parse the data to required format using beautiful soup
#2 parameters: source, format
soup = bs.BeautifulSoup(source,'lxml')

# fetching the data from all text in <p>
text= ""
for paragraph in soup.find_all('p'):
    text += paragraph.text
    
text = re.sub(r'\[[0-9]*\]',' ',text)
text = re.sub(r'\s+',' ', text)
text = text.lower()
text = re.sub(r'\([0-9a-zA-Z:/.-]*\)',' ',text)
text = re.sub(r'\s+', ' ', text)
text = re.sub(r'\d',' ', text)
text = re.sub(r'\s+',' ', text)

#preprocessing the data

# making text to sentences
sentences = nltk.sent_tokenize(text)

sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
print(sentences[0:10])

