def show_menu():
    print("\nUnit Converter")
    print("1. Length (meters <-> feet, kilometers <-> miles)")
    print("2. Weight (kilograms <-> pounds)")
    print("3. Temperature (Celsius <-> Fahrenheit)")
    print("4. Exit")

def main():
    while True:
        show_menu()
        choice = input("Select an option (1-4): ")

        if choice == "1":
             print("Length conversion selected.")
        elif choice =="2":
             print("Weight conversion selected.")
        elif choice == "3":
            print("Temperature conversion selected.")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 4.")

    if __name__ == "_main_":
        main()
