import RPi.GPIO as GPIO
import time

DOOR_RELAY_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(DOOR_RELAY_PIN, GPIO.OUT)


def open_door():
    GPIO.output(DOOR_RELAY_PIN, GPIO.HIGH)
    time.sleep(5)  # 5초 동안 문 열림
    GPIO.output(DOOR_RELAY_PIN, GPIO.LOW)


def cleanup():
    GPIO.cleanup()
