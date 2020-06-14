import folium
import pandas as p
#Latitude = -90 to 90
#Longitude = -180 to 180
#ll = requests.get("https://www.latlong.net")
#/html/body/main/div[2]/div[1]/form/input[1]
data = p.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])
map = folium.Map(location=[25.4,78.5], zoom_start=6)

def color(elevation):
    if elevation <2000:
        return 'green'
    elif 2000<=elevation<3000:
        return 'orange'
    else:
        return 'red'
    
fg = folium.FeatureGroup(name="Volacanoes") #You can add many features to one feature group
for lt,ln,n,e in zip(lat,lon,name,elev):
    #zip distribute the item of each list one by one.
    fg.add_child(folium.Marker(icon=folium.Icon(color=color(e)),location=[lt,ln],popup=[n,e]))

map.add_child(fg) #add features to map by a add_child()
map.save("Volacanoes.html")