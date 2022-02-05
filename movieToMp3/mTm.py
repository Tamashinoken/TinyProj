import os
from moviepy.editor import *
##########################################|
# Agar ushbu modul o`rnatilmagan bo`lsa,  |
# python -m pip install moviepy           | 
# buyrug`i orqali o`rnatishingiz mumkin.  |
##########################################|


# video klipni ochib olamiz. Bunda <fayl_nomi.mp4> ning o`rniga 
# o`zingiz o`zgartirmoqchi bo`lgan fayl nomini kiritasiz.
# Faylga borish yo`lini to`gri ko`rsating yoki 
# pmTm.py fayli va video fayl bitta papkaning ichida bo`lishi kerak.

video = VideoFileClip(os.path.join("<fayl_nomi.mp4>"))  
# Keyin mp4 faylni mp3 ga aylantirib <audio_fayl.mp3> nomi bilan saqlaymiz
# Faylga o`zingiz xohlagancha nom berishingiz mumkin
video.audio.write_audiofile(os.path.join("the_rumbling.mp3"))
