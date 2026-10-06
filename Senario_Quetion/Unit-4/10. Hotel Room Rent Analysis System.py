import numpy as np
import pandas as pd

# Create a NumPy array of room rents
rents = np.array([2500, 3500, 4200, 5000, 3000, 4500, 3800, 5500])

# Calculate statistics
mean_rent = np.mean(rents)
median_rent = np.median(rents)
maximum_rent = np.max(rents)
minimum_rent = np.min(rents)

print("--- Hotel Room Rent Analysis ---")
print("Room Rents:", rents)
print("Mean Rent: ₹", mean_rent)
print("Median Rent: ₹", median_rent)
print("Maximum Rent: ₹", maximum_rent)
print("Minimum Rent: ₹", minimum_rent)

# Create a Pandas DataFrame
df = pd.DataFrame({
    "Room Number": ["101", "102", "103", "104", "105", "106", "107", "108"],
    "Room Rent": rents
})

print("\n--- Hotel Room DataFrame ---")
print(df)

# Display rooms having rent greater than ₹4000
high_rent = df[df["Room Rent"] > 4000]

print("\n--- Rooms with Rent Greater Than ₹4000 ---")
print(high_rent)


# Sample Output:
# --- Hotel Room Rent Analysis ---
# Room Rents: [2500 3500 4200 5000 3000 4500 3800 5500]
# Mean Rent: ₹ 4000.0
# Median Rent: ₹ 4000.0
# Maximum Rent: ₹ 5500
# Minimum Rent: ₹ 2500
#
# --- Hotel Room DataFrame ---
#   Room Number  Room Rent
# 0         101       2500
# 1         102       3500
# 2         103       4200
# 3         104       5000
# 4         105       3000
# 5         106       4500
# 6         107       3800
# 7         108       5500
#
# --- Rooms with Rent Greater Than ₹4000 ---
#   Room Number  Room Rent
# 2         103       4200
# 3         104       5000
# 5         106       4500
# 7         108       5500
