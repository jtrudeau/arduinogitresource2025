#!/usr/bin/env python3
"""
Arduino Data Logger Analysis Script

This script analyzes distance data collected by an Arduino ultrasonic sensor datalogger.
It reads from a CSV file and generates visualizations and statistics.

Usage:
    python analyze_data.py <csv_file_path>

Example:
    python analyze_data.py DISTANCE.CSV
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

def load_data(file_path):
    """Load data from CSV file and return as pandas DataFrame."""
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        sys.exit(1)

def display_basic_stats(data):
    """Calculate and display basic statistics."""
    print("\n===== Basic Statistics =====")
    
    stats = data.describe()
    print(stats)
    
    print("\n===== Additional Metrics =====")
    
    # Calculate additional metrics
    distance_data = data['Distance(cm)']
    
    print(f"Range: {distance_data.max() - distance_data.min():.2f} cm")
    
    # Calculate stability (standard deviation as percentage of mean)
    stability = (distance_data.std() / distance_data.mean()) * 100
    print(f"Stability (lower is better): {stability:.2f}%")
    
    # Count rapid changes (more than 5cm between consecutive readings)
    if len(distance_data) > 1:
        changes = abs(distance_data.diff())
        rapid_changes = sum(changes > 5)
        print(f"Rapid changes (>5cm): {rapid_changes}")

def plot_distance_vs_time(data, output_dir="./"):
    """Create a plot of distance vs time."""
    plt.figure(figsize=(10, 6))
    
    # Convert time from milliseconds to seconds for better readability
    time_sec = data['Time(ms)'] / 1000
    
    plt.plot(time_sec, data['Distance(cm)'], 'b-')
    plt.title('Distance Measurements Over Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Distance (cm)')
    plt.grid(True)
    
    # Add horizontal lines for mean and boundaries (mean ±1 std)
    mean_distance = data['Distance(cm)'].mean()
    std_distance = data['Distance(cm)'].std()
    
    plt.axhline(y=mean_distance, color='r', linestyle='-', alpha=0.3, label=f'Mean: {mean_distance:.2f} cm')
    plt.axhline(y=mean_distance + std_distance, color='g', linestyle='--', alpha=0.3, label=f'Mean + 1σ: {mean_distance + std_distance:.2f} cm')
    plt.axhline(y=mean_distance - std_distance, color='g', linestyle='--', alpha=0.3, label=f'Mean - 1σ: {mean_distance - std_distance:.2f} cm')
    
    plt.legend()
    
    # Save the figure
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f"{output_dir}distance_plot_{timestamp}.png"
    plt.savefig(output_path)
    print(f"Plot saved as {output_path}")
    
    plt.show()

def create_smoothed_data_plot(data, window_size=5, output_dir="./"):
    """Create a plot comparing raw and smoothed data."""
    # Create a smoothed version using moving average
    data['Smoothed_Distance'] = data['Distance(cm)'].rolling(window=window_size).mean()
    
    plt.figure(figsize=(10, 6))
    
    # Convert time from milliseconds to seconds for better readability
    time_sec = data['Time(ms)'] / 1000
    
    plt.plot(time_sec, data['Distance(cm)'], 'b-', alpha=0.5, label='Raw Data')
    plt.plot(time_sec, data['Smoothed_Distance'], 'r-', label=f'Smoothed Data ({window_size}-point moving average)')
    
    plt.title('Raw vs Smoothed Distance Measurements')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Distance (cm)')
    plt.legend()
    plt.grid(True)
    
    # Save the figure
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f"{output_dir}smoothed_data_{timestamp}.png"
    plt.savefig(output_path)
    print(f"Smoothed data plot saved as {output_path}")
    
    plt.show()

def analyze_movement(data, output_dir="./"):
    """Analyze movement patterns based on rate of change."""
    # Calculate speed (rate of change of distance)
    # Convert milliseconds to seconds for time difference
    data['Speed_cm_s'] = data['Distance(cm)'].diff() / (data['Time(ms)'].diff() / 1000)
    
    # Replace infinities and NaN with 0
    data['Speed_cm_s'] = data['Speed_cm_s'].replace([np.inf, -np.inf], np.nan)
    data['Speed_cm_s'] = data['Speed_cm_s'].fillna(0)
    
    # Filter out extreme values that are likely noise
    speed_threshold = 100  # cm/s
    filtered_speed = data.copy()
    filtered_speed.loc[abs(filtered_speed['Speed_cm_s']) > speed_threshold, 'Speed_cm_s'] = np.nan
    
    plt.figure(figsize=(10, 6))
    
    # Plot speed over time
    time_sec = data['Time(ms)'] / 1000
    plt.plot(time_sec, filtered_speed['Speed_cm_s'], 'g-')
    plt.title('Movement Speed Over Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Speed (cm/s)')
    plt.grid(True)
    
    # Mark regions of significant movement
    significant_speed = 10  # cm/s
    movement_periods = abs(filtered_speed['Speed_cm_s']) > significant_speed
    
    if movement_periods.any():
        movement_regions = []
        in_movement = False
        start_idx = 0
        
        # Find continuous periods of movement
        for i, is_moving in enumerate(movement_periods):
            if is_moving and not in_movement:
                in_movement = True
                start_idx = i
            elif not is_moving and in_movement:
                in_movement = False
                movement_regions.append((start_idx, i))
        
        # If we end while still in a movement period
        if in_movement:
            movement_regions.append((start_idx, len(movement_periods)-1))
        
        # Shade the movement regions
        for start, end in movement_regions:
            plt.axvspan(time_sec[start], time_sec[end], alpha=0.2, color='red')
            
        print(f"\nDetected {len(movement_regions)} periods of significant movement")
    
    # Save the figure
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f"{output_dir}movement_analysis_{timestamp}.png"
    plt.savefig(output_path)
    print(f"Movement analysis plot saved as {output_path}")
    
    plt.show()

def main():
    """Main function to run the analysis."""
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <csv_file_path>")
        sys.exit(1)
        
    file_path = sys.argv[1]
    
    print(f"Analyzing data from: {file_path}")
    data = load_data(file_path)
    
    # Display the first few rows
    print("\n===== Data Preview =====")
    print(data.head())
    
    # Display basic statistics
    display_basic_stats(data)
    
    # Create plots
    plot_distance_vs_time(data)
    create_smoothed_data_plot(data)
    analyze_movement(data)
    
    print("\nAnalysis complete!")

if __name__ == "__main__":
    main() 