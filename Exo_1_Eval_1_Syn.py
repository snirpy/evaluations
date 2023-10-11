maTrame = "$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47"

maTrameList = maTrame.split(',')

heure = maTrameList[1]
latitude = maTrameList[2] + maTrameList[3]
longitude = maTrameList[4] + maTrameList[5]

print("Latitude :", latitude)
print("Longitude :", longitude)
print("Heure (UTC) :", heure)    
