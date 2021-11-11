import Jetson.GPIO as GPIO
import spidev
import time

OBJECT = [0xA0]
SENSOR = [0xA1]

def SPI_COMMAND(ADR, spi):
    Data_Buf = [ADR[0], 0x22, 0x22]
    
    GPIO.output(11, GPIO.LOW) #SCE Enable
    time.sleep(0.000001)

    spi.xfer3(Data_Buf[0])
    time.sleep(0.000001)
    spi.xfer3(Data_Buf[1])
    time.sleep(0.000001)
    spi.xfer3(Data_Buf[2])
    time.sleep(0.000001)

    GPIO.output(11, GPIO.LOW)

    return (Data_Buf[2] * 256 + Data_Buf[1])



def main():
    spi = spidev.SpiDev()

    spi.open(0, 0)
    spi.mode = 3
    spi.max_speed_hz = 1000000

    GPIO.setmode(GPIO.BCM)
    mode = GPIO.getmode()
    GPIO.setwarnings(False)
    GPIO.setup(22, GPIO.OUT)

    GPIO.output(22, GPIO.HIGH) #SCE Enable
    
    # test_1 = SPI_COMMAND(SENSOR, spi)
    # time.sleep(0.000001)
    # test_2 = SPI_COMMAND(OBJECT, spi)

    # Data_Buf_1 = [0xA0, 0x22, 0x22]
    # Data_Buf_2 = [0xA1, 0x22, 0x22]

    # a = spi.xfer(Data_Buf_1)
    # time.sleep(0.000001)
    # b = spi.xfer(Data_Buf_2)

    # print(a)
    # print(b)


    Data_Buf_1 = [0x22]
    
    Data_Buf_2 = [0x22]

    GPIO.output(22, GPIO.LOW) # E를 0
    time.sleep(0.000001) # 10마이크로 대기

    spi.xfer(SENSOR) # sensor 보내기
    time.sleep(0.000001) # 10마이크로 대기

    a = spi.xfer(Data_Buf_1,1) 
    time.sleep(0.000001)

    b = spi.xfer(Data_Buf_2,1)
    time.sleep(0.000001)

    GPIO.output(22, GPIO.HIGH)

    time.sleep(0.000001)

    print(b * 256 + a)

    GPIO.output(22, GPIO.LOW)
    time.sleep(0.000001)

    spi.writebytes(OBJECT)
    time.sleep(0.000001)
   
    a = spi.xfer(Data_Buf_1,1)
    time.sleep(0.000001)

    b = spi.xfer(Data_Buf_2,1)
    time.sleep(0.000001)

    GPIO.output(22, GPIO.HIGH)

    time.sleep(0.000002)
    print(a)
    print(b)




   
    
    



if __name__ == '__main__':
    main()