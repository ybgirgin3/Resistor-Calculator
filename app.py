#!usr/bin/python3
#<-- coding=utf8 -->
"""
26 December 2018
author: Yusuf Berkay Girgin

"""

main_color_values = {
    "black": 0, "brown": 1, "red": 2, "orange": 3, 
    "yellow": 4, "green": 5, "blue": 6, "purple": 7, "gray": 8, "white": 9
}


multipler_values = {
    "black": 1, "brown": 10, "red": 100, "orange": 1000, 
    "yellow": 10000, "green": 100000, "blue": 1000000, "gold": 0.1, 
    "silver": 0.01
}


def result(color1Key, color2Key, color3Key):
    # making program read the color1 and color2 values like "1"+"1" = "11" in javascript
    invertString = str(color1Key) + str(color2Key)

    # for adding kilo ohm functionality if multipler value is bigger than 1000
    if color3Key > 999 or invertString == 47:
        Kohm = int(sonuc) * int((color3Key/1000))

        # for adding M kilo ohm functionality if the kilo ohm value that mentioned above is bigger than 1000
        if Kohm > 999:
            print("value of the resistor is: {}Mk ohm".format(Kohm/1000))
        else:
            print("value of the resistor is: {}k ohm".format(Kohm))

    else:
        ohm = int(invertString) * color3Key
        if ohm > 999:
            print("value of the resistor is: {}k ohm".format(ohm/1000))
        else:
            print("value of the resistor is {} ohm".format(ohm))


# processing values
def gettingValueByKey(color1, color2, color3):
  
    # controlling  if color1 in main_color_values named dictionary
    if color1 in main_color_values:
        color1Key = main_color_values[color1]
        print("value of the first color is: {}".format(color1Key))

    # controlling  if color2 in main_color_values named dictionary
    if color2 in main_color_values:
        color2Key = main_color_values[color2]
        print("value of the second color is: {}".format(color2Key))

    # controlling  if color3 in multipler_values named dictionary
    if color3 in multipler_values:
        color3Key = multipler_values[color3]
        print("value of the multipler color is: {}".format(color3Key))

    result(color1Key, color2Key, color3Key)


if __name__ == '__main__':
    print("""
        - This app doesn't use tolerance value while calculating the Ohm
        
        Reminder for people who don't have knowledge about resistors;
        - We can begin to read colors on the resistor with the closest color to edge

    """)
    
    # getting colors from user
    firstColor = input("first color name: ")
    secondColor = input("second color name: ")
    thirdColor = input("multipler color name: ")
    
    # sending values to process
    gettingValueByKey(firstColor, secondColor, thirdColor)
