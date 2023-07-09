from PIL import Image
import requests
from io import BytesIO
import torch
from torch.utils.data import Dataset,DataLoader
from gensim.models import KeyedVectors
from config import word2vec_path
import numpy as np

word2vec_model = KeyedVectors.load_word2vec_format(word2vec_path,binary=True)

def load_image(url):
    if url == None: return None
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return np.array(img)

def get_text():
    pass


def vectorize(sentence):
    words = sentence.split()
    words_vecs = [word2vec_model.get_vector(word) for word in words if word in word2vec_model.key_to_index]
    if len(words_vecs) == 0:
        return np.zeros(400)
    words_vecs = np.array(words_vecs)
    return np.mean(words_vecs,axis=0)
class FBDataset(Dataset):
  def __init__(self,data, transforms = None, mode ='train'):
        super().__init__()
        self.transforms = transforms
        self.mode = mode
        self.data = data
  def __getitem__(self,idx):
        if self.mode == "train" or self.mode == "val":
            id = self.data[idx]['id']
            name = self.data[idx]['name']
            ava = load_image(self.data[idx]['ava'])
            ava = self.transforms(ava) if ava is not None else None
            cover = load_image(self.data[idx]['cover'])
            cover = self.transforms(cover) if cover is not None else None
            intro = self.data[idx]['introduction']
            no_fr = self.data[idx]['nums_of_friend']
            no_im = self.data[idx]['nums_of_images']
            no_vd = self.data[idx]['nums_of_videos']
            no_ab = self.data[idx]['nums_of_albums']
            contries = self.data[idx]['countryside']
            add = self.data[idx]['address']
            rela = self.data[idx]['rela']
            return id, name, ava, cover, intro, no_fr, no_im, no_vd, no_ab, add, rela
  def __len__(self):
    return len(self.data)
