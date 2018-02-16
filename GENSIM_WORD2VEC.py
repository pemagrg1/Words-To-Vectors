#---GENSIM WORD2VEC---
import gensim, logging
sentences = [['one', 'two']]
model = gensim.models.Word2Vec(sentences, min_count=1)
print(model.wv['one'])