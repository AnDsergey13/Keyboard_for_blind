import sys
from PyQt5.QtWidgets import (
		QApplication, QWidget, QLabel, QPushButton
	)
from PyQt5.QtCore import pyqtSlot, QRect, QCoreApplication

import pyttsx3

key_text = {}

class KeyBoard(QWidget):
	def __init__(self, title=" "):
		super().__init__()

		tts = pyttsx3.init()
		rate = tts.getProperty('rate') #Скорость произношения
		tts.setProperty('rate', rate-65)
		volume = tts.getProperty('volume') #Громкость голоса
		tts.setProperty('volume', volume+0.9)
		voices = tts.getProperty('voices')
		# Задать голос по умолчанию
		tts.setProperty('voice', 'ru') 
		# Попробовать установить предпочтительный голос
		for voice in voices:
			if voice.name == 'Anna':
				tts.setProperty('voice', voice.id)

		self.title = title
		self.left = 500
		self.top = 300
		self.width = 600
		self.height = 400
		self.tts = tts


		self.setWindowTitle(self.title)
		# self.setGeometry(self.left, self.top, self.width, self.height)
		## use above line or below
		self.resize(self.width, self.height)
		self.move(self.left, self.top)

		self.centralwidget = QWidget(self)
		self.create_button(0, 0, 60, 60, "Esc")
		#self.widget()

	def create_button(self, x, y, width, height, text="Empty"):
		self.pushButton = QPushButton(self.centralwidget)
		self.pushButton.setGeometry(QRect(x, y, width, height))
		self.pushButton.setText(text)

		
	# def widget(self):
	# 	# window setup
	# 	self.setWindowTitle(self.title)
	# 	# self.setGeometry(self.left, self.top, self.width, self.height)
	# 	## use above line or below
	# 	self.resize(self.width, self.height)
	# 	self.move(self.left, self.top)

	# 	self.centralwidget = QWidget(self)
	# 	#self.centralwidget.setObjectName(u"centralwidget")
	# 	self.pushButton = QPushButton(self.centralwidget)
	# 	#self.pushButton.setObjectName(u"pushButton")
	# 	self.pushButton.setGeometry(QRect(0, 0, 60, 60))
	# 	self.pushButton.setText("Esc")

	# 	self.pushButton_2 = QPushButton(self.centralwidget)
	# 	self.pushButton_2.setGeometry(QRect(0, 60, 80, 60))
	# 	self.pushButton_2.setText("ё")

	# 	# add button
	# 	# self.btn1 = QPushButton(self, text="В")
	# 	# self.btn1.move(5, 95)
	# 	# self.btn1.clicked.connect(self.button_A)


	# 	# self.btn2 = QPushButton(self, text="А (Арбуз)")
	# 	# self.btn2.move(5, 35)
	# 	# self.btn2.pressed.connect(self.button_B)

	# 	self.show()


	@pyqtSlot()
	def button_A(self):
		self.tts.say('Иван васильевич')
		self.tts.runAndWait()

	@pyqtSlot()
	def button_B(self):
		self.tts.say('Говорит правду')
		self.tts.runAndWait()


def main():
	app = QApplication(sys.argv)
	key = KeyBoard(title="Клавиатура")
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()