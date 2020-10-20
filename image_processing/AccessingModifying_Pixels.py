import cv2

img = cv2.imread('image_processing/datas/images/load_image.jpg')

print ('pixel img[100,100] values',img[100,100])
print('accessing only blue pixel',img[100,100,0])
img[100,100] = [255,255,255]
print('Modifying img[100,100] pixel values to [255,255,255]',img[100,100])

print('accessing RED value',img.item(10,10,2))

print('modifying RED value img.itemset((10,10,2),100)',img.item(10,10,2))

print('Image Properties - shape',img.shape)
print('Image Properties - size', img.size)
print('Image Properties - dtype',img.dtype)

# cv2.imshow('image',img)
# k = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
