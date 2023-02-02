import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def test(pic):
    
# 学習器(cascade.xml)の指定
    Cascade = cv2.CascadeClassifier('cascade.xml')
    # 予測対象の画像の指定
    img = cv2.imread('test-picture/'+pic, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    point = Cascade.detectMultiScale(gray, scaleFactor=1.01, minNeighbors=1,minSize=(1,1))

    if len(point) > 0:
        for rect in point:
            cv2.rectangle(img, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), (0, 0, 255), thickness=2)
            
    else:
        print ("no detect")

    cv2.imwrite('2021/cut2/lbp/'+pic, img)


#パスの取得&リスト作成(フルパスで入力)
ab_path = r'E:\2022引継ぎ資料\カスケードファイル\test-picture'
files = os.listdir(ab_path)

for dir in files:
    test(dir)
