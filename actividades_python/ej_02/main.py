from gpiozero import LED
from time import sleep

leds = [
    LED(19),
    LED(13),
    LED(26),
]

blink_patterns = [
    (1, 1),  
    (0.25, 0.25),  
    (0.5, 0.5),
]

while True:
    for i, led in enumerate(leds):
        on_time, off_time = blink_patterns[i]
        led.on()
        sleep(on_time)
        led.off()
        sleep(off_time)
