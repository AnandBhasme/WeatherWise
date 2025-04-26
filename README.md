# WeatherWise

A distributed weather station network using Raspberry Pi and various sensors to collect localized weather data from cellular towers.

## Project Structure

```
WeatherWise/
├── Frontend/              # Frontend web application
├── RaspberryPi-codes/     # Raspberry Pi sensor code
├── server/               # Backend server code
│   ├── server.py
│   └── templates/
└── docs/                 # Documentation and presentations
```

## Features

- Real-time weather data collection
- Multiple sensor integration (DHT11, Ultrasonic, LDR)
- Web dashboard for data visualization
- Open data API for machine learning enthusiasts
- Localized weather data collection

## Hardware Requirements

- Raspberry Pi
- DHT11 Temperature & Humidity Sensor
- HC05 Bluetooth Module
- Ultrasonic Sensor
- LDR Sensor
- MCP3008 ADC (for LDR)

## Software Requirements

- Python 3.x
- Flask
- Adafruit_DHT
- RPi.GPIO
- spidev

## Installation

1. Clone the repository:
```bash
git clone https://github.com/AnandBhasme/WeatherWise.git
cd WeatherWise
```

2. Install dependencies:
```bash
# For Raspberry Pi
pip install -r requirements.txt

# For server
cd server
pip install -r requirements.txt
```

3. Configure the sensors:
- Connect sensors as per the wiring diagram
- Update configuration in RaspberryPi-codes/weather_station.py

4. Run the server:
```bash
cd server
python server.py
```

5. Run the weather station:
```bash
cd RaspberryPi-codes
python weather_station.py
```

## API Documentation

The API provides endpoints for:
- Real-time sensor data
- Historical data
- Station information

## Contributing

Contributions are welcome! Please read our contributing guidelines before submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 