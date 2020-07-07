import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
from time import sleep# Imports sleep (aka wait or pause) into the program
import pygame


GPIO.setmode(GPIO.BOARD)# Sets the pin numbering system to use the physical layout


win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Berrybot")
counter = 9
# Set up pin 23 for PWM
GPIO.setup(16,GPIO.OUT)  # Sets up pin 23 to an output (instead of an input)
p = GPIO.PWM(16, 40)     # Sets up pin 23 as a PWM pin
p.start(0)               # Starts running PWM on the pin and sets it to 0

run = True
while run:
    
    #pygame.time.delay(100)
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            counter = counter-0.2
            p.ChangeDutyCycle(counter)     # (1-12)Changes the pulse width to 3 (so moves the servo)
            #sleep(0.1)
        if keys[pygame.K_LEFT]:
            counter = counter+0.2
            p.ChangeDutyCycle(counter)     # (1-12)Changes the pulse width to 3 (so moves the servo)
            #sleep(0.1)
        if keys[pygame.K_y]:
            run = False

        GPIO.setwarnings(False) 
# Move the servo back and forth
p.ChangeDutyCycle(counter)     # (1-12)Changes the pulse width to 3 (so moves the servo)
#sleep(1)                 # Wait 1 second(minimum 0.4 for 180 turn)
#p.ChangeDutyCycle(12)    # Changes the pulse width to 12 (so moves the servo)
#sleep(0.2)
#p.ChangeDutyCycle(7)    # Changes the pulse width to 12 (so moves the servo)
#sleep(0.2)

# Clean up everything
p.stop()                 # At the end of the program, stop the PWM
GPIO.cleanup()  
