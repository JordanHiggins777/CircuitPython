
# CircuitPython
My CircuitPython assignments

### Assignment 1: Led Fade
<details closed>
<summary> Click Here for Info: </summary>
<br>
  
Purpose:Make a LED fade in and out.

Code file name:LED Fade(CurcuitPython).py

Tips & Tricks

This assignment was the first of the year and very much so an introduction to CircuitPython. The objective of the assignment was to make an LED fade in, and out of brightness. The wiring is very simple, and I have no particular tips, because it's such a simple circuit. As far as the code is concerned, using  a bool function is important here because it makes things much easier. Using a bool function, or a true-false statement gives two options true, or false.With these two options you should see them as an up or down, in place of true or false. Up(true) being the code you write for the LED fading in, and down(false) is the code you write for the LED fading out.

Pictures:
<img src="Frit1.PNG" width="1000">


</details>


### Assignment 2: Servo
<details closed>
<summary> Click Here for Info: </summary>
<br>
OverView:In this assignment I use captive touch to control a servo.

Code file name:Capacitive Touch and servo(CurcuitPython).py

Tips & Tricks
Captive touch might seem like this new technology that you’ve never seen before, but in reality captive touch is just a button that you can’t see. Using wire as a button is just as simple as coding a wire button, which is almost identical to wiring a button. 

Pictures:
<img src="Frit2.PNG" width="1000">
</details>


### Assignment 3: LCD and Button
<details closed>
<summary> Click Here for Info: </summary>
<br>

OverView:In this assignment I use a button to control an lcd to count up or down.

Code file name:LCD and button(CurcuitPython).py

Tips & Tricks: This is one of the harder assignments then the others. It will be one of the first obstacles that you run into will be errors and a lot of them. The first error most people came into contact with was having and updated metro, this issue was a big obstacle, because of just pure 
technical errors, however, the problem is mostly fixed, so whoever is reading this should not have this problem. The second error was the error about spacing(you'll know it when you see it) just add a space and you should be good to go(look at the bottom of the code). Other than those two errors it should be fairly straight forward.

Pictures:

</details>


### Assignment 4 photo interrupter 
<details closed>
<summary> Click Here for Info: </summary>
<br>

In this assignment I used an lcd and a photo interrupter. Every 4 seconds the photo interrupter would tell the lcd how many times it has been interrupted. 

This assignment was fairly easy, the code for the lcd has already been done in the previous assignment, so half the work is already done. The only thing that needs to be done is the photo interrupter. The main new thing you will learn in this assignment is time. Time could be represented in multiple ways but first you will need to import time and in my case I used monotonic to  tell the metro do something every 4 seconds. Then it prints out the number(named number) that associates with the photo interrupter interruptions.

Pictures:

</details>

### Assignment 5 neopixel and sonar 
<details closed>
<summary> Click Here for Info: </summary>
<br>
  
In this assignment I used a sonar to detect distance and a neopixel that shows a color depending on how far away it is from the nearest object.

Tips & Tricks:This is a fairly easy assignment if you DON’T HARD CODE IT. I know it may be tempting to hard code it for each individual color but one that would take about 3 years assuming you didn't sleep drink eat or tire. Use equations such as the ones listed below; I know these might look really confusing at first but all these are just like any equation you would use in math. If you use this site called Desmos(graphing calculator) you can see why these equations are so important.

r =(-((sonar.distance)*8)+127)
b =(((sonar.distance)*8)-127) 
g =-(abs(((sonar.distance)*8)-127))+100

Pictures:
<img src="Graph for assignment 5.PNG" width="1000">

</details>


### Assignment 6 Classes, Modules, and Objects.
<details closed>
<summary> Click Here for Info: </summary>
<br>
  
In this assignment I used 2 rgb leds to make a (out of order) rainbow. I was given the code below and told to make a library that made it possible.


This assignment was one of the hardest this year, so if you are reading this budget your time . This assignment introduces many things: libraries, modules, and coding rgb leds. The use of self. is a bit of code you will use for most lines of code in this assignment(reference the library) the reasoning for this is because your mainly defining modules. Understanding the coding of modules will save your life. Coding the rgb leds are fairly simple when compared to coding modules(in my opinion) the thing you will need for defining colors are as follow

</details>


### Assignment 7: Hello Vs code
<details closed>
<summary> Click Here for Info: </summary>
<br>
  
Purpose: create a folder in vs code and make a hello in serial monitior 

Code file name:LED Fade(CurcuitPython).py

Tips & Tricks
just follow the directions its fairly simple

Pictures:


</details>


### Assignment 7: Hello Vs code
<details closed>
<summary> Click Here for Info: </summary>
<br>
  
Purpose: create a folder in vs code and make a hello in serial monitior 

Tips & Tricks
just follow the directions its fairly simple


</details>



### Assignment 8: Fancy LED
<details closed>
<summary> Click Here for Info: </summary>
<br>
  
Purpose: use vs code to make 6 leds light up in various orders

Code file name:

Tips & Tricks
just follow the directions its fairly simple

Pictures:


</details>

