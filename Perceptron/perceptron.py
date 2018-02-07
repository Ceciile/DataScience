#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 10:21:21 2017

@author: qianqian
"""
#jeux de test uci iris ,breast cancer wiconsn , mushroom , spambase

#iris ne semble pas avoir besoin de normalisation

#spambase normalise ok
#wdbc normalise ok

#musroom voir code cecile (non normalisé)

#+faire un tableau recap voir cours !!!!

import random as random
import numpy as np
#perceptron + adaline? + plein de petite function pour triater lees données


#adaline a continuer

#T le nb d'epochs
#eta le pas d'apprentissage
#S ensemble d'apprentissage
def perceptron(T,eta,S):
    print("perceptron")
    Sline = [line for line in open(S)]#ligne de l'ensemble d'apprentissage
    w0 = 0 #initialisation du biais a zero
    nbvar = len(Sline[0].split())-1#nb de variables : les x[i] le -1 sert a ne pas compter la classe(y[i])
    
    #print("nbvar")
    #print(nbvar)
    #ok
    nbligne = len(Sline)#nb de ligne dans l'ensemble d'apprentissage
    #print("nbligne")
    #print(nbligne)
    #ok
    tabvar =[]#pour recuperer toutes les variables dans un tableau +la classe
    x = np.zeros((nbligne,nbvar))
    y = np.zeros(nbligne)#y[i]
    w = np.zeros(nbvar)
    ind = 0
    for l in Sline:#pour chaque ligne remplissage du tableau de var et les y[i]
        tabvar.append(l.split())
        x[ind]=tabvar[ind][1:]#on recupere les varible de la ligne d'indice 0
        y[ind] = float (tabvar[ind][0])#on recupere la classe
        ind = ind + 1#indice pour la ligne suivante
        
    for t in range(T+1):
        for i in range(1,nbligne):
            if y[i]*(w0 + np.dot(w,x[i])) <= 0:  #yi*(w0+<w,xi>)<=0  <=> si mal classe
                w0 = w0 + eta * y[i]
                
                yy =[y[i]]*nbvar#yy 4 = nb de var
                etaeta = np.array([eta] * nbvar)#vector eta 4 = nb de var
                
                w  = w  + (etaeta*yy) * x[i] #pb here ?
    print("w0")
    print(w0)
    print("w")
    print(w)
    return(w0,w);

###adaline algo not working
def adaline(T,eta,epsilon,S):
    print("adaline")
    Sline = [line for line in open(S)]
    #w0 = random.randint()#init aleatoire ?
    w0 = 0#should work too
    nbvar = len(Sline[0].split())-1
    ind = 0
    nbligne = len(Sline)
    tabvar =[]
    x = np.zeros((nbligne,nbvar))
    y = np.zeros(nbligne)
    w = np.zeros(nbvar)
    diff = epsilon + 1 # sur de passer dans le while au moins une fois
    for l in Sline:
        tabvar.append(l.split())
        x[ind]=tabvar[ind][1:]
        y[ind] = float (tabvar[ind][0])
        ind = ind + 1
    for t in range(T+1):
        while(diff > epsilon):
            i = random.randint(0,nbligne-1)#choix aleatoire d'un elem ?
            h = w0 + np.dot(w,x[i]) #calcul du h actuel h = w0 + np.dot(w,x)?
            #mise ajour des poids
            w0 = w0 - 2 * eta *(h -y[i])
            #yy =[y[i]]*nbvar#yy 4 = nb de var
            etaeta = np.array([eta] * nbvar)#vector eta 4 = nb de var
            wpred = w#save to calcul the diff
            w  = w  - 2 * etaeta * x[i] *( h - y[i])
            #another formule for update weight is used on his online course !?
            
        
            #diff = wpred - w
            #diff ) L() - L() ?
    print("w0")
    print(w0)
    print("w")
    print(w)
    return(w0,w);
#######################################
#il manque les autres algo
###############################################

#make a function ?
#
def cleanIrisData(outputFileName):
# cleaning data for iris base 
    dataFile = open("iris.data", "r")
    cleanData =open(outputFileName,"w")
    for line in dataFile:
        if(line.split(",")[-1] == "Iris-setosa\n"):
            newLine = "+1 "+line.replace(","," ")[0:16]+'\n'
            cleanData.write(newLine)
        elif line.split(",")[-1] == "Iris-versicolor\n" or line.split(",")[-1] == "Iris-virginica\n":
            newLine = "-1 "+line.replace(","," ")[0:16]+'\n'
            #print(newLine)
            cleanData.write(newLine)
    cleanData.close()
    dataFile.close()


# cleaning data for spam base + normalisation
def clean(line):
     line = str(line)
     line = line.replace("[","");
     line = line.replace("]","");
     line = line.replace("\\n","");
     line = line.replace("'","");
     #line = line.replace(",",",");
     line = line.replace(","," ");
     return line
 
    
#normalize too
def cleanSpamData(outputFileName):  
    
    dataFile = open("spambase.data", "r")
    cleanData =open(outputFileName,"w")

    #mini = np.zeros(len([line in dataFile]))
    #print("taille maxi")
    #print(len([lines for lines in dataFile]))
    taille_maxi = len([lines for lines in open("spambase.data")][0].split(","))-1
    #print(taille_maxi)
    maxi = np.zeros(taille_maxi)
    for line in dataFile:
        line_split=line.split(",")
        #remove the class in linesplit at the end for the moment
        line_split=line_split[:-1]
        for i in range(len(line_split)):#pour chaque colone
            #init  maxi 
            if maxi[i] < float(line_split[i]):
                maxi[i] = line_split[i]
         
        
    dataFile.close()   
    dataFile = open("spambase.data", "r")
    for line in dataFile:
        line_split=line.split(",")
        classe = int (line_split[-1])#recupere la class  la fin
        if classe == 0:
            classe = -1
            #print("classe")
            #print(classe)
        for i in range((len(line_split)) -1):
            line_split[i] = float(line_split[i]) / maxi[i]
        line = clean(line_split)
        cleanData.write( str(classe) +" "+ line[:-1] +"\n")#line[:-2] ??

    cleanData.close()
    dataFile.close()

#cleaning data for wdbc
def cleanWdbcData(outputFileName):
    dataFile = open("wdbc.data", "r")
    cleanData =open(outputFileName,"w")

    #mini = np.zeros(len([line in dataFile]))
    #print("taille maxi")
    #print(len([lines for lines in dataFile]))
    taille_maxi = len([lines for lines in open("wdbc.data")][0].split(","))-2
    #print(taille_maxi)
    maxi = np.zeros(taille_maxi)
    for line in dataFile:
        line_split=line.split(",")
        #remove the class in linesplit at the end for the moment
        line_split=line_split[1:]#on supprime l id du patient
        classe =  (line_split[0])#donc la premiere colonne est la classe 
        if classe == 'M':#Maligne 
            classe = +1
            line_split[0]= +1
        elif classe == 'B':#benige
            classe = -1
            line_split[0]= -1
        for i in range(len(line_split)-1):#pour chaque colone #pas de souci pour la classe ??
            if maxi[i] < float(line_split[i]):
                maxi[i] = line_split[i]
         
    dataFile.close()   
    dataFile = open("wdbc.data", "r")
    for line in dataFile:
        line_split=line.split(",")
        line_split=line_split[1:]#on enleve l'id des patient
        classe =(line_split[0])#donc la premiere colonne est la classe 
        if classe == 'M':#Maligne 
            classe = +1
        elif classe == 'B':#benige
            classe = -1
        
        for i in range(1,(len(line_split)) -1):
            line_split[i] = float(line_split[i]) / maxi[i]
        line = clean(line_split)
        line = line.replace("  "," ")#pb d'espace
        cleanData.write( str(classe)+ line[1:] +"\n")#line[:-2] ??
    cleanData.close()
    dataFile.close()


#separation aleatoire 
#SfileName  et testfileName dataFileName vec l'extension .txt
def splitRandom(SfileName,testfileName,dataFileName):
    print("separation aleatoire de test")
    Sfile = open(SfileName,"w")
    testfile = open(testfileName,"w")
    random.seed(2);#pour avoir toujours le meme tirage aleatoire a enlever si besoin
    testdata = [line for line in open(dataFileName) if random.random() >= 0.7]
    cleanDataLine = [line for line in open(dataFileName)]
    n = 0
    m = 0
    p = 0
    print("Length datafilename")
    print(len(testdata))
    for l in cleanDataLine:
        p = p + 1
        #print("p")
        #print(p)
        if l in testdata:
            n = n +1
            testfile.write(l);
        if not(l in testdata):
            Sfile.write(l)
            m = m + 1
    testfile.close()
    Sfile.close()


#creation base de test pour spambase voir dans l main
#splitRandom("spamS2.txt","spamtest2.txt","spambase.txt")
"""
random.seed(2);#pour avoir toujours le meme tirage alea
testfile = open("spamtest.txt","w")
testdata = [line for line in open("spambase.txt") if random.random() >= 0.7]
Sfile    = open("spamS.txt","w")
for l in open("spambase.txt"):
    if l in testdata:
        #l = l+"\n"
        testfile.write(l)
    else:
        Sfile.write(l)
