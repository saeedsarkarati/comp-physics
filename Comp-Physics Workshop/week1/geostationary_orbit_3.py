a_moon = 0.3844e6
p_moon = 27.321582
p_satellite = 1
a_satellite = ( (p_satellite / p_moon)**2)**(1.0/3)*a_moon
print ('geostationary orbit', a_satellite)
