from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
import sys
import scanner
import requests


class KioskApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('탁구장 키오스크')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()
        self.label = QLabel("QR 코드 또는 RFID 태그를 스캔하세요")
        layout.addWidget(self.label)

        self.scan_button = QPushButton("스캔 시작")
        self.scan_button.clicked.connect(self.scan_qr_rfid)
        layout.addWidget(self.scan_button)

        self.setLayout(layout)

    def scan_qr_rfid(self):
        qr_code = scanner.scan_qr()
        response = requests.post(
            "http://localhost:8000/check_access", json={"qr_code": qr_code})
        result = response.json()

        if result.get("status") == "approved":
            self.label.setText("입장 승인 ✅")
        else:
            self.label.setText("입장 거부 ❌")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    kiosk = KioskApp()
    kiosk.show()
    sys.exit(app.exec_())
