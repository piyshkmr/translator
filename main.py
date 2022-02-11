
from PyQt5.QtWidgets import QApplication, QComboBox, QGridLayout, QLabel, QPushButton, QTextEdit, QWidget
from googletrans import LANGUAGES, Translator
from PyQt5.QtGui import QFont


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.translator = Translator()

        self.setWindowTitle("Translator")

        self.setMinimumSize(850, 500)

        self.setFont(QFont("Helvetica", 9, 400))

        # layout
        self.setLayout(QGridLayout())

        # label
        self.layout().addWidget(QLabel("From"), 0, 0)

        # from language text area
        self.fromLanguage = QTextEdit()
        self.fromLanguage.setFontPointSize(12.0)
        self.layout().addWidget(self.fromLanguage, 1, 0)

        # from languages combobox
        self.fromLanguageList = QComboBox()
        # adding language to combobox
        self.setLanguage(self.fromLanguageList)
        # setting default language english
        self.fromLanguageList.setCurrentIndex(21)
        self.layout().addWidget(self.fromLanguageList, 2, 0)

        # label
        self.layout().addWidget(QLabel("To"), 0, 1)

        # to language text area
        self.toLanguage = QTextEdit()
        self.toLanguage.setFontPointSize(12.0)
        self.layout().addWidget(self.toLanguage, 1, 1)

        # from languages combobox
        self.toLanguageList = QComboBox()
        # adding language to combobox
        self.setLanguage(self.toLanguageList)
        # setting default language hindi
        self.toLanguageList.setCurrentIndex(38)
        self.layout().addWidget(self.toLanguageList, 2, 1)

        # button

        self.translateBtn = QPushButton("Translate")
        self.layout().addWidget(self.translateBtn, 3, 0, 1, 2)
        self.translateBtn.clicked.connect(self.translateText)

        self.show()

    def translateText(self):
        fromText = self.fromLanguage.toPlainText()
        fromLanguage = self.fromLanguageList.currentData()
        toLanguage = self.toLanguageList.currentData()

        # translating
        result = self.translator.translate(
            fromText, dest=toLanguage, src=fromLanguage)

        # setting text
        self.toLanguage.setText(result.text)

    # addd languages to combobox

    def setLanguage(self, comboBox):
        for key, value in LANGUAGES.items():
            comboBox.addItem(value, key)


app = QApplication([])
window = MainWindow()
app.exec_()
