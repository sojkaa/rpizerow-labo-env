from gpiozero import LED, Buzzer
from signal import pause

buzzer = Buzzer(22)
led_r = LED(19)
led_g = LED(26)
led_b = LED(13)

def toggle_led(color):
  """LED"""
  if color == 'r':
    led_r.toggle()
  elif color == 'g':
    led_g.toggle()
  elif color == 'b':
    led_b.toggle()

while True:
  comando = input("Ingrese lo que quiere activar: buzzer o colores: ").lower()

  if comando == "buzzer":
    opcion = input("Ingrese opcion: on u off: ").lower()
    if opcion == "on":
      buzzer.on()
    elif opcion == "off":
      buzzer.off()

  elif comando == "colores":
    opcion = input("Ingrese opcion: r(rojo), g(green) or b(blue): ").lower()
    toggle_led(opcion)

pause()
