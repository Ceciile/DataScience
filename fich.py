#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on 10th Janv 2018

@author: Qianqian
"""

import random as random
import numpy as np

line='e,x,s,g,f,n,f,w,b,k,t,e,s,s,w,w,p,w,o,e,n,a,g'
new_s=''
if(line.split(",")[0] == "e"):
   for c in line.split(",")[1:]:
       new_s = new_s +' '+ str(ord(c)-96)
       print len(c)
   print  "+1"+new_s+"\n"
"""
if(line.split(",")[0] == "p\n"):
        #cleanData.write(newLine)
        for c in line.split(",")[1:]:
	    new_s = new_s +' '+ str(ord(c)-96)
        newLine = "+1"+new_s+'\n'
        print(newLine,"dasdasd")
elif line.split(",")[0] == "e\n":
            for c in line.split(",")[1:]:
	        new_s = new_s +' '+ str(ord(c)-96)
            newLine = "-1"+new_s+'\n'
            print(newLine)"""

