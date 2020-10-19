#opwncvのラップラシアンフィルタのパラメータを決定するための試行用プログラム

#ボケた画像のlaplacian.var()を計測して、それをボケ画像判定のスレッショルドにする

import cv2
import numpy as numpy
import os

image_name = r'C:\Users\shin\Desktop\cut_image\tomato_1_71.jpg'     #読み込む画像


#イメージの読み込み
primal_image = cv2.imread(image_name)
gray_image = cv2.cvtColor(primal_image, cv2.COLOR_BGR2GRAY)

#エッジを検出する
def variance_of_laplacian(image):
    return cv2.Laplacian(image, cv2.CV_64F)
 
laplacian_image = variance_of_laplacian(gray_image)

#検出した画像のエッジのスコアを画面の左上に表示する
#put text https://axa.biopapyrus.jp/ia/opencv/puttext.html
def report_image(image, laplacian, text):
   cv2.putText(laplacian_image, "{}: {:.2f}".format(text, laplacian.var()), (10, 30),
               cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 3)
#cv2.putText(image, "{}: {:.2f}".format(text, laplacian.var()), (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 3)

text = "laplacian.var()　is"

laplacian_report = report_image(laplacian_image, laplacian_image, text)



#画面の表示
cv2.imshow("primal_image", primal_image)
cv2.imshow("gray_image", gray_image)
cv2.imshow("laplacian_image", laplacian_image)
#cv2.imshow("laplacian_report", laplacian_report)

cv2.waitKey(0)
