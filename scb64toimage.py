# -*- coding: utf-8 -*-
# base64 encode された bmp, png を自動判別し、
# base64 decode (拡張子を自動的につける)
import sys
import os
import base64
import imghdr    # 画像ファイル種別の識別用

TEMPFILE = 'C:\\Windows\\temp\\__tempimage'


# コマンドライン引数のチェック
if len(sys.argv[1:]) == 0:
    print "Error: base64encode_data_file is not defined."
    sys.exit(0)

# コマンドライン引数から入力ファイル名を取得
base64_filename = sys.argv[1]


# base64 encodeデータ 読み込み
with open(base64_filename, 'rb') as fb64:
    b64encode_data = fb64.read()    # base64 encodeデータ

# base64 encode ---> base64 decode
b64decode_data = base64.b64decode(b64encode_data)


# 一時的にファイル出力
with open(TEMPFILE, 'wb') as fout:
    fout.write(b64decode_data)

# BASE64エンコードファイル名の拡張子を外す
fname, ext = os.path.splitext(base64_filename)

# 画像ファイル種別の判別
ext2 = imghdr.what(TEMPFILE)


# 入力ファイルの拡張子を「.{ext2}」に変更して、出力ファイル名にする
decoded_filename = '{0}.{1}'.format(fname, ext2)

# base64 decode ---> ファイル書き込み
with open(decoded_filename, 'wb') as fout:
    fout.write(b64decode_data)
