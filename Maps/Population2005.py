import folium

map = folium.Map(location=[0,0], zoom_start=6)
fg = folium.FeatureGroup(name="Population2005") #You can add many features to one feature group
fg.add_child(folium.GeoJson(data=open("world.json",'r',encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']< 10000000
                                            else 'orange' if 10000000<=x['properties']['POP2005']<20000000 else 'red'}))

map.add_child(fg) #add features to map by a add_child()
map.save("Population.html")