testfile.close()
Sfile.close()
"""
# verifier si on obtient le meme res normalement ok


#apprentissage sur S
T = 1000 # 5* taille de ??
eta = 1#hyperparametre
#(resW0,resW) = perceptron(T,eta,"S.txt")
#print("resW0")
#print(resW0)
#print("resW")
#print(resW)

#test sur la base de test
def test(w0,w,testbase):
    perf = 0
    nbtest = len(testbase)
    testline = [line for line in open(testbase)]
    y = 0
    tabvar =[]
    for test in testline:
        tabvar =(test.split())
        y= float (tabvar[0])
        x=np.array([float(i) for i in tabvar[1:]])
        if y*(w0 + np.dot(w,x)) > 0:  #yi*(w0+<w,xi>)>0: bien classé perceptron
            perf = perf + 1 
    perf = perf/nbtest
    print("performance")
    print(perf)
    
#test perceptron spam 
#test("spamtest.txt")#pb here ?
"""
perf = 0;
nbTest = 53 # to find by itself
testline = [line for line in open("test.txt")]
#x=np.array([])
y = 0
ind = 0
tabvar =[]
w0,w = perceptron(T,eta,"S.txt")

for tst in testline:
    tabvar =(tst.split())
    y= float (tabvar[0])
    x=np.array([float(i) for i in tabvar[1:]])
    if y*(w0 + np.dot(w,x)) > 0:  #yi*(w0+<w,xi>)>0: bien classé
        perf = perf + 1 
