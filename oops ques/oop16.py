# Display an Image and its Transformation using Tkinter and
# OpenCV-Python:
# (i).Program to read and display an RGB color image and
# convert it into grayscale, negative and edge images.


import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk

def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def negative(image):
    return cv2.bitwise_not(image)

def edges(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    return edges

def display_images(image):
    gray = grayscale(image)
    negative_img = negative(image)
    edge_img = edges(image)

    images = [image, gray, negative_img, edge_img]
    titles = ["Original", "Grayscale", "Negative", "Edges"]

    for i in range(len(images)):
        cv2.imshow(titles[i], images[i])

    cv2.waitKey(0)
    cv2.destroyAllWindows()

root = tk.Tk()
root.title("Image and its Transformations")

# Read the image
image_path = "example.jpg"
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert the image to Tkinter format
image_pil = Image.fromarray(image)
image_tk = ImageTk.PhotoImage(image_pil)

# Display the image
label = tk.Label(root, image=image_tk)
label.pack()

# Display the transformations
display_images(image)

root.mainloop()
