import torch
import numpy as np
from PIL import Image

def calculate_ema(vec, n=10):
    beta = 2/(n+1)
    v = vec
    for i in range(0,vec.shape[1]):
        if i != 0:
            v[:, i] = beta*(v[:, i] - v[:, i-1]) + v[:, i-1]
        else:
            v[:, i] = torch.mean(v[:, 0:n])
    
    return v

def generate_random(loader, trunc_psi=0.6):
	noise   = torch.randn(1, 512)
	images = generate_from_noise(loader, noise, trunc_psi=trunc_psi)
	return images, noise.numpy()

def generate_from_noise(loader, noise, trunc_psi=0.6, ema = False, ema_n = 10):
	all_imgs = []
	if ema:
		noise = calculate_ema(noise, n=ema_n)

	for i in range(0, 4):
		styles  = loader.noise_to_styles(noise, trunc_psi = trunc_psi) 
		images  = loader.styles_to_images(styles)[0]
		all_imgs.append(Image.fromarray(np.einsum('ijk->jki', images.numpy()*255).astype(np.uint8)).quantize())

	return all_imgs