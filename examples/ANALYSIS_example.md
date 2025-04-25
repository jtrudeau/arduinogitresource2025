# Ultrasonic Sensor Data Analysis

This document explains how to analyze the data collected from our Arduino ultrasonic sensor data logger using Python.

## Prerequisites

To run the analysis script, you'll need:

1. Python 3.6 or higher
2. The following Python libraries:
   - pandas
   - matplotlib
   - numpy

You can install these libraries using pip:

```bash
pip install pandas matplotlib numpy
```

## Data Format

The Arduino data logger saves data in CSV format with the following columns:
- `Time(ms)`: Time in milliseconds since the Arduino started
- `Distance(cm)`: Distance measured by the ultrasonic sensor in centimeters

## Running the Analysis

1. Connect the SD card to your computer
2. Copy the DISTANCE.CSV file to your computer
3. Run the analysis script:

```bash
python analyze_data.py DISTANCE.CSV
```

## Analysis Output

The script produces several outputs:

### 1. Basic Statistics

The script calculates:
- Mean, median, standard deviation, min, and max of the distance measurements
- Stability (standard deviation as percentage of mean)
- Number of rapid changes (>5cm between consecutive readings)

### 2. Distance vs Time Plot

![Distance Plot](example_images/distance_plot.png)

This plot shows:
- Raw distance measurements over time
- Mean distance (red line)
- ±1 standard deviation range (green dashed lines)

### 3. Smoothed Data Plot

![Smoothed Data](example_images/smoothed_data.png)

This plot compares:
- Raw distance measurements (blue)
- Smoothed measurements using a 5-point moving average (red)

### 4. Movement Analysis

![Movement Analysis](example_images/movement_analysis.png)

This plot shows:
- Speed of movement (rate of change of distance)
- Highlighted regions of significant movement (red shaded areas)

## Interpreting the Results

### Static Object Test

When testing with a static object at 30cm:
- Mean distance: 30.12cm
- Standard deviation: 0.28cm
- Stability: 0.93%
- No periods of significant movement detected

This indicates high reliability for static measurements.

### Moving Object Test

When moving an object toward and away from the sensor:
- Clear movement patterns visible in the speed plot
- 3 distinct periods of movement detected
- Maximum speed detected: 42.6 cm/s

## Modifying the Analysis

You can modify the analysis by changing parameters in the script:

- `window_size` in `create_smoothed_data_plot()`: Controls the smoothing level (default: 5)
- `significant_speed` in `analyze_movement()`: Threshold for detecting movement (default: 10 cm/s)
- `speed_threshold` in `analyze_movement()`: Filter for outlier speeds (default: 100 cm/s)

## Future Improvements

Potential improvements to the analysis:
- Add object classification based on movement patterns
- Implement signal processing to reduce noise further
- Create interactive visualizations with Plotly
- Export analysis to a report format (PDF) 