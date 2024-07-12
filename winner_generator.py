from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

#создание главного окна
app = QApplication([])
window = QWidget()
window.setWindowTitle('Определитель победителя')
window.resize(400,200)

#создание кнопки и метки
button = QPushButton('Сгенерировать')
text = QLabel('Нажми, чтобы узнать победителя')
winner = QLabel('?')

#равнение виджетов по вертикали
line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(button, alignment = Qt.AlignCenter)
window.setLayout(line)

def show_winner():
    number = randint(0, 9)
    winner.setText(str(number))
    text.setText('Победитель:')

button.clicked.connect(show_winner)

window.show()
app.exec_()
