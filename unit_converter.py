def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def kilometers_to_miles(km):
    return km * 0.621371

def miles_to_kilometers(miles):
    return miles / 0.621371

def kilograms_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kilograms(pounds):
    return pounds / 2.20462

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def get_valid_float(prompt):
    """Get a valid float input from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def convert_length():
    while True:
        print("\nLength Conversion")
        print("1. Meters to Feet")
        print("2. Feet to Meters")
        print("3. Kilometers to Miles")
        print("4. Miles to Kilometers")
        print("5. Back to main menu")

        choice = input("Select an option (1-5): ")
        if choice == "5":
            break  
        value = get_valid_float("Enter value to convert: ")

        if choice == "1":
            print(f"{value} meters = {meters_to_feet(value):.2f} feet")
        elif choice == "2":
            print(f"{value} feet = {feet_to_meters(value):.2f} meters")
        elif choice == "3":
            print(f"{value} kilometers = {kilometers_to_miles(value):.2f} miles")
        elif choice == "4":
            print(f"{value} miles = {miles_to_kilometers(value):.2f} kilometers")
        else:
            print("Invalid choice. Please select a number from 1 to 5.")

def convert_weight():
    while True:
        print("\nWeight Conversion")
        print("1. Kilograms to Pounds")
        print("2. Pounds to Kilograms")
        print("3. Back to main menu")

        choice = input("Select an option (1-3): ")
        if choice == "3":
            break 

        value = get_valid_float("Enter value to convert: ")

        if choice == "1":
            print(f"{value} kg = {kilograms_to_pounds(value):.2f} pounds")
        elif choice == "2":
            print(f"{value} pounds = {pounds_to_kilograms(value):.2f} kg")
        else:
            print("Invalid choice. Please select a number from 1 to 3.")

def convert_temperature():
    while True:
        print("\nTemperature Conversion")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Back to main menu")

        choice = input("Select an option (1-3): ")
        if choice == "3":
            break 

        value = get_valid_float("Enter value to convert: ")

        if choice == "1":
            print(f"{value}°C = {celsius_to_fahrenheit(value):.2f}°F")
        elif choice == "2":
            print(f"{value}°F = {fahrenheit_to_celsius(value):.2f}°C")
        else:
            print("Invalid choice. Please select a number from 1 to 3.")

def main():
    while True:
        print("\n=== Unit Converter ===")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == "1":
            convert_length()
        elif choice == "2":
            convert_weight()
        elif choice == "3":
            convert_temperature()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 4.")

if __name__ == "__main__":
    main()
