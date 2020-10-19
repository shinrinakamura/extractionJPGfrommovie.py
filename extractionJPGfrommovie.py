#movie_cut_toJPG
#opencv document http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_gui/py_image_display/py_image_display.html
# -*- coding: *-
"""
@author: S.Nakamura     2020/10/18
動画を読み込んで画像（ｊｐｇ）に分割するプログラム
input_movie：読み込む動画ファイル名
cpf：何フレームごとに保存するか
image_dir：画像の出力先ディレクトリ（無ければ作成する）

・動画の読み込み
・何フレーム毎に読み込むか
・画像の出力先のディレクトリの指定
・ピンぼけ画像を外す
・サイズの変更
・名前を決めて出力する
""" 

#ボケた画像をはじくためのパラメータは実際に自分が見てボケていると認識した画像のパラメータを参考に決定する
#ボケていると認識した画像を実際に二次微分して見る必要がある
#laplaciaan.var()の値が800以下のものをボケ画像として判定


import cv2
import numpy as np
import os
#import shutil
#ディレクトリの指定　　https://office54.net/python/python-unicode-error
input_movie_dir =   r"C:\Users\機械学習\anotation用動画"       #読み込む動画をディレクトリから指定
input_movie_file = r"\eggplant_6.mp4"
image_dir   =   r"C:\Users\\anotation用動画\cut_image"           #出力先のフォルダ
#image_file  =   r"image_%s"          #出力するファイル名 最初にバックスラッシュをつける必要がある
#image = 
i=0
count = 0
cpf = 10 #cut per frame
#画像のサイズ
image_width = 640
image_heigh = 480
#ボケ画像判定のためのlaplacian.var
laplacian_thr = 800


#ファイルがあるか確認する

#動画から画像への変換
#動画の読み込み
cap = cv2.VideoCapture(input_movie_dir+input_movie_file)
#動画の読み込み完了


#outputimageのファイル名の作成
#input_movie_file.replace('.mpg4', '')


while(cap.isOpened()):
    ret, frame = cap.read()             #動画を読み込む
    #assert frame, "オープンに失敗"
    if not cap.isOpened():
        print ("can't open")
        break


    if ret == False:
        print('Finished')                    #動画が読み込めないとき
        break

    if count%cpf == 0:

        #サイズを小さくする
        resize_frame = cv2.resize(frame,(image_width,image_heigh))

         #画像がぶれていないか確認する
        laplacian = cv2.Laplacian(resize_frame, cv2.CV_64F)
        if ret and laplacian.var() >= laplacian_thr: # ピンぼけ判定がしきい値以上のもののみ出力
            
            #第１引数画像のファイル名、第２引数保存したい画像
            #ディレクトリの指定がうまくできていないので改善する必要がある
            write = cv2.imwrite('cut_image_2\\'+input_movie_file.replace('.mp4', '')+'_%s.jpg' %(i), resize_frame)  # Save a frame
            assert write, "保存に失敗"
            print('Save', 'cut_image_2\\'+input_movie_file.replace('.mp4', '')+'_%s.jpg' %(i))
            i += 1
            
        
        

        
    count = count + 1



cap.release()
