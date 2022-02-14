import cv2
import numpy as np

img = cv2.imread('images/法制社-新旧对照全文加水印_1.png')
new = np.clip(2.0*img-160, 0, 255).astype(np.uint8)
cv2.imwrite('images/法制社-新旧对照全文加水印_1_cleaned.png', new)