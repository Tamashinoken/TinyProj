import pandas as pd
import matplotlib.pyplot as plt


# data.txt fayldan ma'lumotlarni olib, ularni ustun ko`rinishida o`qiydi
data = pd.read_csv('data.txt', sep='\s+', header=None)
pd.DataFrame(data)

# x massivga jadvalning 1-ustuni (raqamlash 0 dan boshlanadi) elementlarini beradi
# y massivga esa 2-ustun elementlari
x = data[0]
y = data[1]

# grafik yashil rangli (g kalit so`zi rangni bildiradi) nuqtalar (d nuqtani bildiradi) ko`rinishida uzluksiz chiziq holatida chiziladi
plt.plot(x, y, 'gd-')
plt.show()
