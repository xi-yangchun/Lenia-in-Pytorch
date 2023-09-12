import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from lenia import Lenia_Simple
from monitor import Monitor
from multiprocessing import Process

#a=torch.tensor(np.random.rand(1,1,200,200)).float()
a=torch.tensor(np.zeros((1,1,200,200))).float()
ls=Lenia_Simple(a,"exponential",g_mu=0.15,g_sigma=0.016,R=13,T=10)
for i in range(5):
    for j in range(4):
        ls.make_orbium_at(40+30*i,40+40*j)
m=Monitor()
m.run_single_channel(ls)