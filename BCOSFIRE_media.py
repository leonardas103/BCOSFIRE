import numpy as np

def load_image(path):
    import cv2
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    height, width = img.shape
    return (img, height, width)

def main(image, filter1, filter2, preprocessthresh):
    x,y = 101,101
    np.zeros((201,201), dtype=int)