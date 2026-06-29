# ============================================
# SESSION 06 - NumPy (Numerical Python)
# ============================================

import numpy as np


# --- Concept 1: Creating Arrays ---

# Python list
my_list = [1, 2, 3, 4, 5]
print(my_list)

# Convert to NumPy array
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

# 2D array (matrix / table)
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)
print(matrix.shape)     # (2, 3) → 2 rows, 3 columns


# --- Concept 2: Array Operations (Vectorisation) ---

arr = np.array([10, 20, 30, 40, 50])

# Math on the whole array at once — no loop needed
print(arr + 5)      # [15 25 35 45 55]
print(arr * 2)      # [20 40 60 80 100]
print(arr / 10)     # [1. 2. 3. 4. 5.]
print(arr - 5)      # [5 15 25 35 45]

# Real world — normalising sensor data (MinMaxScaler logic)
sensor = np.array([100, 200, 300, 400, 500])
normalised = (sensor - sensor.min()) / (sensor.max() - sensor.min())
print(normalised)   # [0.   0.25 0.5  0.75 1.  ]


# --- Concept 3: Array Indexing & Slicing ---

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])

# Indexing
print(arr[0])       # 10  — first element
print(arr[-1])      # 80  — last element

# Slicing [start:end] (end not included)
print(arr[0:3])     # [10 20 30]
print(arr[2:5])     # [30 40 50]
print(arr[:4])      # [10 20 30 40]
print(arr[4:])      # [50 60 70 80]

# Step slicing [start:end:step]
print(arr[::2])     # [10 30 50 70]

# Boolean indexing — most powerful NumPy feature
print(arr[arr > 40])    # [50 60 70 80]

# Real world — find critical engines
rul_values = np.array([120, 30, 95, 15, 200, 45])
critical = rul_values[rul_values < 50]
print(critical)         # [30 15 45]
print(len(critical))    # 3


# --- Concept 4: Array Statistics ---

sensor = np.array([120, 340, 180, 520, 90, 410, 250])

print(sensor.sum())             # total
print(sensor.mean())            # average
print(sensor.max())             # highest
print(sensor.min())             # lowest
print(sensor.std())             # standard deviation
print(sensor.argmax())          # index of max value
print(sensor.argmin())          # index of min value
print(round(sensor.mean(), 2))  # rounded average

# Real world — sensor dropping logic (zero variance)
sensor_std = np.array([0.0, 5.2, 0.0, 8.1, 0.0, 3.4])
useless_sensors = np.where(sensor_std == 0)
print(useless_sensors)          # positions of zero-variance sensors


# --- Concept 5: Reshaping & 2D Array Operations ---

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(arr.shape)        # (12,)

reshaped = arr.reshape(3, 4)
print(reshaped)
print(reshaped.shape)   # (3, 4)

# 2D array operations
data = np.array([[100, 200, 300],
                 [400, 500, 600],
                 [700, 800, 900]])

print(data.mean())          # mean of entire array
print(data.mean(axis=0))    # mean of each column [400. 500. 600.]
print(data.mean(axis=1))    # mean of each row    [200. 500. 800.]


# ============================================
# SESSION 06 - TASKS
# ============================================

# --- Task 1: Sensor Analysis ---
readings = np.array([120, 340, 180, 520, 90, 410, 250, 600, 75, 430])

# 1. Stats
print(f"Mean: {round(readings.mean(), 2)}")
print(f"Max: {readings.max()}")
print(f"Min: {readings.min()}")

# 2. Readings above the mean
above_mean = readings[readings > readings.mean()]
print(f"Above mean: {above_mean}")

# 3. Count above mean
print(f"Count above mean: {len(above_mean)}")

# 4. Critical readings below 100
critical = readings[readings < 100]
print(f"Critical readings: {critical}")


# --- Task 2: RUL Predictions ---
rul = np.array([130, 45, 200, 30, 95, 180, 15, 250, 60, 110, 25, 175])

# 1. Cap at 125
capped = np.minimum(rul, 125)
print(f"Capped: {capped}")

# 2. Critical engines below 50
critical = capped[capped < 50]
print(f"Critical engines: {critical}")

# 3. Count critical
print(f"Total critical: {len(critical)}")

# 4. Reshape to 3 rows x 4 columns
reshaped = capped.reshape(3, 4)
print(reshaped)
print(reshaped.shape)
