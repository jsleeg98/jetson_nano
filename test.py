import Jetson.GPIO as GPIO
import time
# GPIO.setmode(GPIO.BCM)
# mode = GPIO.getmode()
# GPIO.setwarnings(False)
# GPIO.setup(4, GPIO.OUT)

# try:
#     while True:
#         GPIO.output(4, GPIO.HIGH)
#         time.sleep(1)
#         GPIO.output(4, GPIO.LOW)
#         time.sleep(1)
# finally:
#     GPIO.cleanup()

input_pin = 18

def print_state(channel):
    print('test')


def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(input_pin, GPIO.IN)

    curr_value = GPIO.HIGH

    try:
        GPIO.add_event_detect(input_pin, GPIO.FALLING, callback = print_state, bouncetime = 10)
        while(1):
            pass
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()