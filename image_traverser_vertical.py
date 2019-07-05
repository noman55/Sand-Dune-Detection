# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 14:28:12 2019

@author: rrscw
"""
# -*- coding: utf-8 -*-
'''
Image traversing algorithm : COMPLETE VERTICAL MASK
'''

import cv2
import  numpy as np


#read the same image in color for drawing colored rectangle
image_for_output=cv2.imread("2.png",1)

def image_draw(y_start,y_end,x_start,x_end):
    global image_for_output
    #draws a rectangle on the image from specified points
    image_for_output = cv2.rectangle(image_for_output,(x_start,y_start),(x_end,y_end),(0,255,0),3)
    cv2.imshow("",image_for_output)
    cv2.waitKey()
    cv2.destroyAllWindows()

#the greyscale image to be analyzed
image=cv2.imread("2.png",0)
image_for_output=cv2.imread("2.png",1)

vertical_mask_length=100
vertical_mask_height=100
pass_density=4

#HORIZONTAL
number_of_whole_passes_possible_x=int(image.shape[1]/vertical_mask_length)-1          #we will leave the last pass as its traversed in the 2nd last 
density_passes_made_x=pass_density*number_of_whole_passes_possible_x
x_spacing=int(vertical_mask_length/pass_density)

#VERTICAL
number_of_whole_passes_possible_y=int(image.shape[0]/vertical_mask_height)-1        #we will leave the last pass as its traversed in the 2nd last 
density_passes_made_y=pass_density*number_of_whole_passes_possible_y
y_spacing=int(vertical_mask_height/pass_density)

'''
print(number_of_whole_passes_possible_x)
print(density_passes_made_x)
print(x_spacing)
print(" ")
print(number_of_whole_passes_possible_y)
print(density_passes_made_y)
print(y_spacing)
'''

for i in range(density_passes_made_x):
    x_start=i*x_spacing
    for j in range(density_passes_made_y):
        y_start=j*y_spacing
        image_sliced=image[y_start: (y_start+vertical_mask_height), x_start : (x_start + vertical_mask_length)]      #OPPOSITE FORMAT!!    (HEIGHT!!!=ROWS=X)
        image_draw(y_start,y_start+vertical_mask_height,x_start,x_start + vertical_mask_length)
       
        
        

    




