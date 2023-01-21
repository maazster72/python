"""
This program take a temperature in degress Celsius as an input and displays the conversion in Farenheit
"""

def getTempInCelcius():
    usr_input = float(input("Please enter a temperature in degrees Celcius: "))
    return usr_input

def calcFromCelciusToFarenheit(temp):
    res = (temp * 1.8) + 32
    return res


def main():
    temp_cel = getTempInCelcius()
    temp_far = calcFromCelciusToFarenheit(temp_cel)

    conversion_str = str(temp_cel) + " degrees Celcius = " + str(temp_far) + "F"

    print(conversion_str)

main()




