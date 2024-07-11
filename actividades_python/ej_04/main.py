import time
import gpiozero
import Adafruit_ADS1x15

# Crear una instancia de ADC
adc = Adafruit_ADS1x15.ADS1115()

# Configuración de los pines GPIO para los LEDs
red_led = gpiozero.PWMLED(17)
blue_led = gpiozero.PWMLED(27)

R_REF = 10000.0  # Resistencia de referencia en ohmios
BETA = 3900.0    # Beta del termistor

GAIN = 1

def read_potentiometer():
    """Lee el valor del potenciómetro y lo escala a un rango de 0 a 30 grados."""
    value = adc.read_adc(0, gain=GAIN)
    temperature_setpoint = value * 30.0 / 32767.0
    return temperature_setpoint

def read_thermistor():
    """Lee el valor del termistor y lo convierte a grados Celsius."""
    value = adc.read_adc(1, gain=GAIN)
    resistance = R_REF * (32767.0 / value - 1.0)
    temperature = 1.0 / (1.0 / 298.15 + (1.0 / BETA) * (resistance / R_REF - 1.0)) - 273.15
    return temperature

def control_leds(temp_setpoint, actual_temp):
    """Controla los LEDs en función de la diferencia entre el setpoint y la temperatura actual."""
    difference = actual_temp - temp_setpoint
    max_difference = 5.0
    duty_cycle = min(abs(difference) / max_difference, 1.0)

    if difference > 0:
        # Temperatura real está por encima del setpoint, encender LED azul
        blue_led.value = duty_cycle
        red_led.value = 0
    else:
        # Temperatura real está por debajo del setpoint, encender LED rojo
        red_led.value = duty_cycle
        blue_led.value = 0

def main():
    """Función principal del programa."""
    while True:
        temp_setpoint = read_potentiometer()
        actual_temp = read_thermistor()
        control_leds(temp_setpoint, actual_temp)
        print(f"Setpoint: {temp_setpoint:.2f}°C, Actual: {actual_temp:.2f}°C")
        time.sleep(1)

if __name__ == "__main__":
    main()
