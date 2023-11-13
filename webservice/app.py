import os
import time
from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import torch
import torchvision.transforms as transforms
import torch.nn as nn
import torchvision
from PIL import Image
import json

app = Flask(__name__, static_folder='/app/webpage/static', template_folder='/app/webpage')

# Instantiate the model
model = torchvision.models.resnet50(pretrained=True)
num_ftrs = model.fc.in_features

# Replace the last fc layer
model.fc = nn.Linear(num_ftrs, 50)

# Initialize the fc layer with Xavier normal initialization
nn.init.xavier_normal_(model.fc.weight)

# Load the model
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
checkpoint = torch.load('/app/checkpoint.pth.tar', map_location=device)
model.load_state_dict(checkpoint['resnet50_state_dict'])
model = model.to(device)
model.eval()

@app.route('/', methods=['GET'])
def index():
    copyright = "Джассал Навмит Сингх (Navmeet Jassal). All rights reserved."
    return render_template('index.html', copyright=copyright, current_time=time.time(), image_loc="")

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(os.path.join('webpage', 'uploads'), filename)

@app.route('/upload_image', methods=['POST'])
def upload_image():
    image_file = request.files['image']  # Changed 'image_file' to 'image'
    base_dir = os.path.abspath(os.path.dirname(__file__))
    image_location = secure_filename(image_file.filename)

    # Ensure the directory exists
    os.makedirs(os.path.join(base_dir, 'webpage', 'uploads'), exist_ok=True)

    image_file.save(os.path.join(base_dir, 'webpage', image_location))
    pred = predict_image(os.path.join(base_dir, 'webpage', image_location))
    return render_template('index.html', prediction=pred, image_loc=image_location)

def predict_image(image_path):
    """Use PyTorch to make a prediction."""
    # Process image
    img = Image.open(image_path)
    transform = transforms.Compose([
        transforms.Resize((224,224)),
        transforms.ToTensor()
    ])
    img_t = transform(img)
    batch_t = torch.unsqueeze(img_t, 0)

    # Predict
    out = model(batch_t)
    _, index = torch.max(out, 1)

    # Load subclasses
    with open('subclasses.json', 'r') as f:
        subclasses = json.load(f)

    return subclasses[str(index.item())]

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)