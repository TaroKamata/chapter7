# -*- coding: utf-8 -*-
#
# カメラキャプチャ

import cv2
#import time
#import os.path
#import datetime

#SAVE_DIR = os.path.expanduser('~') + '\\AppData\\Local\\Temp'
SAVE_DIR = 'C:\\WINDOWS\\Temp'
SAVE_FNAME = 'capture.png'


# run() メソッドから開始させる
def run(**args):
    # 初期化
    capture = cv2.VideoCapture(0)
    if capture.isOpened() is True:
        print 'Success Open Camera!'

    ret, image = capture.read()
    if ret == True:
        print 'Read OK!'


    # 撮影 (１回目はセピアカラーになってしまうので、保存しない)
    capture.read()
    ret, image = capture.read()
    if ret == True:
        cv2.imwrite('{0}\\{1}'.format(SAVE_DIR, SAVE_FNAME), image)


    # 後始末
    capture.release()
    cv2.destroyAllWindows()


    # 保存した画像ファイルを読んで、returnで戻す
    with open('{0}\\{1}'.format(SAVE_DIR, SAVE_FNAME), 'rb') as f:
        data = f.read()    # 文字列で読み込まれる
    print len(data)  # デバッグ用にサイズだけ表示

    return data




# コマンドラインから実行する場合には、以下が必要
#retval = run()
#print retval
