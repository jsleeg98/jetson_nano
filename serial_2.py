from serial import Serial
import time

arduino = Serial('/dev/ttyACM0', 115200, timeout = 5)
# arduino = Serial(
# port = '/dev/ttyACM0',
# baudrate = 115200,
# bytesize = Serial.EIGHTBITS,
# parity = Serial.PARITY_NONE,
# stopbit = Serial.STOPBITS_ONE,
# timeout = 5,
# xonoff = False,
# rtscts = False,
# dsrdir = False,
# writeTimeout = 2
# )

while True:
    try:
        a = input()
        arduino.write(a.encode())
        data = arduino.readline()
        if data:
            print(data)
            result = data.decode('utf-8')
            ther = result[14:18]
            print(ther)
        time.sleep(1)
    except Exception as e:
        print(e)
        arduino.close()

