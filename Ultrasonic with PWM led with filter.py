from DIYables_MicroPython_Ultrasonic_Sensor import UltrasonicSensor
from machine import Pin, PWM, time_pulse_us
import time

sensor = UltrasonicSensor(trig_pin=1, echo_pin=0)
sensor.enable_filter(num_samples=10)  # Enable filtering and set number of samples to 20

LED = PWM(Pin(12))      

LED.freq(1000)


while True:
    sensor.loop()
    distance = sensor.get_distance()
    if distance is not None:
        print("Distance= ", distance, "cm")
        
        if distance < 30:
            duty_cycle = int((1 - (distance / 30)) * 65535)  # Scale pwm from 0 to 65535
            LED.duty_u16(duty_cycle)
        else:
            LED.duty_u16(0)
    
    time.sleep(0.1)