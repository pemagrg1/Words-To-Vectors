######-------------GENSIM-------------
import gensim
from gensim.models import Word2Vec
gensim_model = "/Users/pemagurung/Desktop/work/blogg/Use of gensim/word2vec-GoogleNews-vectors/GoogleNews-vectors-negative300.bin.gz"
gensim_model = gensim.models.KeyedVectors.load_word2vec_format(gensim_model, binary=True, limit=100000)
gensim_vector = gensim_model['dog']
print(gensim_vector.shape)
##for 2D
test = gensim_vector.reshape(1, -1)
print test
