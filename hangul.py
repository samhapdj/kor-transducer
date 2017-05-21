# -*- coding: utf-8 -*-
#! /usr/bin/env python
"""
hangul.py
dmin1 - Do June Min
"""
import numpy
import sys
import codecs
from os.path import exists


"""
main
"""
def main():
    result = open("alph", "w")
    alph = "ㅏ ㅐ ㅑ ㅒ ㅓ ㅔ ㅕ ㅖ ㅗ ㅘ ㅙ ㅚ ㅛ ㅜ ㅝ ㅞ ㅟ ㅠ ㅡ ㅢ ㅣ"
    info = alph.split()
    for item in info:
        result.write(item+":"+item+" Loop ;\n")
    result.close()
          

   
if __name__ == "__main__":
    main()
