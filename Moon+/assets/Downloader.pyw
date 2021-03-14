import sys
from PyQt5.QtWidgets import QApplication, QProgressBar, QWidget, QLineEdit, QPushButton,\
    QVBoxLayout, QHBoxLayout
from PyQt5.QtCore    import QThread, pyqtSignal
import urllib.request    

class Downloader(QThread):
    preprogress = pyqtSignal(float)
    progress = pyqtSignal(float)
    def __init__(self, fileUrl, fileName):
        QThread.__init__(self)
        self._init = False
        self.fileUrl = fileUrl
        self.fileName = fileName

    def run(self):
        urllib.request.urlretrieve(self.fileUrl, self.fileName, self._progress)

    def _progress(self, block_num, block_size, total_size):
        if not self._init:
            self.preprogress.emit(total_size)
            self._init = True

        downloaded = block_num * block_size
        if downloaded < total_size:
            self.progress.emit(downloaded)
        else:
            self.progress.emit(total_size)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.downloader = None

        self.fileUrl = QLineEdit()
        self.loadButton = QPushButton()
        self.loadButton.clicked.connect(self._loadFile)
        hbox = QHBoxLayout()            

        hbox.addWidget(self.fileUrl)
        hbox.addWidget(self.loadButton)

        vbox = QVBoxLayout(self)                                                    
        vbox.addLayout(hbox)                         
        self.bar = QProgressBar() 
        vbox.addWidget(self.bar)

    def _loadFile(self):
        ar = self.fileUrl.text().split('/')
        if len(ar) == 0:
            return
        fileName = f'_{ar[len(ar) -1]}'             

        self._download = Downloader(self.fileUrl.text(), fileName)        
        self._download.preprogress.connect(lambda x: self.bar.setMaximum(x))
        self._download.progress.connect(lambda d: self.bar.setValue(d))
        self._download.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())