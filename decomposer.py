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
 usage - prints out information for how program should be used on the command
    line.  Call this method if the user gives improper arguments
"""
def usage():
    print >> sys.stderr, "Usage: python hangul.py compose/decompose inputfile outputfile"
    print >> sys.stderr, "  compose/decompose - option "
    print >> sys.stderr, "  inputfile - file to be processed "
    print >> sys.stderr, "  outputfile - name of result "

"""
composeFile:
Input: input and output filename
Output: 
"""
def composeFile(inputfile, outputfile):
    
    result = codecs.open(outputfile, "w","utf-8")
    with codecs.open(inputfile,"r","utf-8") as f:
        for line in f:
            info = line.split("/")
	    #print info
	    for word in info:
		if len(word)!=3:
		    result.write(word)
                else:
	    	    #print word
                    #print len(word)
                    result.write(compose(word[0],word[1],word[2]))#.encode('utf-8'))
    result.close()

"""
decomposeFile:
Input: input and output filename
Output: 
"""
def decomposeFile(inputfile, outputfile):
    
    result = codecs.open(outputfile, "w","utf-8")
    with codecs.open(inputfile,"r","utf-8") as f:
        for line in f:
            info = line.split()
            print "info: ",info

            for word in info:
                count = 1
                leng = len(word)
                print "word: ", word
                for char in word:
                    count += 1
                    decomposition = decompose(char)
                    print "decomposition: ", decomposition
                    #result.write("/") #find a suitable marker -- may not be needed at all!
                    for dec in decomposition:
                        
                        #if dec == " ":
                        #print count, leng
                        if dec == " ":
                            pass
                        else:
                            result.write(dec)
                    #result.write("/")
                result.write(" ") #write a space after a word
          

def getOI(cho):
    
    for i in range(0,len(onset)):
        if (onset[i]) == cho:#cho.decode('utf-8'):
            return i

def getNI(cho):
    for i in range(0,len(nucleus)):
        if (nucleus[i]) == cho:#cho.decode('utf-8'):
            return i

def getCI(cho):
    for i in range(0,len(coda)):
        if (coda[i]) == cho:#.decode('utf-8'):
            return i

"""
compose: Given onset, nucleus, coda sounds compose them
input: cho(onset), jung(nucleus), jong(coda) chars
output: composed char
"""
def compose(cho, jung, jong):

    onsetPOS = getOI(cho)
    nucleusPOS = getNI(jung)
    codaPOS = getCI(jong)
 
    #print cho, onsetPOS
    #print jung, nucleusPOS
    #print jong, codaPOS

    nUnicode = unibase + (onsetPOS * 21 + nucleusPOS) * 28 + codaPOS
   
    
    char = unichr(nUnicode)
    return char
    

def decompose(char):
    #cho: 0xea
    #jung: 0xb0
    #jong: 0x80
    temp = 0x0000
    charcode =  (ord(char))

    decomp = []
    #not hangul char
    if charcode < unibase or charcode > unilast:
        return [char]
    
    charidx = charcode - unibase
    
    cho =  charidx/(21*28)
    charidx = charidx % (21*28)

    jung = charidx/28
    charidx = charidx %28

    jong = charidx
    """   
    print onset[cho]
    print nucleus[jung]
    print coda[jong]
    """
    return [onset[cho],nucleus[jung],coda[jong]]
    """
    for i in range(0,len(char)):
        temp = "0x"+repr(char[i])[3:5]
        temp = int(temp,16)
        decomp.append(hex(temp))
    
    diff1 = int(decomp[0],16)-int(0xea)
    diff2 = int(decomp[1],16)-int(0xb0)
    diff3 = int(decomp[2],16)-int(0x80)

    return [onset[diff1], nucleus[diff2], coda[diff3]]
    """

"""
main
"""
def main():
    if len(sys.argv) != 3:
        usage()
        exit()
    else:
        #option = sys.argv[1]
        inputfile = sys.argv[1]
        outputfile = sys.argv[2]
        
        if(not exists(inputfile)):
            print "inputfile does not exist!"
            exit()

    global onset
    onset= u"ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"
    #onset = [u"\u3131",u"\u3132", u"\u3134", u"\u3137",u"\u3138", u"\u3139",u"\u3141",u"\u3142", u"\u3143", u"\u3145" \
#u"\u3146 ", u"\u3147", u"\u3148",u"\u3149", u"\u314A", u"\u314B", u"\u314C", u"\u314D", u"\u314E"]
    global nucleus
    #nucleus= [u"\u314F",u"\u3150", u"\u3151", u"\u3152", u"\u3153", u"\u3154", u"\u3155", u"\u3156", u"\u3157", u"\u3158" \
	#u"\u3159", u"\u315A", u"\u315B", u"\u315C", u"\u315D", u"\u315E", u"\u315F", u"\u3160", u"\u3161", u"\u3162", u"\u3163"]
    nucleus = u"ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ"
    global coda 
    #coda = ["",u"\u3131", u"\u3132", u"\u3133", u"\u3134", u"\u3135", u"\u3136", u"\u3137", u"\u3139", u"\u313A", u"\u313B", \
#u"\u313C", u"\u313D", u"\u313E", u"\u313F", u"\u3140", u"\u3141", u"\u3142", u"\u3144", u"\u3145", u"\u3146", u"\u3147", u"\u3148",\
	#u"\u314A", u"\u314B", u"\u314C", u"\u314D",u"\u314E"]
    coda= u" ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ"
    global unibase 
    unibase= 0xAC00
    global unilast 
    unilast= 0xD79F

    decomposeFile(inputfile, outputfile)
               
    return

if __name__ == "__main__":
    main()
