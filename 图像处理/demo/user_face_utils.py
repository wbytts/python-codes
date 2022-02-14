from imutils import face_utils
import imutils
import dlib
 
 
#初始化dlib人脸检测（基于HOG），然后创建面部标志预测器
detector = dlib.get_frontal_face_detector()
 
predictor = dlib.shape_predictor('点模型数据地址')
 
image = cv2.imread('图片地址')#输入图片实参则读入图片
 
 
image = imutils.resize(image, width=500)  # 调整图片宽度为500
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)#图片调整为灰色
 
#  检测灰度图像中的面部
rects = detector(gray, 1)
for (i, rect) in enumerate(rects):
    shape = predictor(gray, rect)
    shape = shape_to_np(shape)
    ii=visualize_facial_landmarks(image,shape)
    cv2.imshow('ok',ii)
    cv2.waitKey(0)