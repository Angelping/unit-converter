import sys

def get_input():
    """Get input unit and value from user."""
    value = float(input("Enter the value to convert: "))
    unit = input("Enter the unit to convert from: ").lower()
    return value, unit

def select_conversion_type(unit):
    """Determine the conversion type based on the input unit."""
    length_units = ['mm', 'cm', 'm', 'km', 'in', 'ft', 'yd', 'mi']
    mass_units = ['mg', 'g', 'kg', 'lb', 'oz']
    temperature_units = ['c', 'f', 'k']

    if unit in length_units:
        return 'length'
    elif unit in mass_units:
        return 'mass'
    elif unit in temperature_units:
        return 'temperature'
    else:
        return None

def convert_length(value, from_unit, to_unit):
    """Convert between length units."""
    # Conversion to meters
    meters = {
        'mm': value / 1000,
        'cm': value / 100,
        'm': value,
        'km': value * 1000,
        'in': value * 0.0254,
        'ft': value * 0.3048,
        'yd': value * 0.9144,
        'mi': value * 1609.344
    }
    
    # Convert to the desired unit
    result = meters[from_unit] / meters[to_unit] * value
    return result

def convert_mass(value, from_unit, to_unit):
    """Convert between mass units."""
    # Conversion to grams
    grams = {
        'mg': value / 1000,
        'g': value,
        'kg': value * 1000,
        'lb': value * 453.592,
        'oz': value * 28.3495
    }
    
    # Convert to the desired unit
    result = grams[from_unit] / grams[to_unit] * value
    return result

def convert_temperature(value, from_unit, to_unit):
    """Convert between temperature units."""
    if from_unit == 'c' and to_unit == 'f':
        return (value * 9/5) + 32
    elif from_unit == 'f' and to_unit == 'c':
        return (value - 32) * 5/9
    elif from_unit == 'c' and to_unit == 'k':
        return value + 273.15
    elif from_unit == 'k' and to_unit == 'c':
        return value - 273.15
    elif from_unit == 'f' and to_unit == 'k':
        return (value - 32) * 5/9 + 273.15
    elif from_unit == 'k' and to_unit == 'f':
        return (value - 273.15) * 9/5 + 32
    else:
        return value

def main():
    print("Welcome to the Unit Converter!")
    
    while True:
        value, from_unit = get_input()
        conversion_type = select_conversion_type(from_unit)
        
        if conversion_type is None:
            print("Invalid unit. Please try again.")
            continue
        
        to_unit = input(f"Enter the unit to convert to ({conversion_type}): ").lower()
        
        if conversion_type == 'length':
            result = convert_length(value, from_unit, to_unit)
        elif conversion_type == 'mass':
            result = convert_mass(value, from_unit, to_unit)
        elif conversion_type == 'temperature':
            result = convert_temperature(value, from_unit, to_unit)
        
        print(f"{value} {from_unit} is equal to {result:.4f} {to_unit}")
        
        if input("Do you want to perform another conversion? (y/n): ").lower() != 'y':
            print("Thank you for using the Unit Converter. Goodbye!")
            break

if __name__ == "__main__":
    main()
