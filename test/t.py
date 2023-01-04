import matplotlib.pyplot as plt
from matplotlib.pyplot import Rectangle
import numpy as np
import cv2

from core.util.matrix.operation import show as m_show

fig = plt.figure(figsize=(5.12, 5.12))
plt.Rectangle((0, 0), 100, 100)
# 绘制横向十字架
plt.plot([-10, 10], [0, 0], 'k-', linewidth=20)
# 绘制纵向十字架
plt.plot([0, 0], [-0.5, 0.5], 'k-', linewidth=20)

plt.savefig("C:\\Users\\10956\\Desktop\\test.png")

# Load the image
img = cv2.imread("C:\\Users\\10956\\Desktop\\test.png", 0)

# Resize the image to 64x64
img = cv2.resize(img, (64, 64))

# Threshold the image to convert it to 0 or 1
img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)[1]
matrix = np.array(img)
matrix[matrix == 0] = 1
matrix[matrix == 255] = 0
print(matrix)
m_show.save_show_pic_rat90(matrix)