perf = perf/nbTest
print("performance")
print(perf)
"""

"""
def clean(data):
#data = str(data)
    data = data.replace("[","");
    data = data.replace("]","");
    data = data.replace("\\n","");
    data = data.replace(",","");
    data = data.replace("'","");
    return data
"""


def writefich(line,fich):
     line = clean(line)
     for char in line:
            if char == ",":
                fich.write("\n")
            else:
                fich.write(char)
                
def crossvalid(nbcross,data): 
    random.shuffle(data,lambda:0.2)#melange aleatoire des donné
    datasize = len(data)
    #nbcross = 10
    toto = open('toto.txt',"w")
    #print(type(toto))
    cross = np.zeros(nbcross,dtype =type(toto))#10 nb de partie
    #print(type(cross))
    crosstest = np.zeros(nbcross,dtype =type(toto))#10 nb de partie      
    for i in range(nbcross):
        namefich="cross"+str(i)+".txt"
        nametest="crosstest"+str(i)+".txt"
        cross[i] = open(namefich,"w")
        crosstest[i] = open(nametest,"w")
        if (i == 0):
            #cross0.txt
            line = data[int((datasize/nbcross)):]
            writefich(line,cross[i])
            #crosstest0.txt
            line = data[0: int((datasize/nbcross))]
            writefich(line,crosstest[i])
        
        elif i != (nbcross -1):
            line = data[0: int((datasize/nbcross)*i)]
            writefich(line,cross[i])
            cross[i].write("\n")
            line = data[int((datasize/nbcross)*(i+1)):]
            writefich(line,cross[i])
        
            #crosstest[i]
            line =data[int((datasize/nbcross)*i) :int((datasize/nbcross)*(i+1)) ]
            writefich(line,crosstest[i])
       
        else:       
            line =data[0: int((datasize/nbcross)*i)]
            writefich(line,cross[i])      
            #crosstest[nbcross-1]
            line =data[int((datasize/nbcross)*i):]
            writefich(line,crosstest[i])
        #close file pb here
        """
"""
        for i in range(nbcross):
            cross[i].close()
            crosstest[i].close()
        """
"""
#crossvalidation
#decoupage des donné en 10 groupe aprrentissage d'un eta sur 9 test sur 1

#creation des bloc
data = [line for line in open("data.txt")]
#datasize = len(data)
#print(datasize)    
  
#crossvalid(10,data)

#Sfile.close()#?

#brouillon main

print("408")
#w0,w = perceptron(T,eta,"S.txt")


#cleandata

cleanIrisData("iris2.txt")


cleanSpamData("spambase2.txt")
cleanWdbcData("wdbc2.txt")

#creation base de test pour spambase iris et wdbc

#bug?
splitRandom("S_spambase2.txt","T_spambase2.txt","spambase2.txt")
splitRandom("S_iris2.txt","T_iris2.txt","iris2.txt")
splitRandom("S_wdbc2.txt","T_wdbc2.txt","wdbc2.txt")


(resW0,resW) = perceptron(T,eta,"S_spambase2.txt")
test(resW0,resW,"T_spambase2.txt")


(resW0,resW) = perceptron(T,eta,"S_iris2.txt")
test(resW0,resW,"T_iris2.txt")
(resW0,resW) = perceptron(T,eta,"S_wdbc2.txt")
test(resW0,resW,"T_wdbc2.txt")

"""
(resW0,resW) = adaline(T,eta,0.1,"spamS.txt")
print("resW0")
print(resW0)
print("resW")
print(resW)

print("fin")
"""
#autre algo ?
# autre data ?
#tableau recap ?
