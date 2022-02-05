# rasmlarda orqa fonda bo`ladigan va hammani asabiga tegadigan watermark ni olib tashlash
# buning uchun bizga opencv moduli kerak bo`ladi
# uni o`rnatish uchun har doimgidek 
#   sudo apt update
#   sudo apt install python3-opencv
# buyruqlaridan foydalanish mumkin)))

import cv2 
import numpy as np 
     
     
def back_rm(filename): 
    img = cv2.imread('<rasm_nomi.jpg>') 
    # rasmni grayscale qilib o`zgartirib olamiz. 
    # Xullas, intensivligi katta nuqta oqroq, intensivligi kichik nuqta esa qoraroq  bo`lib ko`rinadi. 
    gr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
     
    bg = gr.copy() 
     
        # Morfologik o`zgartirishlar kiritish
        # batafsil: https://docs.opencv.org/3.4/d9/d61/tutorial_py_morphological_ops.html 
    for i in range(5): 
        kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, 
                                                (2 * i + 1, 2 * i + 1)) 
        bg = cv2.morphologyEx(bg, cv2.MORPH_CLOSE, kernel2) 
        bg = cv2.morphologyEx(bg, cv2.MORPH_OPEN, kernel2) 
     
        # subtract: ikkita grayscale qilib o`zgartirilgan rasmlar massivini bir-biridan ayirish
        # natijada hosil bo`lgan grayscale massivning minimal elementi nolga teng bo`ladi.
        # boshqacha aytganda, ayirish natijasida hosil bo`lgan barcha manfiy qiymatlar nolga tenglashtiriladi.  
    dif = cv2.subtract(bg, gr) 
     
        # thresholding: rasmni qismlarga ajratish
    bw = cv2.threshold(dif, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1] 
    dark = cv2.threshold(bg, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1] 
     
        # eng qoraroq bo`lgan sohadan piksellarni ajratib olish 
    darkpix = gr[np.where(dark > 0)] 
     
        # Qoraroq sohadan eng qora nuqtalarni ajratib olish uchun bu sohani yana qismlarga bo`lamiz. 
    darkpix = cv2.threshold(darkpix, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1] 
     
        # ajratib olingan qoraroq nuqtalarni watermark sohasiga qo`yish
    bw[np.where(dark > 0)] = darkpix.T 
     
      # natijaviy faylni saqlaymiz
    cv2.imwrite('final.jpg', bw) 
      
# ajratib olingan watermark faylni o`chirib tashlaymiz      
back_rm('watermark.jpg') 
