from sense_hat import SenseHat
import random

sense = SenseHat()

def setRandomPixel(screen,sense,markerInd):
    index = random.randrange(0,63,1)
    while index == markerInd:
        index = random.randrange(0,63,1)

    screen[index] = [0,255,0]
    sense.set_pixels(screen)

count = 0
marker = [255,0,0]
white = [255,255,255]
green = [0,
         255,0]
screen = []

for x in range(64):
    screen.append(white)

markerInd = 35
screen[markerInd] = marker
sense.set_pixels(screen)
setRandomPixel(screen,sense,markerInd)

while True:
    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "middle":
                sense.show_message(str(count),0.1,[0,0,255],[255,255,255])
                sense.set_pixels(screen)  

            else:
                moveMarker = False
                temp = markerInd
                if event.direction == "up" and markerInd > 7:
                    markerInd -= 8
                    moveMarker = True
                elif event.direction == "down" and markerInd < 56:
                    markerInd += 8
                    moveMarker = True
                elif event.direction == "left" and markerInd % 8 != 0:
                    markerInd -= 1
                    moveMarker = True
                elif event.direction == "right" and markerInd % 8 != 7:
                    markerInd += 1
                    moveMarker = True
                    
                if moveMarker:
                    if screen[markerInd] == green:
                        count += 1
                        setRandomPixel(screen,sense,markerInd)
                    screen[markerInd] = marker
                    screen[temp] = [255,255,255]
                            
                    sense.set_pixels(screen)  

