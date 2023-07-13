import pandas as pd
from datasets import FBDataset
#import gensim
#from gensim.models import KeyedVectors
from config import word2vec_path
import numpy as np
from models.model import EarlyFusion
from config import *
import torch 

df = pd.read_csv("data_sample_1k.csv",)
#fbuid', 'name', 'introduction', 'countryside', 'address',
 #      'rela', 'ava', 'cover', 'nums_of_friend', 'nums_of_images',
 #     'nums_of_videos', 'nums_of_albums', 'Label'
label = df.pop('Label')
id = df.pop('fbuid')
#word2vec_model = KeyedVectors.load_word2vec_format(word2vec,binary=True)
# def vectorize(sentence):
#     words = sentence.split()
#     words_vecs = [word2vec_model.get_vector(word) for word in words if word in word2vec_model.key_to_index]
#     if len(words_vecs) == 0:
#         return np.zeros(400)
#     words_vecs = np.array(words_vecs)
#     return np.mean(words_vecs,axis=0)
def profile_detect(**kwargs:dict):
    model = EarlyFusion()
    model.load_state_dict(torch.load(detection_model_path))
    print("load model done!")
    score = model(**kwargs)
    return score