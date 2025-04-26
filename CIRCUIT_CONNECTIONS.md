# Weather Station Circuit Connections

## Components Required
1. Raspberry Pi
2. DHT11 Temperature & Humidity Sensor
3. HC05 Bluetooth Module
4. Ultrasonic Sensor (HC-SR04)
5. LDR Sensor
6. MCP3008 ADC
7. Jumper Wires
8. Breadboard
9. 10kΩ Resistor (for LDR)
10. 4.7kΩ Resistor (for DHT11)

## Pin Connections

### DHT11 Sensor
```
DHT11 Pin -> Raspberry Pi Pin
VCC      -> 3.3V (Pin 1)
GND      -> GND (Pin 6)
DATA     -> GPIO 4 (Pin 7)
```

### HC05 Bluetooth Module
```
HC05 Pin -> Raspberry Pi Pin
VCC      -> 5V (Pin 2)
GND      -> GND (Pin 6)
TX       -> GPIO 14 (Pin 8)
RX       -> GPIO 15 (Pin 10)
```

### Ultrasonic Sensor (HC-SR04)
```
HC-SR04 Pin -> Raspberry Pi Pin
VCC         -> 5V (Pin 2)
GND         -> GND (Pin 6)
TRIG        -> GPIO 23 (Pin 16)
ECHO        -> GPIO 24 (Pin 18)
```

### LDR Sensor with MCP3008 ADC
```
LDR Pin -> MCP3008 Pin
VCC     -> 3.3V (Pin 1)
GND     -> GND (Pin 6)
OUT     -> CH0 of MCP3008

MCP3008 Pin -> Raspberry Pi Pin
VDD         -> 3.3V (Pin 1)
VREF        -> 3.3V (Pin 1)
AGND        -> GND (Pin 6)
DGND        -> GND (Pin 6)
CLK         -> GPIO 11 (Pin 23)
DOUT        -> GPIO 9 (Pin 21)
DIN         -> GPIO 10 (Pin 19)
CS          -> GPIO 8 (Pin 24)
```

## Power Connections
```
Raspberry Pi Power
5V Pins    -> Pin 2, Pin 4
3.3V Pins  -> Pin 1, Pin 17
GND Pins   -> Pin 6, Pin 9, Pin 14, Pin 20, Pin 25, Pin 30, Pin 34, Pin 39
```

## Important Notes
1. Always double-check voltage levels:
   - DHT11 and MCP3008 require 3.3V
   - HC05 and HC-SR04 can use 5V

2. Use appropriate resistors:
   - 4.7kΩ pull-up resistor for DHT11 data line
   - 10kΩ resistor in series with LDR for voltage divider

3. GPIO Pin Numbers:
   - Use BCM numbering (GPIO.BCM) in code
   - Physical pin numbers are shown in parentheses

4. Safety Precautions:
   - Always power off before making connections
   - Double-check connections before powering on
   - Use appropriate voltage levels for each component
   - Ensure proper grounding

## Troubleshooting
1. If DHT11 is not working:
   - Check 4.7kΩ pull-up resistor
   - Verify 3.3V power supply
   - Check data pin connection

2. If LDR readings are unstable:
   - Check voltage divider circuit
   - Verify MCP3008 connections
   - Ensure proper SPI configuration

3. If HC05 is not connecting:
   - Check TX/RX connections (they should be crossed)
   - Verify baud rate settings
   - Check power supply

4. If Ultrasonic sensor is not working:
   - Check TRIG and ECHO connections
   - Verify 5V power supply
   - Ensure proper timing in code 