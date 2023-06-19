# cnn_test

该项目是基于Vue3+vite搭建的，Cnn_test的实验内容是基于torch库搭建Cnn卷积神经网络来对MIT的Indoor scenes 数据集进行图像分类。该项目搭建的网站所实现的功能有通过Markdown-it插件来展示实验过程、实验代码和实验结果；通过python后端对已训练好的模型进行加载，从而实现上传图片并且分类的功能。

## vue项目的依赖安装

```sh
npm install
```

### 运行与热部署

```sh
npm run dev
```

### 运行与打包

```sh
npm run build
```

## Python后端所需库

```python
import torch 
import torch.nn as nn 
from torchvision import transforms 
import numpy as np 
import matplotlib.pyplot as plt 
import pathlib 
from PIL import Image
from torchvision.datasets import ImageFolder
import random as rd
from torch.utils.data import SubsetRandomSampler, Dataset, DataLoader,random_split
import torch.nn.functional as F
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
import pandas as pd
import torchsummary
import torchvision.models as models
import math
import os
import torch.utils.data.sampler as sampler
```

