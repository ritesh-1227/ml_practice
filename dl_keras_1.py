from keras.models import load_model
from keras.preprocessing.image import img_to_array
import cv2
import numpy as np


fd = cv2.CascadeClassifier(r'C:\Users\rites\Desktop\Study\Techienest\haarcascade_frontalface_default.xml')
model_ = load_model(r'C:\Users\rites\Desktop\Study\Techienest\_mini_XCEPTION.106-0.65.hdf5')
em = ['angry','disgusted','afraid','happy','sad','surprised','calm']
v = cv2.VideoCapture(0)
best_em = []
while(True):
    r, img = v.read()
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    f = fd.detectMultiScale(gray_img)
    if len(f)>0:
        [x,y,w,h] = f[0]
        roi = gray_img[y:y+h,x:x+w]
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),1)
        roi = cv2.resize(roi,(48,48))
        roi = roi.astype('float')/255.0
        roi = img_to_array(roi)
        roi = np.expand_dims(roi,axis = 0)
        p = list(model_.predict(roi)[0])
        best_em.append(em[p.index(max(p))])
##Dont do :    img = cv2.resize(img,(48,48))
    cv2.imshow('image',img)
    press_key = cv2.waitKey(1)
    if press_key == ord(chr(32)):
        v.release()
        cv2.destroyAllWindows()
        break
max_c = 0
max_exp = 'kuch_bhi'
for i in set(best_em):
    exp = i
##    print(i)
    if best_em.count(i) > max_c:
        max_c = best_em.count(i)
        max_exp = i

print('You look '+ max_exp)


