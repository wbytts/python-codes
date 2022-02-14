from collections import OrderedDict
import numpy as np
import cv2
 
# 定义一个映射面部索引的字典
# 特定人脸区域的地标
FACIAL_LANDMARKS_IDXS = OrderedDict([
	("mouth", (48, 68)),
	("right_eyebrow", (17, 22)),
	("left_eyebrow", (22, 27)),
	("right_eye", (36, 42)),
	("left_eye", (42, 48)),
	("nose", (27, 36)),
	("jaw", (0, 17))
])
 
def rect_to_bb(rect):
# 由DLIB预测一个边界并转换它
# 对于通常我们所做的格式（x，y，w，h）
# OPEN与OpenCV
	x = rect.left()
	y = rect.top()
	w = rect.right() - x
	h = rect.bottom() - y
 
	# 返回 tuple  (x, y, w, h)
	return (x, y, w, h)
 
def shape_to_np(shape, dtype="int"):
	# 初始化（x，y）坐标的列表
	coords = np.zeros((shape.num_parts, 2), dtype=dtype)
 
# 对所有面部标志进行循环并转换
# 关于x（y，y）坐标的2元组
	for i in range(0, shape.num_parts):
		coords[i] = (shape.part(i).x, shape.part(i).y)
 
	# 返回（x，y）坐标的列表
	return coords
 
def visualize_facial_landmarks(image, shape, colors=None, alpha=0.75):
# 创建输入图像的两个副本 (一个用于输入图像)
# 叠加和 (一个用于最终输出图像)
	overlay = image.copy()
	output = image.copy()
 
# 如果颜色列表为“否”，则用唯一的方法初始化它。
# 每个脸部标志区域的颜色
	if colors is None:
		colors = [(19, 199, 109), (79, 76, 240), (230, 159, 23),
			(168, 100, 168), (158, 163, 32),
			(163, 38, 32), (180, 42, 220)]
 
	# 在面部标志区域上分别的连线
	for (i, name) in enumerate(FACIAL_LANDMARKS_IDXS.keys()):
		# grab the (x, y)-coordinates associated with the
		# face landmark
		(j, k) = FACIAL_LANDMARKS_IDXS[name]
		pts = shape[j:k]
 
		# 检查是否应该画下颌线
		if name == "jaw":
			# 因为 jawline 是一个非封闭的面部区域，
# 只画出（x，y）坐标之间的直线
			for l in range(1, len(pts)):
				ptA = tuple(pts[l - 1])
				ptB = tuple(pts[l])
				cv2.line(overlay, ptA, ptB, colors[i], 2)
 
		# 处理计算点的凸包
		# 并在覆盖图上绘制船体
		else:
			hull = cv2.convexHull(pts)
			cv2.drawContours(overlay, [hull], -1, colors[i], -1)
 
	# 应用透明覆盖
	cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)
 
	# 返回输出图像
	return output