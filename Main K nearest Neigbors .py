# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 20:55:42 2019

@author: DELL
"""

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
import os
import numpy as np
from sklearn import preprocessing, neighbors, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import skimage.feature

##################################TUNING LBP PARAMETERS
radius=6
n_points=15
METHOD="uniform"

#TEXTURE1 files
sand_ripple=[]

for x in os.listdir("sand_ripple"):
    if '.png' in x:
        x='sand_ripple/'+x
        sand_ripple=np.append(sand_ripple,x)
    
print(sand_ripple)

#TEXTURE2 files
sand_fine=[]

for x in os.listdir("sand_fine"):
    if '.png' in x:
        x='sand_fine/'+x
        sand_fine=np.append(sand_fine,x)
    
print(sand_fine)

#TEXTURE3 files
terrain=[]

for x in os.listdir("terrain"):
    if '.png' in x:
        x='terrain/'+x
        terrain=np.append(terrain,x)
    
print(terrain)

#all texture files
texture=[]
texture=np.append(texture,sand_ripple)
texture=np.append(texture,sand_fine)
texture=np.append(texture,terrain)

#defined FEATURES
X=[]


#generating all features and appending to X
for i in range(len(texture)):
    image= skimage.io.imread(texture[i],as_grey=True)
    lbp = skimage.feature.local_binary_pattern(image, n_points, radius, METHOD)
    n_bins = int(lbp.max() + 1)
    a=np.histogram(lbp.ravel(),normed=True, bins=n_bins, range=(0, n_bins))
    X=np.append(X,a[0])

#generating feature table/matrix    
X=np.reshape(X,(len(texture),n_bins))

#LABEL FOR TEXTURE1
y1=np.ones(len(sand_ripple),int)                         #MUST BE single array not matrix
#LABEL FOR TEXTURE2
y2=np.ones(len(sand_fine),int)                            #MUST BE single array not matrix
#LABEL FOR TEXTURE2
y3=np.zeros(len(terrain),int)                            #MUST BE single array not matrix

#ALL LABELS
y=[]
y=np.append(y,y1)
y=np.append(y,y2)
y=np.append(y,y3) 
                                     
print(X)
print(y)

X_train,X_test,y_train,y_test=train_test_split(X , y , test_size=0.2)

clf=neighbors.KNeighborsClassifier()
#clf=svm.SVC()
#clf=LinearRegression()

clf.fit(X_train,y_train)
accuracy=clf.score(X_test,y_test)
print(accuracy)

#read the same image in color for drawing colored rectangle

def image_draw(y_start,y_end,x_start,x_end):
    global image_for_output
    '''
    global vertical_mask_length
    center_x= x_start+int(vertical_mask_length/2)
    center_y= y_start+int(vertical_mask_length/2)
    '''
    #draws a circle point on the image from specified points
    cv2.circle(image_for_output,(x_start,y_start), 5, (0,255,255), -1)
    cv2.circle(image_for_output,(x_start,y_end), 5, (0,255,255), -1)
    cv2.circle(image_for_output,(x_end,y_start), 5, (0,255,255), -1)
    cv2.circle(image_for_output,(x_end,y_end), 5, (0,255,255), -1)


    #draws a rectangle on the image from specified points
    #image_for_output = cv2.rectangle(image_for_output,(x_start,y_start),(x_end,y_end),(0,255,0),3)
 

def test_sliced_image(test_image):
    test_X=[]
    lbp = skimage.feature.local_binary_pattern(test_image, n_points, radius, METHOD)
    n_bins = int(lbp.max() + 1)
    a=np.histogram(lbp.ravel(),normed=True, bins=n_bins, range=(0, n_bins))
    test_X=np.append(test_X,a[0])
    test_X=np.reshape(test_X,(1,n_bins))
    global clf
    result=clf.predict(test_X)
    print(result)
    return result

IMAGE='large_field.png'
IMAGE_SAVE='large_field2_circle_pd2_100px.png'
pass_density=2
vertical_mask_length=100
vertical_mask_height=100


#the greyscale image to be analyzed
image=cv2.imread(IMAGE,0)
image_for_output=cv2.imread(IMAGE,1)


#HORIZONTAL
number_of_whole_passes_possible_x=int(image.shape[1]/vertical_mask_length)-1          #we will leave the last pass as its traversed in the 2nd last 
density_passes_made_x=pass_density*number_of_whole_passes_possible_x
x_spacing=int(vertical_mask_length/pass_density)

#VERTICAL
number_of_whole_passes_possible_y=int(image.shape[0]/vertical_mask_height)-1        #we will leave the last pass as its traversed in the 2nd last 
density_passes_made_y=pass_density*number_of_whole_passes_possible_y
y_spacing=int(vertical_mask_height/pass_density)


for i in range(density_passes_made_x):
    x_start=i*x_spacing
    for j in range(density_passes_made_y):
        y_start=j*y_spacing
        image_sliced=image[y_start: (y_start+vertical_mask_height), x_start : (x_start + vertical_mask_length)]      #OPPOSITE FORMAT!!    (HEIGHT!!!=ROWS=X)
        test_result=test_sliced_image(image_sliced)
        if (test_result==1):
            image_draw(y_start,y_start+vertical_mask_height,x_start,x_start + vertical_mask_length)
                
        
cv2.imshow("",image_for_output)
cv2.imwrite(IMAGE_SAVE,image_for_output)
cv2.waitKey()
cv2.destroyAllWindows()       





