# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 13:28:47 2018
Traffic congestion statistics 
Input: the UTN path
Output: the figure of congestion roads per hour 
@author: autumn
"""
import numpy as np
import matplotlib.pyplot as plt

def congestionStatistics(path):
    
    roads_number = np.zeros((7,24))
    
    for i in range(5,12):
        file0=open(path + "Bus-utn\\Bus-utn-volume\\Day-201803" + '%02d' % i+ "-bus-volume.txt",'rb+')#
        file1=open(path + "Bus-utn\\Bus-utn-speed\\Day-201803" + '%02d' % i+ "-bus-speed.txt",'rb+')#
        file2=open(path + "Taxi-utn\\Taxi-utn-volume\\Day-201803" + '%02d' % i+ "-taxi-volume.txt",'rb+')#
        file3=open(path + "Taxi-utn\\Taxi-utn-speed\\Day-201803" + '%02d' % i+ "-taxi-speed.txt",'rb+')#
        while 1:
            line0 = file0.readline()
            line1 = file1.readline()
            line2 = file2.readline()
            line3 = file3.readline()
            
            
            if not line0:
                break
            if line0 == '' or line0 == None:
                break
            if not line1:
                break
            if line1 == '' or line1 == None:
                break
            
            
            line0 = line0.decode('utf8').replace("\r\n",'').split(',')
            line1 = line1.decode('utf8').replace("\r\n",'').split(',')
            line2 = line2.decode('utf8').replace("\r\n",'').split(',')
            line3 = line3.decode('utf8').replace("\r\n",'').split(',')
                        
            
            for j in range(1,25):
                if ( int(line0[j]) > 40 and int(float(line1[j])) < 10 ) or ( int(line2[j]) > 40 and int(float(line3[j])) < 10 ):
                  roads_number[i-5][j-1] += 1;
            
        file0.close()
        file1.close()
        file2.close()
        file3.close()
    
    x = []
    
    for i in range(0,24):
        x.append(i)
        
    for row in list(roads_number):
        plt.plot(x,row,"-",label="number"+ str('%02d' % i))
    plt.show()
    
    
path = "C:\\Users\\autumn\Desktop\\我的论文\\scientific data\\新建文件夹 (2)\\UTN\\" # change path to the UTN path
congestionStatistics(path)
    
    
    
