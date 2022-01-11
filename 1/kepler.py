'''
Data used by Kepler (1618)
Planet
Mean distance to sun (AU)
Period (days)
R^3/T^2 (10-6 AU^3/day^2)
Mercury	0.389	87.77	7.64
Venus	0.724	224.70	7.52
Earth	1	365.25	7.50
Mars	1.524	686.95	7.50
Jupiter	5.20	4332.62	7.49
Saturn	9.510	10759.2	7.43
365.2564
'''
a = [0.389, 0.724, 1, 1.524, 5.20, 9.510]
p = [87.77, 224.70, 365.25, 686.95, 4332.62, 10759.2]
names = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for i in range (len(a)):
	print (names[i], a[i]**3 / p[i]**2)
print('-' * 30)
'''
Modern data (Wolfram Alpha Knowledgebase 2018)
Planet
Semi-major axis (AU)
Period (days)
R^3/T^2 (10-6 AU^3/day^2)
Mercury	0.38710	87.9693	7.496
Venus	0.72333	224.7008	7.496
Earth	1	365.2564	7.496
Mars	1.52366	686.9796	7.495
Jupiter	5.20336	4332.8201	7.504
Saturn	9.53707	10775.599	7.498
Uranus	19.1913	30687.153	7.506
Neptune	30.0690	60190.03	7.504
'''
a = [0.38710, 0.72333, 1, 1.52366, 5.20336, 9.53707, 19.1913, 30.0690]
p = [87.9693, 224.7008, 365.2564, 686.9796, 4332.8201, 10775.599, 30687.153, 60190.03]
for i in range (len(a)):
	print (names[i], a[i]**3 / p[i]**2)
print('-' * 30)

a_moon = 0.3844e6
p_moon = 27.321582
p_satellite = 1
a_satellite = ( (p_satellite / p_moon)**2)**(1.0/3)*a_moon
print ('geostationary orbit', a_satellite)
