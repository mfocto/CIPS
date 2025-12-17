import cv2
import numpy as np


class PreprocessContext:
    def __init__(self, proc_w, proc_h):
        self.proc_w = proc_w
        self.proc_h = proc_h

class CommonPreprocessor:
    def run(self, img, cfg):
        h, w = img.shape[:2]
        return img, PreprocessContext(proc_w=w, proc_h=h)


