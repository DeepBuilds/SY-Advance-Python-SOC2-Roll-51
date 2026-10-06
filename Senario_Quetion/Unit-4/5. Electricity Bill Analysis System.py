import numpy as np
import pandas as pd

# Create a NumPy array of electricity bills
bills = np.array([1800, 2500, 3200, 4500, 2900, 5100, 2750, 3600])

# Calculate statistics
mean_bill = np.mean(bills)
median_bill = np.median(bills)
maximum_bill = np.max(bills)
minimum_bill = np.min(bills)

print("--- Electricity Bill Analysis ---")
print("Bills:", bills)
print("Mean Bill: ₹", mean_bill)
print("Median Bill: ₹", median_bill)
print("Maximum Bill: ₹", maximum_bill)
print("Minimum Bill: ₹", minimum_bill)

# Create a Pandas DataFrame
df = pd.DataFrame({
    "Consumer ID": ["C101", "C102", "C103", "C104", "C105", "C106", "C107", "C108"],
    "Bill Amount": bills
})

print("\n--- Consumer DataFrame ---")
print(df)

# Display consumers whose bill exceeds ₹3000
high_bills = df[df["Bill Amount"] > 3000]

print("\n--- Consumers with Bill Above ₹3000 ---")
print(high_bills)


# Sample Output:
# --- Electricity Bill Analysis ---
# Bills: [1800 2500 3200 4500 2900 5100 2750 3600]
# Mean Bill: ₹ 3281.25
# Median Bill: ₹ 3050.0
# Maximum Bill: ₹ 5100
# Minimum Bill: ₹ 1800
#
# --- Consumer DataFrame ---
#   Consumer ID  Bill Amount
# 0        C101         1800
# 1        C102         2500
# 2        C103         3200
# 3        C104         4500
# 4        C105         2900
# 5        C106         5100
# 6        C107         2750
# 7        C108         3600
#
# --- Consumers with Bill Above ₹3000 ---
#   Consumer ID  Bill Amount
# 2        C103         3200
# 3        C104         4500
# 5        C106         5100
# 7        C108         3600
