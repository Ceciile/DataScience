#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
Created on 10th Janv 2018

@author: Qianqian
"""
#faut normaliser donnees!!

import random as random
import numpy as np
import re
#adaline

#tabparam = 
def initweight(size) :
    w = [0.] * size
    for i in range(1,size) :
        w[i] = random.randint(0,100)/100.
    return w



def hw(w,x) :
    #print (len(w[1:]) ,type(x))
    return w[0] + np.dot(w[1:], x)
def L(w,S) :
    size_of_space = len(S[0].split())-1
    m = len(S)
    somme = 0
    for i in range(1,m) :
	intS=map(float,(S[i].split())[:-1])
        xi = intS#S[i][0:size_of_space]
        yi = float(S[i].split()[size_of_space])
        somme = somme + pow(hw(w,xi) - yi ,2)
    return somme/m

def adaline(S, T, eta, E) :
    size_of_space = len(S[0].split()) -1
    w = initweight(size_of_space+1)#len(S[0])
    print ("initweight : ",w)
    t = 0
    condition = True
    while condition :
        # Choisir un exemple Alea
        i = random.randint(0,len(S)-1)
	intS=map(float,(S[i].split())[:-1])
	#print type(S[i].split())
        yi = float(S[i].split()[size_of_space])
        xi = intS
        #MAJ
        w2 = [0] * (size_of_space + 1)#w2 = np.zeros(size_of_space + 1)
        w2[0] = w[0] - 2*eta*(hw(w, xi)-yi)
        w2[1:] = np.subtract(w[1:],[2*eta*x*(hw(w, xi)-yi) for x in xi])
        t = t+1
        condition = t < T and abs(L(w2, S) - L(w, S)) > E
        w = w2
    return w
            
# cleaning data
#dataFile = open("agaricus-lepiota.data", "r")
#cleanData =open("data.txt","w")
#data= dataFile.read()

"""
s = 'abcd'
new_s = ''
for c in s:
    new_s += str(ord(c) - 96)
print(new_s)
"""
def Mushroom() :
    fname = "agaricus-lepiota.data"
    f = open(fname, "r")
    cleanData =open("data.txt","w")
    lines = []
    for line in f :
        line = line.strip("\n")
        line_tab = line.split(",")
        res = line_tab[1:] + ["e"]
        res = map(lambda x : (ord(x) - 96)/26., res)
        if line_tab[0] == "e" :
            res[len(res)-1] = "+1 "
        else :
            res[len(res)-1] = "-1 "
        lines.append(res)
    for line in lines :
        cleanData.write(' '.join(map(str,line)))
        cleanData.write('\n')
    cleanData.close()
    #mon_set = np.array(lines, dtype=float)
"""
new_s=''
for line in dataFile:
    #print(line)
    #print(line.split(","))
    
    if(line.split(",")[0] == "p"):
        #cleanData.write(newLine)
        for c in line.split(",")[1:]:
	    new_s = new_s +' '+ str(ord(re.sub('[^a-z]+', '', c))-96)
        newLine = "+1"+new_s+"\n"
        cleanData.write(newLine)
    else:
         for c in line.split(",")[1:]:
	     new_s = new_s +' '+ str(ord(re.sub('[^a-z]+', '', c))-96)
         newLine = "-1"+new_s+"\n"
         cleanData.write(newLine)


"""


#cleanData.close()
#dataFile.close()
Mushroom()


#separation aleatoire
testfile = open("test.txt","w")
Sfile    = open("S.txt","w")
#cleanData =open("data.txt","r")
random.seed(2);
testdata = [line for line in open("data.txt") if random.random() >= 0.7]
cleanDataLine = [line for line in open("data.txt")]
n = 0
m = 0
p = 0
for l in cleanDataLine:
    p = p + 1
    if l in testdata:
         n = n +1
         testfile.write(l);
    if not(l in testdata):
        Sfile.write(l)
        m = m + 1
print(p)
print("testfile:",n)
print(m)        
print(n+m)
testfile.close()
Sfile.close()

#apprentissage sur S
T = 10*len(testdata)/3
eta = 0.1#hyperparametre
print "ADALINE"
laernData = [line for line in open("S.txt")]
tData = [line for line in open("test.txt")]
print ("T = 10*len(testdata)/3 ",T)
wT = adaline(laernData, T, 0.1, 100)
print wT
#print perf

#faut normaliser donnees
