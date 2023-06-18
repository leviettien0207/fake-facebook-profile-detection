import torch
from torch.utils.data import Dataset,DataLoader
from torch import nn
from torch.nn import Sequential
from torch import optim
import torchvision
from torchvision import models
import torchvision.transforms as T
class MulBert(nn.Module):
  def __init__(self):
        super(MulBert, self).__init__()
        self.Bert_1 = BertModel.from_pretrained('bert-base-uncased')
        self.Bert_2 = BertModel.from_pretrained('bert-base-uncased')
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(768*2, 1000),
            nn.Dropout(0.2),
            nn.ReLU(),
            nn.Linear(1000, 724),
            nn.Dropout(0.2),
            nn.ReLU(),
            nn.Linear(724, 300),
        )

  def forward(
        self,
        sent_id_1, mask_1,
        sent_id_2 ,mask_2,
    ):  
        sent_id_1 = sent_id_1.squeeze(0)
        sent_id_2 = sent_id_2.squeeze(0)
        _ , outputs_1 = self.Bert_1(
            sent_id_1,attention_mask=mask_1, return_dict=False
        )
        _ , outputs_2 = self.Bert_2(
            sent_id_2,attention_mask=mask_2, return_dict=False
        )
        outputs = torch.cat((outputs_1,outputs_2),1)        
        outputs =  self.linear_relu_stack(outputs) # add hidden states and attention if they are here
        return outputs
class Dirsm(nn.Module):
  def __init__(self):
        super(Dirsm, self).__init__()
        self.visual = torch.hub.load('pytorch/vision:v0.10.0', 'inception_v3', pretrained=True)
        self.visual.fc = nn.Sequential(nn.Linear(in_features = 2048,out_features = 1000))
        self.text = MulBert()
        self.classifier = nn.Sequential(
            nn.Linear(in_features=1300,out_features=1000),
            nn.Dropout(0.2),
            nn.ReLU(),
            nn.Linear(in_features=1000,out_features = 512),
            nn.Dropout(0.2),
            nn.ReLU(),
            nn.Linear(in_features=512,out_features = 256),
            nn.Dropout(0.15),
            nn.ReLU(),
            nn.Linear(in_features=256,out_features = 1),
            nn.Dropout(0.1),
            nn.Sigmoid()
        )
  def forward(self,
        sent_id_1, mask_1,
        sent_id_2 ,mask_2,image):
        out1 = self.visual(image)
        out2 = self.text(sent_id_1, mask_1,
        sent_id_2 ,mask_2)
        out = torch.cat((out1,out2),1)
        out = self.classifier(out)
        return out