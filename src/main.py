from game import Game
from PIL import Image
import numpy
import os

def save_npy_as_png():
    dirname = "/home/fuge/Downloads/JAXAtari_BasicMath/scripts/BasicMath_screenshots"
    dirs = os.listdir(dirname)
    for cur_dir in dirs:
        if not cur_dir.endswith(".npy"):
            continue
        arr = numpy.load(os.path.join(dirname, cur_dir))
        img = Image.fromarray(arr)
        img.save(os.path.join(dirname, cur_dir.replace(".npy", ".png")))

if __name__ == "__main__":
    Game().play()