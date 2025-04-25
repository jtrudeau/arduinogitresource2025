/*
  Ultrasonic Sensor Data Logger
  
  This sketch reads distance measurements from an HC-SR04 ultrasonic sensor
  and logs the data to a CSV file on an SD card.
  
  Based on Dawson College Virtual Lab exercise:
  https://englab.dawsoncollege.qc.ca/interns/Intro.html#exercise-3-data-logging-see-demo
*/

#include <SPI.h>
#include <SD.h>

// Ultrasonic sensor pins
const int trigPin = 2;
const int echoPin = 3;

// SD card chip select pin
const int chipSelect = 10;

// Variables for calculating distance
long duration;
float distance;

// File for data logging
File dataFile;
String fileName = "DISTANCE.CSV";

void setup() {
  // Initialize serial communication
  Serial.begin(9600);
  
  // Setup ultrasonic sensor pins
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  
  // Initialize SD card
  Serial.print("Initializing SD card...");
  
  if (!SD.begin(chipSelect)) {
    Serial.println("SD card initialization failed!");
    // Don't proceed if SD card initialization fails
    while (1);
  }
  
  Serial.println("SD card initialized successfully.");
  
  // Create/open data file and write header
  dataFile = SD.open(fileName, FILE_WRITE);
  if (dataFile) {
    // If this is a new file, write the header
    if (dataFile.size() == 0) {
      dataFile.println("Time(ms),Distance(cm)");
    }
    dataFile.close();
    Serial.println("Data file ready.");
  } else {
    Serial.println("Error opening data file!");
  }
}

void loop() {
  // Clear the trigger pin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  
  // Send 10μs pulse to trigger pin
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  // Measure the response from echo pin
  duration = pulseIn(echoPin, HIGH);
  
  // Calculate distance in centimeters
  // Sound travels at 343 meters per second or 0.0343 cm/microsecond
  // Time is round-trip, so divide by 2 to get one-way distance
  distance = duration * 0.0343 / 2;
  
  // Get current time in milliseconds
  unsigned long currentTime = millis();
  
  // Log data to console
  Serial.print("Time: ");
  Serial.print(currentTime);
  Serial.print(" ms, Distance: ");
  Serial.print(distance);
  Serial.println(" cm");
  
  // Open file and log data
  dataFile = SD.open(fileName, FILE_WRITE);
  
  if (dataFile) {
    dataFile.print(currentTime);
    dataFile.print(",");
    dataFile.println(distance);
    dataFile.close();
  } else {
    Serial.println("Error opening data file!");
  }
  
  // Wait before next reading
  delay(500);
}

/* 
 * Advanced modifications to try:
 * 
 * 1. Add a button to start/stop logging:
 *    - Connect a button between Arduino pin 4 and GND
 *    - Add pinMode(4, INPUT_PULLUP) in setup()
 *    - Check digitalRead(4) == LOW to toggle logging
 * 
 * 2. Create new file each time Arduino starts:
 *    - Generate unique filenames based on boot count or sequence
 *    - Store boot count in EEPROM to persist across resets
 *    
 * 3. Optimize power consumption:
 *    - Add sleep mode between readings
 *    - Reduce measurement frequency
 *    - Use lower power SD card operations
 */ 