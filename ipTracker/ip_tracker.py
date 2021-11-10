import geocoder
import folium

g = geocoder.ip("138.204.179.49")

myAdress = g.latlng
print(myAdress)

my_map1 = folium.Map(location=myAdress, zoom_start=12)

folium.CircleMarker(location=myAdress, radius=50,
                    popup="ActualLoc").add_to(my_map1)

folium.Marker(myAdress, popup="ActualLoc"). add_to(my_map1)

my_map1.save("my_map.html ")
