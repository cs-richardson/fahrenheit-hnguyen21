# This code converts Celsius to Fahrenheit. However, if the user inputs a string, fraction or number less than -273ºC, it will not convert the temperature
# In addition, the program will re-prompt them if they want to continue whenever they create an error.
# Made by Ben

x=1
while x==1:
    celsius = input("ºC: ")
    try:
        if float(celsius) >= -273:
            fahrenheit = 9/5*float(celsius)+32
            print(round(fahrenheit,5), "ºF:")
        else:
            print("Not possible.")
    except ValueError:
        print("This isn't a number.")
    prompt=input("Do you want to continue? ")
    if prompt.upper() == "YES" or prompt.upper() == "Y":
        continue
    else:
        break
