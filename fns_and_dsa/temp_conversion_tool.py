FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius():
    result = (temp - 32 ) * FAHRENHEIT_TO_CELSIUS_FACTOR 
    
    print(f"{temp}°F is {result}°C")
    
def convert_to_fahrenheit():
    result = (temp * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    
    print(f"{temp}°C is {result}°F")
    
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

try:
    temp = float(input("Enter the temperature to convert: "))

    if unit == "C":
        convert_to_fahrenheit()
    elif unit == "F":
        convert_to_celsius()
    else:
        print("Invalid unit. Please enter C or F.")

except ValueError:
    print("Invalid temperature. Please enter a numeric value.")







































