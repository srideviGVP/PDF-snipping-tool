from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog, QVBoxLayout, QPushButton, QWidget
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import sys
from PIL import Image

class ImageViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.image_path = None
        self.original_image = None
        self.cropped_image = None

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Image Cropper')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()
        self.lbl_image = QLabel(self)
        self.lbl_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.lbl_image)

        btn_open = QPushButton('Open Image', self)
        btn_open.clicked.connect(self.open_image)
        layout.addWidget(btn_open)

        btn_crop = QPushButton('Crop Image', self)
        btn_crop.clicked.connect(self.crop_image)
        layout.addWidget(btn_crop)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_image(self):
        filepath, _ = QFileDialog.getOpenFileName(self, 'Open file', '', 'Image files (*.jpg *.png *.jpeg)')
        if filepath:
            self.image_path = filepath
            self.original_image = Image.open(self.image_path)
            pixmap = QPixmap(self.image_path)
            self.lbl_image.setPixmap(pixmap.scaled(self.lbl_image.width(), self.lbl_image.height(), Qt.AspectRatioMode.KeepAspectRatio))

    def crop_image(self):
        if self.original_image:
            # Define crop coordinates (this can be enhanced to use interactive selection)
            left, top, right, bottom = 100, 100, 300, 300
            self.cropped_image = self.original_image.crop((left, top, right, bottom))
            self.cropped_image.save("cropped_image.jpg")
            pixmap = QPixmap("cropped_image.jpg")
            self.lbl_image.setPixmap(pixmap.scaled(self.lbl_image.width(), self.lbl_image.height(), Qt.AspectRatioMode.KeepAspectRatio))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageViewer()
    ex.show()
    sys.exit(app.exec())
