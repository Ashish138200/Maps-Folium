import folium
import pandas as p

data = p.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])
map = folium.Map(location=[25.4, 78.5], zoom_start=6)


def color(elevation):
    if elevation < 2000:
        return 'green'
    elif 2000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


fgv = folium.FeatureGroup(name="Volacanoes")  # You can add many features to one feature group
for lt, ln, n, e in zip(lat, lon, name, elev):
    # zip distribute the item of each list one by one.
    fgv.add_child(folium.Marker(icon=folium.Icon(color=color(e)), location=[lt, ln], popup=[n, e]))


fgp = folium.FeatureGroup(name="Population2005") #You can add many features to one feature group
fgp.add_child(folium.GeoJson(data=open("world.json",'r',encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']< 10000000
                                            else 'orange' if 10000000<=x['properties']['POP2005']<20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("LayerControl.html")