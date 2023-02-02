import cv2
import numpy as np
import os


def main(img):
    FOLDER = "origin-pic/"
    COPY_FOLDER = "filtered-pic/"

    print(img)

    src=cv2.imread(FOLDER+img,1)

    #ルックアップテーブル生成
    min_table = 50
    max_table = 205
    diff_table = max_table - min_table

    LUT_HC = np.arange(256, dtype ='uint8')
    LUT_LC = np.arange(256, dtype ='uint8')

    # ハイコントラストLUT作成
    for i in range(0, min_table):
        LUT_HC[i] = 0
    for i in range(min_table, max_table):
        LUT_HC[i] = 255 * (i - min_table) / diff_table
    for i in range(max_table, 255):
        LUT_HC[i] = 255

    # ローコントラストLUT作成
    for i in range(256):
        LUT_LC[i] = min_table + i * (diff_table) / 255

    high_cont_img = cv2.LUT(src, LUT_HC)
    low_cont_img = cv2.LUT(src, LUT_LC)

    cv2.imwrite(COPY_FOLDER+"high"+img, high_cont_img)
    cv2.imwrite(COPY_FOLDER+"low"+img, low_cont_img)

    LUT_G1 = np.arange(256, dtype = 'uint8' )
    LUT_G2 = np.arange(256, dtype = 'uint8' )
    
    # ガンマ変換ルックアップテーブル
    gamma1 = 0.75
    gamma2 = 1.5
    for i in range(256):
        LUT_G1[i] = 255 * pow(float(i) / 255, 1.0 / gamma1)
        LUT_G2[i] = 255 * pow(float(i) / 255, 1.0 / gamma2)

    high_gamma_img = cv2.LUT(src, LUT_G1)
    low_gamma_img = cv2.LUT(src, LUT_G2)
    high_gamma2_img = cv2.LUT(high_cont_img, LUT_G1)
    low_gamma2_img = cv2.LUT(low_cont_img, LUT_G2)

    cv2.imwrite(COPY_FOLDER+"G1"+img, high_gamma_img)
    cv2.imwrite(COPY_FOLDER+"G2"+img,low_gamma_img)
    cv2.imwrite(COPY_FOLDER+"G3"+img, high_gamma2_img)
    cv2.imwrite(COPY_FOLDER+"G4"+img,low_gamma2_img)

    #ブラー
    average_square = (10,10)
    blur_img = cv2.blur(src, average_square)
    cv2.imwrite(COPY_FOLDER+"hei"+img, blur_img)

    #ガウス
    row,col,ch= src.shape
    mean = 0
    sigma = 15
    gauss = np.random.normal(mean,sigma,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    gauss_img = src + gauss
    cv2.imwrite(COPY_FOLDER+"gauss"+img, gauss_img)

    #ソルトアンドペッパー
    row,col,ch = src.shape
    s_vs_p = 0.5
    amount = 0.004
    salt_img = src.copy()
    papper_img=src.copy()

    # 塩モード
    num_salt = np.ceil(amount * src.size * s_vs_p)
    coords = [np.random.randint(0, i-1 , int(num_salt)) for i in src.shape]
    salt_img[coords[:-1]] = (255,255,255)
    cv2.imwrite(COPY_FOLDER+"salt"+img, salt_img)


    # 胡椒モード
    num_pepper = np.ceil(amount* src.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i-1 , int(num_pepper)) for i in src.shape]
    papper_img[coords[:-1]] = (0,0,0)
    cv2.imwrite(COPY_FOLDER+"papper"+img,papper_img)

#パスの取得&リスト作成
ab_path = r'C:/Users/yasut/Desktop/python/cycle-learn/origin-pic'
files = os.listdir(ab_path)

for dir in files:
    filter.main(dir)