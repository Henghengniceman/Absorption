# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 16:22:47 2020

@author: Hengheng Zhang

E-Mail: hengheng.zhang@kit.edu

Function： calcuate absorption 

"""
import datetime
import pandas as pd
import os 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

#%% Read MA 200
MA200DataSet = pd.read_csv('../Data/30s/MA200-0211_S0086_201011160430.csv')
MA200DateTime =list(MA200DataSet.iloc[:,6])  
MA200tt=[]
for i in range(0,len(MA200DateTime)):
    MA200DateTime[i]=datetime.datetime.strptime(MA200DateTime[i].replace('T',' '),"%Y-%m-%d %H:%M:%S")
    MA200tt.append(datetime.datetime.timestamp(MA200DateTime[i]))
#%% IRBCC
MA200BCC880=np.array(list(MA200DataSet.iloc[:,75])) 
MA200BCC625=np.array(list(MA200DataSet.iloc[:,72])) 
MA200BCC528=np.array(list(MA200DataSet.iloc[:,69])) 
MA200BCC470=np.array(list(MA200DataSet.iloc[:,66])) 
MA200BCC375=np.array(list(MA200DataSet.iloc[:,63])) 

#%% read AE51
AE51DataSet = pd.read_csv('../Data/30s/AE51-S6-1225_20201011-160400.csv',sep='|', header=0, skiprows=15)
AE51DataSet=list(AE51DataSet.iloc[:,0]) 

AE51DataStrAll=[]
for i  in range (0,len(AE51DataSet)):
    AE51DataStrAll.append(AE51DataSet[i].split(','))
    
AE51DateTime = []
AE51tt=[]
AE51BCC = []
for i  in range (1,len(AE51DataStrAll)):
    AE51DateTime.append(datetime.datetime.strptime(AE51DataStrAll[i][0]+' '+AE51DataStrAll[i][1],"%Y/%m/%d %H:%M:%S"))
    AE51tt.append(datetime.datetime.timestamp(AE51DateTime[i-1]))
    AE51BCC.append(float(AE51DataStrAll[i][9]))
AE51BCC = np.array(list(AE51BCC))
#%% read AE33 right 
AE33DataSetAll = []
for Filename in  os.listdir('../Data/30s/AE33'):
    AE33DataSet  = pd.read_csv(('../Data/30s/AE33/'+Filename),header=None)
    AE33DataSet = list(AE33DataSet.iloc[:,0])  
    AE33DataSetAll.extend(AE33DataSet[5:])
aa=AE33DataSet[4].split(' ')
AE33DataStrAll = []
for i  in range (0,len(AE33DataSetAll)):
    AE33DataStrAll.append(AE33DataSetAll[i].split(' '))

AE33DateTime = []
AE33tt =[]
AE33BCC370 =[]
AE33BCC470 =[]
AE33BCC520 =[]
AE33BCC590 =[]
AE33BCC880 =[]

for i  in range (0,len(AE33DataStrAll)):
    AE33DateTime.append(datetime.datetime.strptime(AE33DataStrAll[i][0]+' '+AE33DataStrAll[i][1],"%Y/%m/%d %H:%M:%S"))
    AE33tt.append(datetime.datetime.timestamp(AE33DateTime[i]))
    AE33BCC370.append(float(AE33DataStrAll[i][40]))
    AE33BCC470.append(float(AE33DataStrAll[i][43]))
    AE33BCC520.append(float(AE33DataStrAll[i][46]))
    AE33BCC590.append(float(AE33DataStrAll[i][49]))
    AE33BCC880.append(float(AE33DataStrAll[i][55]))
    
AE33BCC370 = np.array(list(AE33BCC370))
AE33BCC470 = np.array(list(AE33BCC470))
AE33BCC520 = np.array(list(AE33BCC520))
AE33BCC590 = np.array(list(AE33BCC590))
AE33BCC880 = np.array(list(AE33BCC880))

#%% selcet data 
# MA200DateTimeS =MA200DateTime[0:7566]
# MA200BCCS =MA200BCC[0:7566]
# MA200ttS =MA200tt[0:7566]

# AE51DateTimeS =AE51DateTime
# AE51BCCS =AE51BCC
# AE51ttS =AE51tt

MA200tt=np.array(MA200tt)
AE51tt = np.array(AE51tt)

AE33DateTimeS =AE33DateTime[964:]
AE33ttS =AE33tt[964:]
AE33BCC370=AE33BCC370[964:]
AE33BCC470=AE33BCC470[964:]
AE33BCC520=AE33BCC520[964:]
AE33BCC590=AE33BCC590[964:]
AE33BCC880=AE33BCC880[964:]


Halfmin = (AE33ttS[1]-AE33ttS[0])/2

def find_index(src_list, target):

    dst_index_list = []

    for index in range(len(src_list)):
        if (src_list[index] == target):
            dst_index_list.append(index)

    return dst_index_list

# MA200BCC=np.where(MA200BCC > 0, MA200BCC, np.nan)
# AE51BCC=np.where(AE51BCC > 0, AE51BCC, np.nan)
# MA200BCC = np.abs(MA200BCC)
# AE51BCC=np.abs(AE51BCC)
MA200BCCAverage880 = []
MA200BCCAverage625 = []
MA200BCCAverage528 = []
MA200BCCAverage470 = []
MA200BCCAverage375 = []

AE51BCCAverage =[]
for i in range(0,len(AE33ttS)):
    MA200BCCAverage880.append(np.nanmean(MA200BCC880[(MA200tt>AE33ttS[i]-Halfmin)*(MA200tt<AE33ttS[i]+Halfmin)]))
    MA200BCCAverage625.append(np.nanmean(MA200BCC625[(MA200tt>AE33ttS[i]-Halfmin)*(MA200tt<AE33ttS[i]+Halfmin)]))
    MA200BCCAverage528.append(np.nanmean(MA200BCC528[(MA200tt>AE33ttS[i]-Halfmin)*(MA200tt<AE33ttS[i]+Halfmin)]))
    MA200BCCAverage470.append(np.nanmean(MA200BCC470[(MA200tt>AE33ttS[i]-Halfmin)*(MA200tt<AE33ttS[i]+Halfmin)]))
    MA200BCCAverage375.append(np.nanmean(MA200BCC375[(MA200tt>AE33ttS[i]-Halfmin)*(MA200tt<AE33ttS[i]+Halfmin)]))

    AE51BCCAverage.append(np.nanmean(AE51BCC[(AE51tt>AE33ttS[i]-Halfmin)*(AE51tt<AE33ttS[i]+Halfmin)]))
    # aa=AE51BCC[(AE51tt>AE33ttS[i]-Halfmin)*(AE51tt<AE33ttS[i]+Halfmin)]
#%%

# RangeIndex = 2666
with plt.style.context(['science','no-latex']):
    fig, ax = plt.subplots()
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    # ax.xaxis.set_major_locator(mdates.HourLocator())
    ax.plot(AE33DateTimeS,MA200BCCAverage375, label='MA200')
    ax.plot(AE33DateTimeS,AE33BCC370, label='AE33')
    ax.plot(AE33DateTimeS,AE51BCCAverage, label='AE51')
    # ax.title('Wavelength:MA200@357nm,AE33@370nm')
    plt.text(x=0.5, y=0.94, s="Wavelength:MA200@375nm,AE33@370nm", ha="center", transform=fig.transFigure)

    ax.legend()
    # ax.set_xlim([0, 6])
    # ax.set_ylim([0, 1500])
    ax.set(xlabel='Measurement Time [2018/10/11-2018/10/12]')
    ax.set(ylabel='BC Concentration [$\mu$m] ')  
    # ax.autoscale(tight=True)
    fig.savefig('../Figure/30s/Wavelength(MA200@375nmAE33@370nm).jpg',dpi=300)
    plt.close()

with plt.style.context(['science','no-latex']):
    fig, ax = plt.subplots()
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    # ax.xaxis.set_major_locator(mdates.HourLocator())
    ax.plot(AE33DateTimeS,MA200BCCAverage470, label='MA200')
    ax.plot(AE33DateTimeS,AE33BCC470, label='AE33')
    ax.plot(AE33DateTimeS,AE51BCCAverage, label='AE51')
    # ax.title('Wavelength:MA200@357nm,AE33@370nm')
    plt.text(x=0.5, y=0.94, s="Wavelength:MA200@470nm,AE33@470nm", ha="center", transform=fig.transFigure)

    ax.legend()
    # ax.set_xlim([0, 6])
    # ax.set_ylim([0, 1500])
    ax.set(xlabel='Measurement Time [2018/10/11-2018/10/12]')
    ax.set(ylabel='BC Concentration [$\mu$m] ')  
    # ax.autoscale(tight=True)
    fig.savefig('../Figure/30s/Wavelength(MA200@470nmAE33@470nm).jpg',dpi=300)
    plt.close()

with plt.style.context(['science','no-latex']):
    fig, ax = plt.subplots()
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    # ax.xaxis.set_major_locator(mdates.HourLocator())
    ax.plot(AE33DateTimeS,MA200BCCAverage528, label='MA200')
    ax.plot(AE33DateTimeS,AE33BCC520, label='AE33')
    ax.plot(AE33DateTimeS,AE51BCCAverage, label='AE51')
    # ax.title('Wavelength:MA200@357nm,AE33@370nm')
    plt.text(x=0.5, y=0.94, s="Wavelength:MA200@528nm,AE33@520nm", ha="center", transform=fig.transFigure)

    ax.legend()
    # ax.set_xlim([0, 6])
    # ax.set_ylim([0, 1500])
    ax.set(xlabel='Measurement Time [2018/10/11-2018/10/12]')
    ax.set(ylabel='BC Concentration [$\mu$m] ')  
    # ax.autoscale(tight=True)
    fig.savefig('../Figure/30s/Wavelength(MA200@528nmAE33@520nm).jpg',dpi=300)
    plt.close()

with plt.style.context(['science','no-latex']):
    fig, ax = plt.subplots()
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    # ax.xaxis.set_major_locator(mdates.HourLocator())
    ax.plot(AE33DateTimeS,MA200BCCAverage625, label='MA200')
    ax.plot(AE33DateTimeS,AE33BCC590, label='AE33')
    ax.plot(AE33DateTimeS,AE51BCCAverage, label='AE51')
    # ax.title('Wavelength:MA200@357nm,AE33@370nm')
    plt.text(x=0.5, y=0.94, s="Wavelength:MA200@625nm,AE33@590nm", ha="center", transform=fig.transFigure)

    ax.legend()
    # ax.set_xlim([0, 6])
    # ax.set_ylim([0, 1500])
    ax.set(xlabel='Measurement Time [2018/10/11-2018/10/12]')
    ax.set(ylabel='BC Concentration [$\mu$m] ')  
    # ax.autoscale(tight=True)
    
    fig.savefig('../Figure/30s/Wavelength(MA200@625nmAE33@590nm).jpg',dpi=300)
    plt.close()

with plt.style.context(['science','no-latex']):
    fig, ax = plt.subplots()
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    # ax.xaxis.set_major_locator(mdates.HourLocator())
    ax.plot(AE33DateTimeS,MA200BCCAverage880, label='MA200')
    ax.plot(AE33DateTimeS,AE33BCC880, label='AE33')
    ax.plot(AE33DateTimeS,AE51BCCAverage, label='AE51')
    # ax.title('Wavelength:MA200@357nm,AE33@370nm')
    plt.text(x=0.5, y=0.94, s="Wavelength:MA200@880nm,AE33@880nm", ha="center", transform=fig.transFigure)

    ax.legend()
    # ax.set_xlim([0, 6])
    # ax.set_ylim([0, 1500])
    ax.set(xlabel='Measurement Time [2018/10/11-2018/10/12]')
    ax.set(ylabel='BC Concentration [$\mu$m] ')  
    # ax.autoscale(tight=True)
    fig.savefig('../Figure/30s/Wavelength(MA200@880nmAE33@880nm).jpg',dpi=300)
    plt.close()


