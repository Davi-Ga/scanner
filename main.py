import matplotlib.pyplot as plt
from utils.processing import ImageProcessing
from utils.detecting import DetectingCorner
from pdf2image import convert_from_path
import numpy as np

from PIL import Image
import os

file_path = "data/ponto16.jpg"
filename, file_extension = os.path.splitext(file_path)

if file_extension.lower() == ".pdf":
    images = convert_from_path(file_path)
elif file_extension.lower() in [".jpg", ".png", ".jpeg"]:
    images = [Image.open(file_path)]
else:
    print(f"Unsupported file type: {file_extension}")

# Converta a imagem PIL em uma matriz numpy
img = np.array(images[0])
# Crie uma instância da classe ImageProcessing
processor = ImageProcessing()
detect = DetectingCorner()

resized_img = processor.resize_image(img, 1080)
enhanced_img = processor.enhance_image(resized_img)
blank_page = processor.get_blank_page(enhanced_img)
background = processor.get_background(blank_page)
edge = processor.edge_detection(background)

contours, page = processor.get_contours(img, edge)

points = np.squeeze(detect.get_points(img, page))
print(points)
corners = detect.order_points(points)
 
destination_corners = detect.get_destination(corners)

final = detect.perspective_transform(destination_corners, corners, resized_img)
# Use plt.imshow para mostrar a imagem
plt.imshow(final, cmap="gray")
# Salve a imagem
final_image = Image.fromarray(final)
# Salve a imagem
final_image.save('contours.png')