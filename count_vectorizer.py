#####-------------CountVectorizer------------
from sklearn.feature_extraction.text import CountVectorizer
text = ["hello!! my name is Pema and this is a sample text for testing"]
# create the transform
vectorizer = CountVectorizer()
# tokenize and build vocab
vectorizer.fit(text)
# summarize
# encode document
vector = vectorizer.transform(text)
# summarize encoded vector
print "---Vector", vector
print("---vector.shape",vector.shape)
print("---TYPE",type(vector))
print("---toarray",vector.toarray())
print("---vectorizer vocab",vectorizer.vocabulary_)
