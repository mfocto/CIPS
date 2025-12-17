import cv2
import numpy as np

def decode_image_bytes(image_bytes: bytes, encoding: str):
    if not image_bytes:
        raise ValueError('empty image bytes')

    buffer = np.frombuffer(image_bytes, dtype=np.uint8)

    img = cv2.imdecode(buffer, cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError(f"failed to decode image (encoding={encoding})")

    return img