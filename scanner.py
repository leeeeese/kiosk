import cv2
from pyzbar.pyzbar import decode
import serial

# QR 코드 스캔 함수


def scan_qr():
    cap = cv2.VideoCapture(0)
    while True:
        _, frame = cap.read()
        decoded_objects = decode(frame)
        for obj in decoded_objects:
            qr_data = obj.data.decode("utf-8")
            cap.release()
            return qr_data
        cv2.imshow("QR Scanner", frame)
        if cv2.waitKey(1) == 27:  # ESC 키로 종료
            break
    cap.release()
    cv2.destroyAllWindows()
    return None

# RFID 태그 읽기 함수


def read_rfid():
    ser = serial.Serial('/dev/ttyUSB0', 9600)
    rfid_tag = ser.readline().decode().strip()
    return rfid_tag
