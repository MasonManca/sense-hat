## README File
### Team Members: Jaylene B, Ben B, Mason M, Jesse A 


1. Display images. Define two or more images to display. 
    * **File Name:** motion.py
    * **Description:** When the raspberry pi is moved horizonatally, an image of left or right arrows will be displayed in red. 
    
2. Display a message. You should define the contents of the message, the color of the text, the color of the background, and the scroll speed. 
    * **File Name:** joystick.py
    * **Description:** Functions as a game that that allows users to use the joystick to control a red dot and move to a random green stationary dot. If the user presses down on the joystick when they are on top of the green dot, the number of totas times they have played the game will display on the screen. The number that is displayed will move from right to left and will be blue with a background of white. It's scroll speed is 0.1. 
    
3. Sense the environment. Read data from temprature, humidity, and presure. Define some "action(s)" based on analyzing the sensing data.
    * **File Name:** motion.py
    * **Description:** Functions as a display for output data from sensors. Sensors included on the sense hat are as follows respectively: Temperature, Humidity and Temperature. Prior to each measurements display, the sensehat will display a message of which data field is about to be displayed. Example, (Temperature: 37.3).
    
4. Use the joystick. Define "actions" for each direction of pushing the joystick.
    * **File Name:** joystick.py
    * **Description:** Functions as a game that that allows users to use the joystick to control a red dot and move to a random green stationary dot. If the user presses down on the      joystick when they are on top of the green dot, the number of total times they have played the game will display on the screen. The number that is displayed will move from right to left and will be blue with a background of white. It's scroll speed is 0.1. 

### How to Run & Test the File:
1. sudo python joystick.py
2. sudo python motion.py

### Division of Work:
* Jaylene and Ben: worked on joystick.py
* Mason and Jesse: worked on motion.py and environment-sensors.py