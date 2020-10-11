# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 16:22:47 2020

@author: Hengheng Zhang

E-Mail: hengheng.zhang@kit.edu

Function： calcuate observation 

"""
import datetime
import pandas as pd
import os 
# Read MA 200
MA200DataSet = pd.read_csv('../Data/MA200-0211_S0084_201010184901.csv')
MA200DateTime =list(MA200DataSet.iloc[:,6])  
MA200tt=[]
for i in range(0,len(MA200DateTime)):
    MA200DateTime[i]=datetime.datetime.strptime(MA200DateTime[i].replace('T',' '),"%Y-%m-%d %H:%M:%S")
    MA200tt.append(datetime.datetime.timestamp(MA200DateTime[i]))
# read AE51
AE51DataSet = pd.read_csv('../Data/AE51-S6-1225_20201010-184900.csv',sep='|', header=0, skiprows=15)
AE51DataSet=list(AE51DataSet.iloc[:,0]) 

AE51DataStrAll=[]
for i  in range (0,len(AE51DataSet)):
    AE51DataStrAll.append(AE51DataSet[i].split(','))
    
AE51DateTime = []
AE51tt=[]
for i  in range (0,len(AE51DataStrAll)):
    AE51DateTime.append(datetime.datetime.strptime(AE51DataStrAll[i][0]+' '+AE51DataStrAll[i][1],"%Y/%m/%d %H:%M:%S"))
    AE51tt.append(datetime.datetime.timestamp(AE51DateTime[i]))
# read AE33
AE33DataSetAll = []
for Filename in  os.listdir('../Data/AE33'):
    AE33DataSet  = pd.read_csv(('../Data/AE33/'+Filename),header=None)
    AE33DataSet = list(AE33DataSet.iloc[:,0])  
    AE33DataSetAll.extend(AE33DataSet[5:])

AE33DataStrAll = []
for i  in range (0,len(AE33DataSetAll)):
    AE33DataStrAll.append(AE33DataSetAll[i].split(' '))

AE33DateTime = []
AE33tt =[]
for i  in range (0,len(AE33DataStrAll)):
    AE33DateTime.append(datetime.datetime.strptime(AE33DataStrAll[i][0]+' '+AE33DataStrAll[i][1],"%Y/%m/%d %H:%M:%S"))
    AE33tt.append(datetime.datetime.timestamp(AE33DateTime[i]))
