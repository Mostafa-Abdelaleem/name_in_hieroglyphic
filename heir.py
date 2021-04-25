#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 08:09:13 2021

@author: 3m
"""

# importing required libraries
import cv2
import os
import matplotlib.pyplot as plt

#reading name
while True:
    name=input('please enter your name: ')
    if name: break
name=name.lower()

# Getting corresponding images
ImagesPath='./imgs'
imgList=[]
for letter in name:
    imgName=os.path.join(ImagesPath,letter+'.png')
    # print(imgName)
    try:
        imgList.append(cv2.imread(imgName))
    except:
        print('wrong set of characters, please use letters only\nPlease try again')
        quit()

#creating the full name image and displaying it
try: 
    NameInHeir = cv2.hconcat(imgList)
    cv2.imshow('Your Name In Hieroglyphic',NameInHeir)
except:
        print('wrong set of characters, please use letters only\nPlease try again')
        quit()

print('Check the image and press any key to proceed or wait 3 seconds\n')
cv2.waitKey(3000)
cv2.destroyAllWindows()

print('**************** Do you want to save image ****************\nanswer with yes(y) or no (no)')
check=input()

if  check == 'yes' or check == 'y':
    while True:
        path = input('please enter the path to save the image:\n')
        if path: break
    
    if    cv2.imwrite(os.path.join(path , 'NameInHeir.png'), NameInHeir):
        print('Saved as NameInHeir.png in',path,'\nBye Bye pharaoh :D')
    else:
        print('Failed to save image:(\nplease try again and make sure you provide the correct path')
        