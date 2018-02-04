from PIL import Image
import math
import cv2
import numpy as np


def normalize(hist):
	hist_np = np.array(hist, dtype=np.float32)
	hist_sum = sum(hist)
	hist_norm = hist_np / hist_sum
	return hist_norm.tolist()

image1b = Image.open('beach/1.jpeg').resize((500,325))         
image2b = Image.open('beach/2.jpeg').resize((500,325)) 
image3b = Image.open('beach/3.jpeg').resize((500,325))
image4b = Image.open('beach/beach1.jpg').resize((500,325))         
image5b = Image.open('beach/beach2.jpg').resize((500,325)) 
image6b = Image.open('beach/beach3.jpg').resize((500,325))
image7b = Image.open('beach/beach4.jpg').resize((500,325))         
image8b = Image.open('beach/beach5.jpg').resize((500,325)) 
image9b = Image.open('beach/beach6.jpg').resize((500,325))
image10b = Image.open('beach/beach7.jpg').resize((500,325))
image11b = Image.open('beach/beach8.jpg').resize((500,325))         
image12b = Image.open('beach/beach9.jpg').resize((500,325)) 
image13b = Image.open('beach/beach10.jpg').resize((500,325))
image14b = Image.open('beach/beach11.jpg').resize((500,325))
image15b = Image.open('beach/beach12.jpg').resize((500,325))
image1b_hist = normalize(image1b.histogram())     
image2b_hist = normalize(image2b.histogram()) 
image3b_hist = normalize(image3b.histogram())
image4b_hist = normalize(image4b.histogram())     
image5b_hist = normalize(image5b.histogram()) 
image6b_hist = normalize(image6b.histogram()) 
image7b_hist = normalize(image7b.histogram())     
image8b_hist = normalize(image8b.histogram()) 
image9b_hist = normalize(image9b.histogram()) 
image10b_hist = normalize(image10b.histogram())
image11b_hist = normalize(image11b.histogram()) 
image12b_hist = normalize(image12b.histogram()) 
image13b_hist = normalize(image13b.histogram())
image14b_hist = normalize(image14b.histogram()) 
image15b_hist = normalize(image15b.histogram())

image1c = Image.open('city/city1.jpg').resize((500,325))         
image2c = Image.open('city/city2.jpg').resize((500,325)) 
image3c = Image.open('city/city3.jpg').resize((500,325))
image4c = Image.open('city/city4.jpg').resize((500,325))         
image5c = Image.open('city/city5.jpeg').resize((500,325)) 
image6c = Image.open('city/city6.jpeg').resize((500,325))
image7c = Image.open('city/city7.jpg').resize((500,325))         
image8c = Image.open('city/city8.jpg').resize((500,325)) 
image9c = Image.open('city/city9.jpg').resize((500,325))
image10c = Image.open('city/city10.jpg').resize((500,325))
image11c = Image.open('city/city11.jpg').resize((500,325))         
image12c = Image.open('city/city12.jpg').resize((500,325)) 
image13c = Image.open('city/city13.png').resize((500,325))
image14c = Image.open('city/city14.jpg').resize((500,325))
image15c = Image.open('city/city15.jpg').resize((500,325))
image1c_hist = normalize(image1c.histogram())     
image2c_hist = normalize(image2c.histogram()) 
image3c_hist = normalize(image3c.histogram())
image4c_hist = normalize(image4c.histogram())     
image5c_hist = normalize(image5c.histogram()) 
image6c_hist = normalize(image6c.histogram())     
image7c_hist = normalize(image7c.histogram()) 
image8c_hist = normalize(image8c.histogram())
image9c_hist = normalize(image9c.histogram())     
image10c_hist = normalize(image10c.histogram()) 
image11c_hist = normalize(image11c.histogram())     
image12c_hist = normalize(image12c.histogram()) 
image13c_hist = normalize(image13c.histogram())
image14c_hist = normalize(image14c.histogram())     
image15c_hist = normalize(image15c.histogram()) 


