# Dragon Generator
In order to practice my skills in AI, I decided to make this project from scratch. I collected all the data by using different websites' APIs and made two neural networks to process the data before feeding the images to the StyleGAN2 neural network.

## Data collection
I collected the majority of images from the [e926](https://e926.net) imageboard website, using their API. In total, I gathered about 20000 images.

## Data processing
Processing all 20000 images manually is a tedious task, so I trained two neural networks to do it for me. First, I needed to detect all faces on an image to crop them. Second, I classified all the cropped faces into dragons and not dragons.

### Face detector
To train the face detector, I used the [mmdetection](https://github.com/open-mmlab/mmdetection) library to speed up the process of building the neural network architecture. More specifically, I used RetinaNet R50 trained on coco as a model to perform fine tuning on.

### Dragon face classifier
The original pytorch implementation of ResNet18 was used as a base for the dragon face classifier. I only changed the last layer so there are only two classes (dragon and not dragon).

## StyleGAN2
I used the following implementation of StyleGAN2 [stylegan2_pytorch](https://github.com/lucidrains/stylegan2-pytorch).

## Colab links
1. Face detector training [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1gLNjXIWAP3kwQ7bwTy2GLHJ4M1XL11JA?usp=sharing)
2. Face classifier training [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1SvVH4eBTtIf-bPefr44rUr6i9Gljh3Ce?usp=sharing)
3. Data collection [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Zv6-vklI_CpAlFB2k9HQpedKClW_KhBM?usp=sharing)
4. StyleGAN2 training and model testing [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/114eHMP7354KiCp8Xrffzacv6MUtWQNQL?usp=sharing)

## Results
![Results](https://i.imgur.com/bca5Nu7.png)
