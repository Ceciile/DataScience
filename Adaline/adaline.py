#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on 10th Janv 2018

@author: Qianqian
"""

import random as random
import numpy as np
import re
#adaline

#tabparam = 
def adaline(T,eta,S):
    print("adaline")
    Sline = [line for line in open(S)]
    #SS = 
    w0 = 0
    n = 4
    ind = 0
    nbligne = 97# need to find this valuee by itself
    tabvar =[]
    x = [] #vecteur xi de variables
    x = np.zeros((97,4))
    
    #y = [] #yi
    y = np.zeros(97)
    w = np.zeros(n)#extraire le nb de variabble d'une ligne de S
    for l in Sline:
#        print("l = "+l)
#        print("L.split",l.split())
        tabvar.append(l.split())
        
        """
        print("tabvar")
        print(tabvar)
        print("tabvar[0][1:]")
        print(tabvar[0][1:])"""
        #x.append(tabvar[ind][1:])
        x[ind]=tabvar[ind][1:]
        #y.append(float (tabvar[ind][0]))
        y[ind] = float (tabvar[ind][0])
#        print("x0")
#        print(x[ind])
        ind = ind + 1
#        print("T")
#        print(T)
    for t in range(T+1):
        for i in range(1,nbligne):
            """
            print(float(y[i]))
            print(w0)
            print(w)
        
            #x[i]=[float(j) for j in x[i]]
            print("x[i]")
            print(x[i])
            print(np.dot(w,x[i]))
            print(y[i])
            """
#des que quand separer les exemples solution hyperplane, on calcule disdances y*{w0(x) +<w(*),x>}/||w(*)||    =sur!!!positive
            if y[i]*(w0 + np.dot(w,x[i])) <= 0:  #yi*(w0+<w,xi>)<=0
                w0 = w0 + eta * y[i]
                #print(w0)
                """
                print("seconde affectation ")
                print(w)
                print(eta)
                print (int(y[i]*4))
                print(x[i])
                """
                yy =[y[i]]*4#yy 4 = nb de var
                #print(yy)
                #print(x[i]*yy)
                etaeta = np.array([eta] * 4)#vector eta 4 = nb de var
                """
                print("3")
                print(etaeta)
                print(yy)
                print(np.array(etaeta) * np.array(yy))
                print(x[i])
                print(etaeta*yy*x[i])
                print(w + etaeta*yy*x[i] )
                print("res")
                print(w)
                """
                w  = w  + (etaeta*yy) * x[i]
                print(w)
    print("w0")
    print(w0)
    print("w")
#    print(w)
    return(w0,w);
            
# cleaning data
dataFile = open("agaricus-lepiota.data", "r")
cleanData =open("data.txt","w")
#data= dataFile.read()

"""
s = 'abcd'
new_s = ''
for c in s:
    new_s += str(ord(c) - 96)
print(new_s)
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



cleanData.close()
dataFile.close()

"""

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
T = 1000 # 5* taille de ??
eta = 0.1#hyperparametre
(resW0,resW) = adaline(T,eta,"S.txt")
print("resW0")
print(resW0)
print("resW")
print(resW)
#test sur la base de test

Sfile.close()
"""
