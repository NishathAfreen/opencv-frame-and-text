import cv2
img=cv2.imread(r'C:\Users\nishath afreen\Desktop\afrin.jpg')
img=cv2.rectangle(img, (200,210),(15,10),(0,255,0),2)
dimensions=img.shape
print(dimensions)
img=cv2.putText(img,"APPLE",(100,30),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),1,cv2.LINE_AA)
cv2.imshow('apple',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
