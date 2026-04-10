
# Welcome message
print(" Welcome to the Interactive Personal Data Collector!")
print("==============================================\n")

# Collect information
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
fav_number = int(input("Please enter your favourite number: "))

print("\nThank you! Processing your data...\n")

# Data processing
current_year = 2026
birth_year = current_year - age

# Type conversion
rounded_height = int(height)  # float to int

# Variable details
print(" Variable Details ")
print(f"Name: {name} (Type: {type(name)}, Memory Address: {id(name)})")
print(f"Age: {age} (Type: {type(age)}, Memory Address: {id(age)})")
print(f"Height: {height} (Type: {type(height)}, Memory Address: {id(height)})")
print(f"Favourite Number: {fav_number} (Type: {type(fav_number)}, Memory Address: {id(fav_number)})")

# Summary
print("\n Summary ")
print(f"Hello {name}, here is your information:")
print(f"Age: {age}")
print(f"Height: {height} meters")
print(f"Favourite Number: {fav_number}")

# Calculation
print(f"\nYour birth year is approximately: {birth_year} (based on your age of {age})")

# Type conversion explanation
print(f"\nYour height rounded down to nearest integer is: {rounded_height}")
print("This value was converted from float to integer using type casting.")

# Exit message

print(" Thank you for using the Personal Data Collector. Goodbye!")
