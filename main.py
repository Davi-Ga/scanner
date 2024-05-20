import matplotlib.pyplot as plt
from utils.processing import ImageProcessing
from pdf2image import convert_from_path
import numpy as np

from PIL import Image
import os

file_path = 'data/foto1.jpeg'
filename, file_extension = os.path.splitext(file_path)

if file_extension.lower() == '.pdf':
    images = convert_from_path(file_path)
elif file_extension.lower() in ['.jpg', '.png', '.jpeg']:
    images = [Image.open(file_path)]
else:
    print(f'Unsupported file type: {file_extension}')

# Converta a imagem PIL em uma matriz numpy
img = np.array(images[0])
# Crie uma instância da classe ImageProcessing
processor = ImageProcessing()

enhanced_img = processor.enhance_image(img)
blank_page = processor.get_blank_page(enhanced_img)
background = processor.get_background(blank_page)
edge = processor.edge_detection(background)

# Suponha que 'img' é a sua imagem e 'canny' é a imagem após a detecção de borda
contours = processor.get_contours(img, edge)

# Use plt.imshow para mostrar a imagem
plt.imshow(contours, cmap='gray')
plt.show()