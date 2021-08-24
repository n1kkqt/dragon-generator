from stylegan2_pytorch import ModelLoader
from utils import calculate_ema
import torch
import numpy as np
from PIL import Image

loader = ModelLoader(
    base_dir = 'StyleGAN2', 
    name = 'default'  
)

def generate_random(loader, trunc_psi=0.6):
	noise   = torch.randn(1, 512)
	images = generate_from_noise(loader, noise, trunc_psi=trunc_psi)
	return images, noise.numpy()

def generate_from_noise(loader, noise, trunc_psi=0.5, ema = True, ema_n = 10):
	if ema:
		noise = calculate_ema(noise, n=ema_n)

	styles  = loader.noise_to_styles(noise, trunc_psi = trunc_psi) 
	images  = loader.styles_to_images(styles)[0]
	return Image.fromarray(np.einsum('ijk->jki', images.numpy()*255).astype(np.uint8))

for i in range(0, 200):
	img, noise = generate_random(loader)
	img.save(f'imgs/{i}.jpg', "JPEG")