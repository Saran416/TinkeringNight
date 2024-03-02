from sentence_transformers import SentenceTransformer,util
model = SentenceTransformer('all-MiniLM-L6-v2')


sentences1 = ['Amogh are you there',
    'Amogh can you answer this']


embeddings1 = model.encode(sentences1)

def isSimilar():
    sentence = 'Amogh are you here'

    embeddings2 = model.encode(sentence)

        #Compute cosine similarity between all pairs
    cos_sim = util.cos_sim(embeddings1, embeddings2)*100

    for one in cos_sim:
        if(one > 80):
            print("similar")
            return True
        else:
            print("not similar")
            return False

