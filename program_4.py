def temp_conversion(celsius):
    
    fahrenheit = 0.0

    fahrenheit = (9/5)*celsius+32

    return fahrenheit


if __name__ == '__main__':
    celsius = 0.0
    fahrenheit = 0.0
    
    celsius = float(input("Enter a Celsius temperature: "))
    fahrenheit = temp_conversion(celsius)
    
    print ("That is equal to", format(fahrenheit, '.2f'), "degrees Fahrenheit.")

    #Program #4, Donovan Thompson 1/29/25
