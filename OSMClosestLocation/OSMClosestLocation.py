from OSMPythonTools.nominatim import Nominatim

def location_coordinates(location_name):
    nominatim = Nominatim()

    location_data = nominatim.query(location_name, wkt=True)
    #location_data.displyName() #displys the full name of the location
    #location_data.areaId() #area id of the first geometry
    return location_data.wkt()#point lat,lon ? in string
    print("I'm here")

print("I'm here first")
ans = location_coordinates('Abbirim')
print(ans)

