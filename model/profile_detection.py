from models import model
from config import word2vec_path
import numpy as np
from models.model import EarlyFusion
from config import *
import torch

def profile_detect(**kwargs:dict)->float:
    model = EarlyFusion()
    model.load_state_dict(torch.load(detection_model_path,map_location=torch.device('cpu')))
    print("load model done!")
    score = model(**kwargs)
    return score
def example():
    data = {
        'fbuid':'0123135481', 
        'name':"Hoàng",
        'introduction':None,
        'countryside':"Hà Nội",
        'address':"Vĩnh Phúc",
       'rela':0,
       'ava':None,
       'cover':None,
       'nums_of_friend':None,
       'nums_of_images':None,
       'nums_of_videos':2,
       'nums_of_albums':1,
       'old':18
    }
    print(profile_detect(**data))
example()