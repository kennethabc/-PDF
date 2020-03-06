import sys
from PySide2.QtWidgets import *
from MegerPDF import *

class MyMergePDFApp(QMainWindow):
    def __init__(self):
        super().__init__()


        self.cenWidget = QWidget()
        self.setCentralWidget(self.cenWidget)
        self.resize(800, 600)
        self.setWindowTitle("Merge PDF V0.1")

        self.mLayout = QGridLayout()

        self.inputLabel = QLabel("源PDF路径:")
        self.inputText = QLineEdit()
        self.inputBtn = QPushButton("浏览..")

        self.outputLabel = QLabel("输出文件名")
        self.outputText = QLineEdit()


        self.runBtn = QPushButton("执行")
        self.exitBtn = QPushButton("退出程序")

        self.mLayout.addWidget(self.inputLabel, 0, 0)
        self.mLayout.addWidget(self.inputText, 0, 1)
        self.mLayout.addWidget(self.inputBtn, 0, 2)

        self.mLayout.addWidget(self.outputLabel, 1, 0)
        self.mLayout.addWidget(self.outputText, 1, 1)


        self.mLayout.addWidget(self.runBtn, 2, 0)
        self.mLayout.addWidget(self.exitBtn, 2, 2)

        self.mLayout.setSpacing(10)

        self.cenWidget.setLayout(self.mLayout)

        self.inputBtn.clicked.connect(self.getInputPath)

        self.exitBtn.clicked.connect(self.exitApp)
        self.runBtn.clicked.connect(self.run)

        self.show()


    def getInputPath(self):
        self.inputText.setText(QFileDialog.getExistingDirectory())


    def getOutputPath(self):
        self.outputText.setText(QFileDialog.getExistingDirectory())

    def exitApp(self):
        qApp = QApplication.instance()
        qApp.quit()


    def run(self):
        if self.inputText.text() and self.outputText.text():

            try:
                MergePDFto(self.inputText.text(), self.outputText.text())
            except Exception as e:
                self.showInfo(repr(e))

        else:
            self.showInfo("请先输入路径和pdf名称")
            return

    def showInfo(self, str):
        QMessageBox.information(self, '合并PDF', str)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myMergeApp = MyMergePDFApp()
    sys.exit(app.exec_())