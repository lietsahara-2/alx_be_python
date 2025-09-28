global FAHRENHEIT_TO_CELSIUS_FACTOR
global CELSIUS_TO_FAHRENHEIT_FACTOR

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temp = input("Enter the temperature to convert: ")
#try:
 #   temp = float(temp)
#except ValueError:
#    print("Invalid temperature. Please enter a numeric value.")   
#    exit() 

if temp == float:
    temp = float(temp)
elif temp == int:
    temp = int(temp)
else:
    print("Invalid temperature. Please enter a numeric value.")   
    exit()
    

scale = str(input("Is this temperature in Celsius or Fahrenheit? (C/F): "))

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {celsius}°C")
   

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius}°C is {fahrenheit}°F")
    


def main():
    if scale.upper() == "C":
        convert_to_fahrenheit(temp)
    elif scale.upper() == "F":
        convert_to_celsius(temp)
    else:
        print("Invalid scale. Please enter 'C' for Celsius or 'F' for Fahrenheit.")


if __name__ == "__main__":
     if type(temp) == int or float:
        main()
     else:
        print("Invalid temperature. Please enter a numeric value.")