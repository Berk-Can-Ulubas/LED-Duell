# author: Berk Can Ulubas
# version: 1.0
# date: 08.05.2025
# brief: A two-player game where pressing your button moves a LED toward your opponent.

import machine
import time

button1 = machine.Pin(28, mode=machine.Pin.IN, pull=machine.Pin.PULL_UP) #button of player 1
button2 = machine.Pin(27, mode=machine.Pin.IN, pull=machine.Pin.PULL_UP) #button of player 2
prev_button1 = 0
prev_button2 = 0

#21 leds
led_pins = [machine.Pin(i, machine.Pin.OUT) for i in range(21)] # leds from gpio 0 to gpio 20
current_led = len(led_pins)//2 #led in the middle

for led in led_pins: #reset all leds
    led.value(0)
led_pins[current_led].value(1) #in the beginning turn on led in the middle
while True:
    #make snapshot of button
    current_button1 = button1.value() ^ 1 #flips value because of normally open button
    current_button2 = button2.value() ^ 1 #flips value because of normally open button
    
    led_pins[current_led].value(0)
    
    if current_button1 == 1 and prev_button1 == 0 and current_button2 == 0 and current_led < len(led_pins) - 1: #if button 1 is pressed current led is turned off and next led is turned on
      current_led += 1
      
      
    elif current_button2 == 1 and prev_button2 == 0 and current_button1 == 0 and current_led > 0: #if button 1 is pressed current led is turned off and previous led is turned on
      current_led -= 1
      
      
    led_pins[current_led].value(1)
    
    prev_button1 = current_button1
    prev_button2 = current_button2
    time.sleep(0.05) 
    
    