# -*- coding: utf-8 -*-
import sys
import os
import base64

# コマンドライン引数のチェック
if len(sys.argv[1:]) == 0:
    print "Error: base64encode_data_file is not defined."
    sys.exit(0)

# コマンドライン引数から入力ファイル名を取得
base64_filename = sys.argv[1]

# 入力ファイルの拡張子を「.bmp」に変更して、出力ファイル名にする
fname, ext = os.path.splitext(base64_filename)
bmp_filename = fname + ".bmp"

# base64 encodeデータ 読み込み
with open(base64_filename, 'rb') as fb64:
    b64encode_data = fb64.read()    # base64 encodeデータ

# base64 encode ---> base64 decode
b64decode_data = base64.b64decode(b64encode_data)

# base64 decode ---> ファイル書き込み (bmp)
with open(bmp_filename, 'wb') as fout:
    fout.write(b64decode_data)