image1m = Image.open('mountain/4.jpeg').resize((500,325))
image2m = Image.open('mountain/5.jpeg').resize((500,325))
image3m = Image.open('mountain/mount1.jpg').resize((500,325))
image4m = Image.open('mountain/mount2.jpg').resize((500,325))
image5m = Image.open('mountain/mount3.jpg').resize((500,325))
image6m = Image.open('mountain/mount4.jpg').resize((500,325))
image7m = Image.open('mountain/mount5.jpg').resize((500,325))
image8m = Image.open('mountain/mount6.jpg').resize((500,325))
image9m = Image.open('mountain/mount7.jpg').resize((500,325))
image10m = Image.open('mountain/mount8.jpeg').resize((500,325))
image11m = Image.open('mountain/mount9.jpg').resize((500,325))
image12m = Image.open('mountain/mount10.jpg').resize((500,325))
image13m = Image.open('mountain/mount11.jpg').resize((500,325))
image14m = Image.open('mountain/mount12.jpg').resize((500,325))
image15m = Image.open('mountain/mount13.jpg').resize((500,325))
image1m_hist = normalize(image1m.histogram())     
image2m_hist = normalize(image2m.histogram()) 
image3m_hist = normalize(image3m.histogram())
image4m_hist = normalize(image4m.histogram())     
image5m_hist = normalize(image5m.histogram()) 
image6m_hist = normalize(image6m.histogram())
image7m_hist = normalize(image7m.histogram())     
image8m_hist = normalize(image8m.histogram()) 
image9m_hist = normalize(image9m.histogram())
image10m_hist = normalize(image10m.histogram())     
image11m_hist = normalize(image11m.histogram()) 
image12m_hist = normalize(image12m.histogram()) 
image13m_hist = normalize(image13m.histogram())
image14m_hist = normalize(image14m.histogram())     
image15m_hist = normalize(image15m.histogram()) 



dataset = [
    (image1b_hist),                     
    (image2b_hist),
    (image3b_hist),
    (image4b_hist),                     
    (image5b_hist),
    (image6b_hist),
    (image7b_hist),                     
    (image8b_hist),
    (image9b_hist),
    (image10b_hist),                     
    (image11b_hist),
    (image12b_hist),
    (image13b_hist),
    (image14b_hist),
    (image15b_hist),
    (image1c_hist),                     
    (image2c_hist),
    (image3c_hist),
    (image4c_hist),                     
    (image5c_hist),
    (image6c_hist),
    (image7c_hist),                     
    (image8c_hist),
    (image9c_hist),
    (image10c_hist),                     
    (image11c_hist),
    (image12c_hist),
    (image13c_hist),
    (image14c_hist),
    (image15c_hist),
    (image1m_hist),
    (image2m_hist),
    (image3m_hist),
    (image4m_hist),
    (image5m_hist),
    (image6m_hist),
    (image7m_hist),
    (image8m_hist),
    (image9m_hist),
    (image10m_hist),
    (image11m_hist),
    (image12m_hist),
    (image13m_hist),
    (image14m_hist),
    (image15m_hist)


]

labels = [
   0,              
   0,
   0,
   0,              
   0,             
   0,
   0,
   0,              
   0,           
   0,
   0,
   0,              
   0,
   0,
   0,
   1,
   1,
   1,
   1,
   1,
   1,
   1,
   1,
   1,
   1,
   1,
   1,
   1,
   1,
   1,
   2,
   2,
   2,
   2,
   2,
   2,
   2,
   2,
   2,
   2,
   2,
   2,
   2,
   2,
   2

]

knn =cv2.KNearest()

dataset_np = np.array(dataset, dtype=np.float32)
labels_np = np.array(labels, dtype=np.float32)

knn.train(dataset_np, labels_np)

imageToTest = Image.open('testM.jpg').resize((500,325))  

test_hist =  normalize(imageToTest.histogram()) 

input_data = [
 test_hist                         
]

input_data_np = np.array(input_data, dtype=np.float32)

retval, results, neighbours, distances = knn.find_nearest(input_data_np, k=2)

print(neighbours, distances)


print(results)

if retval <1:
	print("It's a picture of a beach")
elif retval >1:
	print ("It's a picture of a mountain")
else:
   print ("It's a picture of a city")

