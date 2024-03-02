from sentence_transformers import SentenceTransformer,util
import numpy as np
import cv2
import pyautogui

model = SentenceTransformer('all-MiniLM-L6-v2')


sentences1 = ['Amogh are you there',
    'Amogh can you answer this']


embeddings1 = model.encode(sentences1)


sentence = 'Amogh are you here'

embeddings2 = model.encode(sentence)

        #Compute cosine similarity between all pairs
cos_sim = util.cos_sim(embeddings1, embeddings2)*100

for one in cos_sim:
    if(one > 80):
        print("similar")
        image = pyautogui.screenshot() 
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR) 
        # writing it to the disk using opencv 
        cv2.imwrite("image1.png", image)
        
    else:
        print("not similar")
       

