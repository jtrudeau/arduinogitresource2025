# Analyzing Your Datalogger Results

This guide will help you analyze the data collected by your Arduino ultrasonic sensor datalogger.

## Accessing Your Data

1. Turn off your Arduino
2. Remove the SD card from the module
3. Insert the SD card into your computer using an SD card reader
4. Open the DISTANCE.CSV file

## Analyzing with Spreadsheet Software

### Using Microsoft Excel

1. Open Excel
2. Go to File → Open and navigate to your DISTANCE.CSV file
3. Make sure to select "All Files" in the file type dropdown if you don't see your CSV
4. Excel should automatically recognize the CSV format
5. Select column A (Time) and column B (Distance)
6. Go to Insert → Chart → Scatter
7. Choose "Scatter with smooth lines" to see the trend of distance over time

### Using Google Sheets

1. Open Google Sheets (sheets.google.com)
2. Go to File → Import and upload your DISTANCE.CSV file
3. Select "Replace spreadsheet" and "Detect automatically" for separator type
4. Click "Import data"
5. Select both columns of data
6. Click Insert → Chart
7. In the Chart Editor, select "Scatter chart"

## Analyzing with Python

Python provides powerful tools for data analysis and visualization. Here's how to analyze your data using Python:

### Required Libraries
- pandas: for data manipulation
- matplotlib: for creating charts
- numpy: for numerical operations

### Python Code Example

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file
data = pd.read_csv('DISTANCE.CSV')

# Display the first few rows
print(data.head())

# Basic statistics
print("\nBasic Statistics:")
print(data.describe())

# Calculate the rate of change (speed)
data['speed_cm_s'] = data['Distance(cm)'].diff() / (data['Time(ms)'].diff() / 1000)

# Create a plot
plt.figure(figsize=(10, 6))

# Plot distance over time
plt.subplot(2, 1, 1)
plt.plot(data['Time(ms)'] / 1000, data['Distance(cm)'], 'b-')
plt.title('Distance vs Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Distance (cm)')
plt.grid(True)

# Plot speed over time (filtering out outliers)
plt.subplot(2, 1, 2)
speed_data = data['speed_cm_s'].replace([np.inf, -np.inf], np.nan).dropna()
speed_data = speed_data[abs(speed_data) < 100]  # Filter extreme values
plt.plot(data['Time(ms)'][1:len(speed_data)+1] / 1000, speed_data, 'r-')
plt.title('Speed vs Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Speed (cm/s)')
plt.grid(True)

plt.tight_layout()
plt.savefig('distance_analysis.png')
plt.show()

# Create a moving average to smooth data
window_size = 5
data['distance_smooth'] = data['Distance(cm)'].rolling(window=window_size).mean()

# Plot raw vs smoothed data
plt.figure(figsize=(10, 6))
plt.plot(data['Time(ms)'] / 1000, data['Distance(cm)'], 'b-', alpha=0.5, label='Raw Data')
plt.plot(data['Time(ms)'] / 1000, data['distance_smooth'], 'r-', label='Smoothed Data')
plt.title('Raw vs Smoothed Distance Measurements')
plt.xlabel('Time (seconds)')
plt.ylabel('Distance (cm)')
plt.legend()
plt.grid(True)
plt.savefig('smoothed_data.png')
plt.show()
```

### Using Jupyter Notebook

For interactive analysis, Jupyter Notebook is highly recommended:

1. Install Jupyter: `pip install jupyter`
2. Create a new notebook: `jupyter notebook`
3. Copy the above code into a cell
4. Adjust the file path to your CSV file
5. Run the cell to see immediate results
6. Experiment with different analysis techniques

### Advanced Analysis Ideas

- Detect movement patterns using threshold detection
- Apply Fourier transforms to find patterns in the data
- Use machine learning to classify different types of movements
- Create 3D visualizations if you're logging data from multiple sensors

## Data Analysis Techniques

### Basic Statistics

Calculate these basic statistics to understand your data:
- Minimum distance: `=MIN(B:B)`
- Maximum distance: `=MAX(B:B)`
- Average distance: `=AVERAGE(B:B)`
- Standard deviation: `=STDEV(B:B)`

### Identifying Patterns

1. Look for sudden changes in distance that might indicate movement
2. Calculate the rate of change between measurements:
   - Add a new column with formula: `=(B3-B2)/(A3-A2)*1000`
   - This gives you speed in cm/second
3. Look for periods of stable readings vs. variable readings

### Filtering Data

If your data contains noise or outliers:
1. Create a filtered column using a moving average
2. Formula: `=AVERAGE(B2:B6)` for a 5-point moving average
3. Chart both the raw and filtered data to compare

## Exporting Your Analysis

1. Save your spreadsheet with your analysis
2. Export any charts as images (.png or .jpg)
3. Include these in your project documentation

## Example Scenarios to Test

1. **Static Object**: Place an object at a fixed distance and verify consistent readings
2. **Moving Object**: Move an object slowly toward and away from the sensor
3. **Interfering Objects**: Introduce additional objects in the path to see how they affect readings
4. **Different Materials**: Test different materials to see if they affect sensor accuracy 