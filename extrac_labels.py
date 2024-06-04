import torch
import pandas as pd

# Model
model = torch.hub.load('./yolov5', 'custom',source='local',path='yolov5/runs/train/exp8/weights/best.pt', force_reload=True)

# Image
img = 'Untitled.jpg'

# Inference
results = model(img)
results.print()
results.show()
result_Labels= (results.pandas().xyxy[0])
# print(result_Labels['name'][0])
result_Labels['name'].to_csv('labels_data.txt',header=None,index=False)

lines = open('labels_data.txt', 'r').readlines()
lines_set = set(lines)
out  = open('labels_data.txt', 'w')
for line in lines_set:
    out.write(line)