# Temperature Conversion Tool using Global Variables
# This script converts temperatures between Celsius and Fahrenheit.

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5



# conversion functions
def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius


def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit


def main():
    try:
        # User input for temperature conversion
        temp_f = float(input("Enter temperature in Fahrenheit: "))
        unit = input("Convert to (C)elsius or (F)ahrenheit? (C/F): ").strip().upper()

        if unit == "C":
            temp_c = convert_to_celsius(temp_f)
            print(f"{temp_f}°F is equal to {temp_c:.2f}°C")

        elif unit == "F":
            temp_c = float(input("Enter temperature in Celsius: "))
            temp_f = convert_to_fahrenheit(temp_c)
            print(f"{temp_c}°C is equal to {temp_f:.2f}°F")

        else:
            print("Invalid choice. Please enter 'C' or 'F'.")

    except ValueError:
        # Handle invalid numeric input
        print("Invalid input. Please enter a numeric value.")
if __name__ == "__main__":
    main()