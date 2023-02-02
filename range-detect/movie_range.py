import cv2
import numpy as np
import matplotlib.pyplot as plt
 
#動画を読込み
#カメラの場合は引数に1か0のデバイスIDを記述
video = cv2.VideoCapture('range.mp4')
 
cascade = cv2.CascadeClassifier('cascade.xml')
 
while video.isOpened():
    # フレームを読込み
    ret, frame = video.read()
    #height, width= frame.shape[:2]
 
    # 読み込めなかった場合は停止
    if not ret: break

    #リサイズ
    frame = cv2.resize(frame, dsize=None, fx=0.5, fy=0.5)

    # 検出
    point = cascade.detectMultiScale(frame, scaleFactor=1.02, minNeighbors=1) 
 
    # 検出できた場合
    if len(point) > 0:
        for (x,y,w,h) in point:
            cv2.rectangle(frame, (x,y),(x+w,y+h), (0, 0, 255), thickness=2)
 

        #距離計算
        w1=443*0.5#基準
        width1=1920#基準
        
        L=2*(w1/w)
        #L=2*((w1/width1)/(w/width))
        L=round(L, 3)

        #テキスト表示
        '''cv2.putText(frame,
                ("W: "+str(w)+"[px]"),
                org=(10, 80),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=2,
                color=(0, 0, 255),
                thickness=3,
                lineType=cv2.LINE_4)

        cv2.putText(frame,
                ("L: "+str(L)+"[m]"),
                org=(10, 160),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=0.5,
                color=(0, 0, 255),
                thickness=3,
                lineType=cv2.LINE_4)'''
        #描画
        
        cv2.imshow('frame', frame)
        print(L)
    
        # enterキーの押下で処理を中止
        key = cv2.waitKey(1) & 0xFF
        if key == 13: break
 
#メモリの解放
video.release()
cv2.destroyAllWindows()