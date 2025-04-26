import time
import json
import requests
import board
import adafruit_dht
import RPi.GPIO as GPIO
import spidev
import psutil

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Ultrasonic Setup
TRIG = 23
ECHO = 24
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# MCP3008 Setup
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

def kill_gpiod_processes():
    for proc in psutil.process_iter():
        if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
            proc.kill()

def read_adc(channel):
    try:
        if channel < 0 or channel > 7:
            return -1
        r = spi.xfer2([1, (8 + channel) << 4, 0])
        adc_out = ((r[1] & 3) << 8) + r[2]
        return adc_out
    except Exception as e:
        print(f"LDR Error: {str(e)}")
        return 0

def get_distance():
    try:
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        
        pulse_start = time.time()
        timeout = time.time() + 0.1
        
        while GPIO.input(ECHO) == 0 and time.time() < timeout:
            pulse_start = time.time()
        
        if time.time() >= timeout:
            print("Ultrasonic Error: Timeout waiting for echo start")
            return 0
        
        pulse_end = time.time()
        timeout = time.time() + 0.1
        
        while GPIO.input(ECHO) == 1 and time.time() < timeout:
            pulse_end = time.time()
        
        if time.time() >= timeout:
            print("Ultrasonic Error: Timeout waiting for echo end")
            return 0
        
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        return round(distance, 2)
    except Exception as e:
        print(f"Ultrasonic Error: {str(e)}")
        return 0

def read_dht11():
    try:
        # Kill any existing gpiod processes
        kill_gpiod_processes()
        
        # Initialize DHT11 with use_pulseio=False
        dht = adafruit_dht.DHT11(board.D4, use_pulseio=False)
        temperature = dht.temperature
        humidity = dht.humidity
        dht.exit()
        return temperature, humidity
    except RuntimeError as error:
        print(f"DHT11 Error: {error.args[0]}")
        return 25, 50
    except Exception as error:
        print(f"DHT11 Error: {str(error)}")
        return 25, 50

def read_sensors():
    # Read DHT11
    temperature, humidity = read_dht11()
    
    # Read LDR
    ldr_value = read_adc(0)
    
    # Read Ultrasonic
    distance = get_distance()
    
    # Create data dictionary
    data = {
        "temperature": temperature,
        "humidity": humidity,
        "light_level": ldr_value,
        "distance": distance,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    
    return data

def send_data(data):
    try:
        response = requests.post(
            "http://192.168.249.222:5000/api/data",
            json=data,
            timeout=5
        )
        print(f"Data sent successfully: {response.status_code}")
    except Exception as e:
        print(f"Error sending data: {str(e)}")
        with open("sensor_data_backup.json", "a") as f:
            f.write(json.dumps(data) + "\n")

if __name__ == "__main__":
    try:
        while True:
            try:
                sensor_data = read_sensors()
                print(sensor_data)
                send_data(sensor_data)
                time.sleep(5)
            except Exception as e:
                print(f"Error in main loop: {str(e)}")
                time.sleep(5)
                continue
    except KeyboardInterrupt:
        GPIO.cleanup()
        spi.close()