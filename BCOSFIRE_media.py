import numpy as np

def load_image(path):
    import cv2
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    height, width = img.shape
    return (img, height, width)

def make_prototype(length):
    a = np.zeros((length,length//2), dtype=int)
    b = np.ones((length,1),  dtype=int)
    return np.concatenate((a,b,a), axis=1)

def main(image, filter1, filter2, preprocessthresh):
    x,y = 100,100
    numoriens = 12
    prototype = make_prototype(201)
    symmfilter = (prototype, [x,y], filter1)
    numoriens = 24 #why do we change it here?
    filter2.set_rotation_psilist(filter2, numoriens, 2)
    asymmfilter = (prototype, [x,y], filter1)
