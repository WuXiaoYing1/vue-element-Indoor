from flask import Flask, request, send_file
import torch # 张量、torch主库
import torch.nn as nn # 神经网络库
from torchvision import transforms # 图像预处理、转换
import numpy as np # 数组运算
import matplotlib.pyplot as plt # 绘制训练损失曲线、显示样本
import pathlib 
from PIL import Image 
from werkzeug.utils import secure_filename
import os
path='../public/image/'
class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()

        self.cnn = nn.Sequential(
            #3*256*256
            nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3,stride=1,padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(True),
            nn.MaxPool2d(kernel_size=3),
            #64*64*64
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(True) ,
            nn.MaxPool2d(kernel_size=3),
            #64*16*16
            nn.Conv2d(in_channels=64,out_channels=64,kernel_size=3,stride=1,padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(True),
            nn.MaxPool2d(kernel_size=1),
            nn.Conv2d(in_channels=64, out_channels=128,kernel_size=3,stride=1,padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(True),
            nn.MaxPool2d(kernel_size=3),
#             nn.AvgPool2d(2),
            nn.Conv2d(in_channels=128, out_channels=128,kernel_size=3,stride=1,padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(True),
            nn.MaxPool2d(kernel_size=1),
            nn.Conv2d(in_channels=128, out_channels=256, kernel_size=3, stride=1,padding=1),
            nn.BatchNorm2d(256),
            nn.AvgPool2d(3),
            nn.Flatten(),
#             nn.Dropout(p=0.31415926),
            nn.Linear(in_features=256*3*3, out_features=67),
        )

    def forward(self, x):
        x = self.cnn(x)
        return x

classes=['airport_inside', 'artstudio', 'auditorium', 'bakery', 'bar', 'bathroom', 'bedroom', 'bookstore', 'bowling', 'buffet', 'casino', 'children_room', 'church_inside', 'classroom', 'cloister', 'closet', 'clothingstore', 'computerroom', 'concert_hall', 'corridor', 'deli', 'dentaloffice', 'dining_room', 'elevator', 'fastfood_restaurant', 'florist', 'gameroom', 'garage', 'greenhouse', 'grocerystore', 'gym', 'hairsalon', 'hospitalroom', 'inside_bus', 'inside_subway', 'jewelleryshop', 'kindergarden', 'kitchen', 'laboratorywet', 'laundromat', 'library', 'livingroom', 'lobby', 'locker_room', 'mall', 'meeting_room', 'movietheater', 'museum', 'nursery', 'office', 'operating_room', 'pantry', 'poolinside', 'prisoncell', 'restaurant', 'restaurant_kitchen', 'shoeshop', 'stairscase', 'studiomusic', 'subway', 'toystore', 'trainstation', 'tv_studio', 'videostore', 'waitingroom', 'warehouse', 'winecellar']

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save('example.txt')
    return {'message': 'File uploaded successfully.'}

@app.route('/download', methods=['GET'])
def download():
    return send_file('example.txt', as_attachment=True)

@app.route('/sent', methods=['GET'])
def sent():
    return 'Hello'

@app.route('/identify', methods=['POST'])
def identify():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    # 加载模型并移动到对应设备
    if torch.cuda.is_available():
        model = torch.load('../public/21_model')
    else:
        model = torch.load('../public/21_model', map_location=torch.device('cpu'))
    model = model.to(device)
    file_obj = request.files.get('file')
    file =request.files['file']
    filename = secure_filename(file.filename)
    file_obj.save(os.path.join(path,file.filename))
    transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor()
    ])
    img = Image.open(os.path.join(path, file.filename))
    img =transform(img)
    sample = img.unsqueeze(0).to(device)
    prediction = model(sample)
    result = classes[prediction.argmax(-1)[-1]]
    # imgs=plt.imread(filename)
    # img.show()
    os.remove(os.path.join(path, file.filename))
    return result

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000,debug=True)