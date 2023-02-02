import cv2
import numpy as np
import matplotlib.pyplot as plt
    
# 学習器(cascade.xml)の指定
cascade = cv2.CascadeClassifier('cascade.xml')

# 予測対象の画像の指定
img = cv2.imread('2meter-model-50.jpg', cv2.IMREAD_COLOR)

#画像サイズ取得
height, width= img.shape[:2]

#グレースケール変換
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#検出
point = cascade.detectMultiScale(gray, scaleFactor=1.01, minNeighbors=1)

#検出出来た場合
if len(point) > 0:
    for (x,y,w,h) in point:
        cv2.rectangle(img, (x,y),(x+w,y+h), (0, 0, 255), thickness=2)
        
else:
    print ("no detect")


#基準
w1=443
width1=1920

#距離計算
L=2*((w1/width1)/(w/width))
L=round(L, 3)

#テキスト表示
cv2.putText(img,
            ("W: "+str(w)+"[px]"),
            org=(10, 80),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=2,
            color=(0, 0, 255),
            thickness=4,
            lineType=cv2.LINE_4)

cv2.putText(img,
            ("L: "+str(L)+"[m]"),
            org=(10, 160),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=2,
            color=(0, 0, 255),
            thickness=3,
            lineType=cv2.LINE_4)
            

#出力
cv2.imwrite('result.jpg', img)

print("width= "+str(width)+"[px]")
print("w= "+str(w)+"[px]")
print("L= "+str(L)+"[m]")