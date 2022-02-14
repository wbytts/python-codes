# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
from numpy import fft
import cv2
from temp_004 import psf2otf


def motion_blur(gray, degree=7, angle=60):
    gray = np.array(gray)
    M = cv2.getRotationMatrix2D((round(degree / 2), round(degree / 2)), angle, 1)
    motion_blur_kernel = np.diag(np.ones(degree))
    motion_blur_kernel = cv2.warpAffine(motion_blur_kernel, M, (degree, degree))
    PSF = motion_blur_kernel / degree

    blurred = cv2.filter2D(gray, -1, PSF)
    blurred = cv2.normalize(blurred,None, 0, 255, cv2.NORM_MINMAX)
    blurred = np.array(blurred, dtype=np.uint8)
    return blurred,PSF


def inverse(blurred, PF):
    IF_fft = fft.fft2(blurred)
    result = fft.ifft2(IF_fft / PF)
    result = np.real(result)
    return result

def wiener(blurred, PF, SNR=0.01):       # 维纳滤波，K=0.01
    IF_fft = fft.fft2(blurred)
    G_f = np.conj(PF) / (np.abs(PF) ** 2 + SNR)
    result = fft.ifft2(IF_fft * G_f)
    result = np.real(result)
    return result

def CLSF(blurred,PF,gamma = 0.05):
    outheight, outwidth = blurred.shape[:2]
    kernel = np.array([[0, -1, 0],
                       [-1, 4, -1],
                       [0, -1, 0]])

    PF_kernel = psf2otf(kernel,[outheight, outwidth])
    IF_noisy = fft.fft2(blurred)

    numerator = np.conj(PF)
    denominator = PF**2 + gamma*(PF_kernel**2)
    CLSF_deblurred = fft.ifft2(numerator* IF_noisy/ denominator)
    CLSF_deblurred = np.real(CLSF_deblurred)
    return CLSF_deblurred

def normal(array):
    array = np.where(array < 0,  0, array)
    array = np.where(array > 255, 255, array)
    array = array.astype(np.int16)
    return array


def main(gray):
    channel = []
    img_H, img_W = gray.shape[:2]
    blurred,PSF = motion_blur(gray, degree=15, angle=30)      # 进行运动模糊处理
    PF = psf2otf(PSF, [img_H, img_W])

    inverse_blurred =normal(inverse(blurred, PF))             # 逆滤波
    wiener_blurred = normal(wiener(blurred, PF))              # 维纳滤波
    CLSF_blurred = normal(CLSF(blurred, PF))                  # 约束最小二乘方滤波

    blurred_noisy = blurred + 0.1 * blurred.std() * \
                    np.random.standard_normal(blurred.shape)  # 添加噪声

    inverse_noise = normal(inverse(blurred_noisy, PF))        # 添加噪声-逆滤波
    wiener_noise = normal(wiener(blurred_noisy, PF))          # 添加噪声-维纳滤波
    CLSF_noise = normal(CLSF(blurred_noisy, PF))              # 添加噪声-约束最小二乘方滤波
    print('CLSF_deblurred',CLSF_blurred)
    channel.append((blurred,inverse_blurred,wiener_blurred,CLSF_blurred,
                    normal(blurred_noisy),inverse_noise,wiener_noise,CLSF_noise))
    return channel


if __name__ == '__main__':
    image = cv2.imread('f:/images/liu_tou.png')
    b_gray, g_gray, r_gray = cv2.split(image.copy())

    Result = []
    for gray in [b_gray, g_gray, r_gray]:
        channel = main(gray)
        Result.append(channel)

    blurred = cv2.merge([Result[0][0][0], Result[1][0][0], Result[2][0][0]])
    inverse_blurred = cv2.merge([Result[0][0][1], Result[1][0][1], Result[2][0][1]])
    wiener_blurred = cv2.merge([Result[0][0][2], Result[1][0][2], Result[2][0][2]])
    CLSF_blurred = cv2.merge([Result[0][0][3], Result[1][0][3], Result[2][0][3]])
    blurred_noisy = cv2.merge([Result[0][0][4], Result[1][0][4], Result[2][0][4]])
    inverse_noise = cv2.merge([Result[0][0][5], Result[1][0][5], Result[2][0][5]])
    wiener_noise = cv2.merge([Result[0][0][6], Result[1][0][6], Result[2][0][6]])
    CLSF_noise = cv2.merge([Result[0][0][7], Result[1][0][7], Result[2][0][7]])


    #========= 可视化 ==========
    plt.figure(figsize=(9, 11))
    plt.gray()
    imgNames = {"Original Image":image,
                "Motion blurred":blurred,
                "inverse_blurred":inverse_blurred,
                "wiener_blurred": wiener_blurred,
                "CLSF_blurred": CLSF_blurred,
                'blurred_noisy': blurred_noisy,
                "inverse_noise":inverse_noise,
                "wiener_noise":wiener_noise,
                "CLSF_noise":CLSF_noise
                }
    for i,(key,imgName) in enumerate(imgNames.items()):
        plt.subplot(331+i)
        plt.xlabel(key)
        plt.imshow(np.flip(imgName, axis=2))
    plt.show()

