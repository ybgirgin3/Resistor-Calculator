# ResistorCalculator

Automation for calculate resistors value

You have two option;

- Color to key;
This option requires color values on the resistor to calculate numeric value of resistor. This app doesn't use tolerance value while calculating the Ohm.


**Information for people who don't have knowledge about resistors;**

        - We can begin to read colors on the resistor with the closest color to edge so that's it.
        
        
**How it works**


for example if your value of resistor is 2.6 ohm;
  you need to enter your firstInteger and secondInteger like, 
  they're single number without point between them (as 26),
  then you need to find your point place like;
  if we divide 26 to 0.1 it gives us 2.6 and,
  it means our pointPlace has value as 0.1.
  

point place is a multipler value;
```py
multipler_values = {
    "black": 1, "brown": 10, "red": 100, "orange": 1000, "yellow": 10000,
    "green": 100000, "blue": 1000000, "gold": 0.1, "silver": 0.01
}
```

we need to multiple this value and color values;
```py
main_color_values = {
    "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5,
    "blue": 6, "purple": 7, "gray": 8, "white": 9
}
```
