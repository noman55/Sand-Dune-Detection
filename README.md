# Sand-Dune-Detection
This is used to detect Sand Dunes on Martian Surface 
Here I have used Image Processing techique called LBP(local binary pattern), the reason being it is illumination invarient
it is (LBP) is texture based technique where ever similar texture maches it will consider it as same texture so, basically shadow effect is gone here 

After applying LBP now we apply ML techiques here I have used KNN algo because it gives 95% of accuracy 
I have created data into two data set one is the sand which is a part of dune and other is texture which is not a dune part 
and given them labels as 1 and 0 respectively 
data contains images of sizes 100px by 100px 

and third part is to traverese image and predict the result 
image traversal is done by square grid of size 100px by 100px 
