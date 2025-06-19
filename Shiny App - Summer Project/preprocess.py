import pandas as pd

# Load the dataset
try:
    df = pd.read_csv("dataset.csv")
    print(" Dataset loaded successfully!\n")
except FileNotFoundError:
    print(" Error: 'dataset.csv' not found in the current folder.")
    exit()

# Preview the first 5 rows
print(" First 5 rows:")
print(df.head(), "\n")

# Show basic structure
print(" Data Types and Non-Null Counts:")
print(df.info(), "\n")

# Rename columns for convenience
df.columns = [col.strip().lower().replace("-", "_") for col in df.columns]

# Convert date columns to datetime
df["scheduledday"] = pd.to_datetime(df["scheduledday"])
df["appointmentday"] = pd.to_datetime(df["appointmentday"])

# Create derived features
df["appointment_weekday"] = df["appointmentday"].dt.day_name()
df["wait_days"] = (df["appointmentday"] - df["scheduledday"]).dt.days

# Convert target to binary (Yes → 1, No → 0)
df["no_show"] = df["no_show"].map({"Yes": 1, "No": 0})

# Remove duplicate rows
before = df.shape[0]
df.drop_duplicates(inplace=True)
after = df.shape[0]
print(f" Removed {before - after} duplicate rows.\n")

# Check for missing values
print(" Missing values per column:")
print(df.isnull().sum(), "\n")

# Save cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)
print(" Cleaned dataset saved as 'cleaned_dataset.csv'. All columns retained.")
