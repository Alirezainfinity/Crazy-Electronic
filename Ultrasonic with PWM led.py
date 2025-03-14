from machine import Pin, PWM, time_pulse_us
import time

TRIG = Pin(1, Pin.OUT)  
ECHO = Pin(0, Pin.IN)   
LED = PWM(Pin(12))      

LED.freq(1000)

def measure_distance():
    TRIG.low()
    time.sleep_us(2)
    TRIG.high()
    time.sleep_us(10)
    TRIG.low()
    
    pulse_duration = time_pulse_us(ECHO, 1, 30000)
    if pulse_duration < 0:
        return None  
    
    distance = (pulse_duration * 0.0343) / 2  # Convert to cm
    return distance

while True:
    distance = measure_distance()
    if distance is not None:
        print("Distance= ", distance, "cm")
        
        
        if distance < 30:
            duty_cycle = int((1 - (distance / 30)) * 65535)  # Scale pwm from 0 to 65535
            LED.duty_u16(duty_cycle)
        else:
            LED.duty_u16(0)
    
    time.sleep(0.1)
