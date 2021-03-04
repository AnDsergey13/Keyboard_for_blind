#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton)
from PyQt5.QtCore import pyqtSlot, QRect, QCoreApplication

class KeyBoard(object):
	def __init__(self, width=500, height=500, x_offset=300, y_offset=300):
		self.app = QApplication(sys.argv)
		self.w = QWidget()
		self.w.setWindowTitle('Клавиатура')
		self.w.resize(width, height)
		self.w.move(x_offset, y_offset)

	def set_size_button(self, width=60, height=60):
		self.width_button = width
		self.height_button = height


	def create_button(self, x, y, width, height, text="Empty"):
		self.pushButton = QPushButton(self.w)
		self.pushButton.setGeometry(QRect(x, y, width, height))
		self.pushButton.setText(text)

	def print_window(self):
		self.w.show()
		sys.exit(self.app.exec_())

row_1 = ["Esc","F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","F11","F12"]
row_2 = ["ё(ёлка)","1","2","3","4","5","6","7","8","9","0","-","=","Backspace"]
row_3 = ["Tab", "й(йогурт)", "ц(цапля)","у(улитка)","к(корова)","е(енот)","н(нос)","г(голос)","ш(шар)","щ(щука)","з(зима)","х(хомяк)","твёрдый знак","Enter"]
row_4 = ["Caps Lock", "ф(фазан)", "ы","в(ворона)","а(арбуз)","п(палка)","р(рак)","о(овёс)","л(лиса)","д(дача)","ж(жизнь)","э(эскимо)","обратная косая черта"]

W_BUT = 60
H_BUT = 60

k = KeyBoard(1200, 400)
k.set_size_button(W_BUT, H_BUT)
## Первый ряд
# Esc
k.create_button(0, 0, W_BUT, H_BUT, row_1[0])
#f1-f4
for pos in range(1, 5):
	k.create_button(W_BUT*(pos+1), 0, W_BUT, H_BUT, row_1[pos])
#f5-f8
for pos in range(5, 9):
	k.create_button((W_BUT*(pos+1)+int(W_BUT/2)), 0, W_BUT, H_BUT, row_1[pos])
#f9-f12
for pos in range(9, 13):
	k.create_button((W_BUT*(pos+2)), 0, W_BUT, H_BUT, row_1[pos])

## Второй ряд
for pos in range(0, len(row_2)-1):
	k.create_button(W_BUT*pos, H_BUT, W_BUT, H_BUT, row_2[pos])
# Backspace
k.create_button(W_BUT*13, H_BUT, W_BUT*2, H_BUT, row_2[13])

## Третий ряд
# Tab
k.create_button(0, H_BUT*2, W_BUT+int(W_BUT/2), H_BUT, row_3[0])
for pos in range(1, len(row_3)-1):
	k.create_button(W_BUT*pos+int(W_BUT/2), H_BUT*2, W_BUT, H_BUT, row_3[pos])
# Enter
k.create_button(W_BUT*(len(row_3)-1)+int(W_BUT/2)+int(W_BUT/6), H_BUT*2, W_BUT+int(W_BUT/2), H_BUT, row_3[len(row_3)-1])

## Четвёртый ряд
# Caps Lock
k.create_button(0, H_BUT*3, W_BUT+int(W_BUT/2+W_BUT/6), H_BUT, row_4[0])
for pos in range(1, len(row_4)):
	k.create_button(W_BUT*pos+int(W_BUT/2), H_BUT*3, W_BUT, H_BUT, row_4[pos])



k.print_window()


# if __name__ == '__main__':

# 	app = QApplication(sys.argv)

# 	w = QWidget()
# 	w.resize(500, 150)
# 	w.move(300, 300)
# 	w.setWindowTitle('Simple')
# 	w.pushButton = QPushButton(w)
# 	w.pushButton.setGeometry(QRect(0, 60, 60, 60))
# 	w.pushButton.setText("text")

# 	w.show()

# 	sys.exit(app.exec_())

# tts = pyttsx3.init()
# rate = tts.getProperty('rate') #Скорость произношения
# tts.setProperty('rate', rate-65)
# volume = tts.getProperty('volume') #Громкость голоса
# tts.setProperty('volume', volume+0.9)
# voices = tts.getProperty('voices')
# # Задать голос по умолчанию
# tts.setProperty('voice', 'ru') 
# # Попробовать установить предпочтительный голос
# for voice in voices:
# 	if voice.name == 'Anna':
# 		tts.setProperty('voice', voice.id)

# @pyqtSlot()
# def button_A(self):
# 	self.tts.say('Иван васильевич')
# 	self.tts.runAndWait()

# @pyqtSlot()
# def button_B(self):
# 	self.tts.say('Говорит правду')
# 	self.tts.runAndWait()
