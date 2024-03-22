from gpiozero import LED, Button
from signal import pause

led = LED(13)
btn = Button(18)

btn.when_pressed = led.on
btn.when_released = led.off

pause()

