from flask import Flask, request, render_template, redirect, jsonify, send_from_directory
from stylegan2_pytorch import ModelLoader
from utils import generate_random, generate_from_noise
from io import BytesIO
import torch
import json
import base64
import gc
import os

loader = ModelLoader(
    base_dir = 'StyleGAN2', 
    name = 'default'  
)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def send_index():
    gc.collect()
    return send_from_directory('./www', "index.html")

@app.route('/<path:path>', methods=['GET'])
def send_root(path):

    gc.collect()
    return send_from_directory('./www', path)

@app.route('/api/image', methods=['POST'])
def generate_image():

    file = request.form.get('array')#request.get_json(silent=True)
    file_dict = json.loads(file)

    latent_vector = torch.FloatTensor([value for key, value in file_dict.items()]).unsqueeze(0)
    #print(torch.randn(1, 512).type(), latent_vector.type(), type(torch.randn(1,512)), type(latent_vector))
    img = generate_from_noise(loader, latent_vector, trunc_psi=0.6, ema = True, ema_n = 50)

    byte_file = BytesIO()
    img[0].save(byte_file, save_all=True, append_images=img[1:], format='GIF', loop=0)
    byte_file = base64.b64encode(byte_file.getvalue())
    
    items = {'img':str(byte_file)[2:-1]}

    response = {'pred':items}
    
    del byte_file
    
    gc.collect()
          
    return jsonify(response)
'''  
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', #0.0.0.0
        port=int(os.environ.get('PORT', 8080)))
'''
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', 
        port=int(os.environ.get('PORT', 8080)))