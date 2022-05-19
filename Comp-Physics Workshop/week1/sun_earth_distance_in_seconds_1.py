#Distance From Sun to Earth in Meters
d = 150e9
#Light Speed in SI Units
light_speed = 3e8
t = d / light_speed
print ('Light Travel Time from Sun to Earth = ', t)
m = t // 60
s = t % 60
print ("It takes", int(m), "minutes and", s, "seconds for sunlight to reach the earth." )
