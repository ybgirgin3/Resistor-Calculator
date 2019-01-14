#!usr/bin/python3
# -*- coding: utf8 -*-
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


def resultOfFindingValue(color1Key, color2Key, color3Key):
    sonuc = str(color1Key) + str(color2Key)

    if color3Key > 999 or sonuc == 47:
        Kohm = int(sonuc) * int((color3Key/1000))

        if Kohm > 999:
            print("value of the resistor is: {}Mk ohm".format(Kohm/1000))

        else:
            print("value of the resistor is: {}k ohm".format(Kohm))

    else:
        ohm = int(sonuc) * color3Key

        if ohm > 999:
            print("value of the resistor is: {}k ohm".format(ohm/1000))

        else:
            print("value of the resistor is {} ohm".format(ohm))



def resultOfFindingKey(color1Value, color2Value, pointValue):
    pass



def gettingValueByKey(color1, color2, color3):

    if color1 in main_color_values:
        color1Key = main_color_values[color1]
        print("value of the resistor is: {}".format(color1Key))

    if color2 in main_color_values:
        color2Key = main_color_values[color2]
        print("value of the resistor is: {}".format(color2Key))

    if color3 in multipler_values:
        color3Key = multipler_values[color3]
        print("value of the resistor is: {}".format(color3Key))

    resultOfFindingValue(color1Key, color2Key, color3Key)



def gettingKeyByValue(Int1, Int2, pointInt):#, unit):
    
    for color1, num1 in main_color_values.items():
        if num1 == Int1:
            print("first color of the resistor: {}".format(color1))

    for color2, num2 in main_color_values.items():
        if num2 == Int2:
            print("second color of the resistor: {}".format(color2))

            

    for powerOfTen, multiplerValue in multipler_values.items():

        if multiplerValue == pointInt:
            print("multipler color of the resistor: {}".format(powerOfTen))

    
    

if __name__ == '__main__':
    print("""
        - This app doesn't use tolerance value while calculating the Ohm
        Reminder for people who don't have knowledge about resistors;
        - We can begin to read colors on the resistor with the closest color to edge

    """)
    print("Color -> Key [1]\nKey -> Color [2]")
    colorOrInt = int(input(": "))
    if colorOrInt == 1:

        firstColor = input("first color name: ")
        secondColor = input("second color name: ")
        thirdColor = input("multipler color name: ")

        gettingValueByKey(firstColor, secondColor, thirdColor)

    elif colorOrInt == 2:

        global firstInteger, secondInteger

        print("""
            - resistor value must be in ohm!!
            - first you need the enter your resistor value without point 
            if it has and later you need the find your point area by calculating which power of ten
            you need to divide the number !!!
        """)


        firstInteger    = int(input("first integer value: "))
        secondInteger   = int(input("second integer value: "))


        # pointPlace must be like;
        # for example if your value of resistor is 2.6 ohm
        # you need to enter your firstInteger and secondInteger like 2 and 6 
        # without point between them
        # then you need to find your point place like;
        # if we divide 0.1 to 26 it gives us 2.6 and 
        # it means our pointPlace has value as 0.1

        pointPlace      = float(input("1/multipler value: "))

        # sending values to function
        gettingKeyByValue(firstInteger, secondInteger, pointPlace)
