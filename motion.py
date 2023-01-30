from sense_hat import SenseHat

sense = SenseHat()

r = [255,0,0]
o = [255,127,0]
y = [255,255,0]
g = [0,255,0]
b = [0,0,255]
i = [75,0,130]
v = [159,0,255]
e = [0,0,0]
 

right_image = [
e,e,e,e,e,e,e,e,
e,e,e,e,r,e,e,e,
e,e,e,e,r,r,e,e,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
e,e,e,e,r,r,e,e,
e,e,e,e,r,e,e,e,
e,e,e,e,e,e,e,e
]

left_image = [
e,e,e,e,e,e,e,e,
e,e,e,r,e,e,e,e,
e,e,r,r,e,e,e,e,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
e,e,r,r,e,e,e,e,
e,e,e,r,e,e,e,e,
e,e,e,e,e,e,e,e
]

while True:
	acceleration = sense.get_accelerometer_raw()
	x = acceleration['x']
	
	if (x < 0):
		sense.set_pixels(left_image)
		# sense.show_letter("L",[0,2,200])
	else:
		sense.set_pixels(right_image)
		# sense.show_letter("R",[255,2,0])

 
# up_image = [
# e,e,e,r,r,e,e,e,
# e,e,r,r,r,r,e,e,
# e,r,r,r,r,r,r,e,
# r,r,r,r,r,r,r,r,
# e,e,e,r,r,e,e,e,
# e,e,e,r,r,e,e,e,
# e,e,e,r,r,e,e,e,
# e,e,e,r,r,e,e,e
# ]

# down_image = [
# e,e,e,r,r,e,e,e,
# e,e,e,r,r,e,e,e,
# e,e,e,r,r,e,e,e,
# e,e,e,r,r,e,e,e,
# r,r,r,r,r,r,r,r,
# e,r,r,r,r,r,r,e,
# e,e,r,r,r,r,e,e,
# e,e,e,r,r,e,e,e
# ]
 
