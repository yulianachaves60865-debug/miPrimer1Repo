import RPi.GPIO as GPIO


PIN_BOTON = 3
PIN_LED = 7

estadoBoton = False


GPIo.setmode(GPIO:BOARD)
GPIO.setwarnings(False)
GPIO.setup(PIN_BOTON,GPIO.IN)
GPIO:setup(PIN_LED, GPIO.OUT)


while True
	estadoBoton = GPIO.input(PIN_BOTON)
	
	if estadoBoton == True:
	     GPIO.output(PIN_LED, True)
	print("PRESIONADO")
	else:
		GPIO.output(PIN_LED, False)
