from machine import I2C,Pin
from lsm303a import LSM303
from time import sleep
from math import atan2,pi

# I2C bus on ESP8266
# i2c = I2C(scl=Pin(5),sda=Pin(4))
# I2C bus on Raspberry Pi Pico
i2c=I2C(0)

compass = LSM303(i2c)
loop=True
while loop:

    # x,y,z=compass.raw_magnetometer()
    x,y,z=compass.magnetometer
    print(x,y,z)
    heading=(atan2(y,x)*180)/pi
    if heading < 0:
        heading=360+heading
    print("Heading: %s" % heading)
    sleep(.500)
