# Arduino Data Logger Project

This is a sample project demonstrating how to create a data logger using an Arduino Uno board.

## About This Project

This project demonstrates a simple ultrasonic sensor-based data logging system that measures distances and stores them on an SD card.

## Features

- Ultrasonic distance sensing
- Data logging to SD card
- Serial monitor output
- CSV file format for easy analysis

## Hardware Requirements

- Arduino Uno board
- HC-SR04 ultrasonic sensor
- SD card module
- SD card (formatted as FAT16 or FAT32)
- Jumper wires
- Breadboard

## Files

- `datalogger.ino`: Main Arduino sketch for the data logger
- `wiring_diagram.png`: Connection diagram for all components
- `data_analysis.md`: Guide for analyzing the collected data
- `README.md`: This documentation file

## Wiring Instructions

### SD Card Module:
- CS → Arduino Pin 10
- MOSI → Arduino Pin 11
- MISO → Arduino Pin 12
- SCK → Arduino Pin 13
- VCC → Arduino 5V
- GND → Arduino GND

### Ultrasonic Sensor (HC-SR04):
- Trigger → Arduino Pin 2
- Echo → Arduino Pin 3
- VCC → Arduino 5V
- GND → Arduino GND

## How to Use

1. Connect the hardware as shown in the wiring diagram
2. Format an SD card as FAT16 or FAT32
3. Insert the SD card into the module
4. Upload the `datalogger.ino` sketch to your Arduino
5. Open the Serial Monitor (9600 baud) to view real-time readings
6. Data will be logged to DISTANCE.CSV on the SD card
7. After collecting data, remove the SD card and analyze the CSV file in a spreadsheet program
8. Follow the instructions in `data_analysis.md` for detailed analysis steps

## Development Notes

- Created as part of the Git learning exercise
- Version 1.0.0
- Based on Dawson College Virtual Lab exercises 