import folium
import os
import json

# Create Map Object

m = folium.Map(location=[42.3601, -71.0589], zoom_start=12)

# Global ToolTip
tooltip = 'Click for more info'

# Create Custom Marker Icon
logoIcon = folium.features.CustomIcon('logo.png', icon_size=(50, 50))

# Vega Data
vis = os.path.join('data', 'vis.json')

# GeoJson Data
overlay = os.path.join('data', 'overlay.json')

# Create markers
folium.Marker([42.3636000, -71.099500], popup='<strong>Location One</strong>', tooltip=tooltip).add_to(m),
folium.Marker([42.3366000, -71.109500], popup='<strong>Location One</strong>',
              tooltip=tooltip, icon=folium.Icon(icon='cloud')).add_to(m),
folium.Marker([42.3366000, -71.159500], popup='<strong>Location One</strong>',
              tooltip=tooltip, icon=folium.Icon(color='purple')).add_to(m),
folium.Marker([42.3366000, -71.159500], popup='<strong>Location One</strong>',
              tooltip=tooltip, icon=folium.Icon(color='green', icon='leaf')).add_to(m),
folium.Marker([42.3151400, -71.072450],
              popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis)), height=250, width=450))).add_to(m),


# Circle Marker
folium.CircleMarker(
    location=[42.466470, -70.942110],
    radius=50,
    popup='My Birth Place',
    color='#428bca',
    fill=True,
    fill_color='#428bca',
).add_to(m)

# GeoJson Marker Overlay
folium.GeoJson(overlay, name='kelapa dua').add_to(m)


# Generate Map

m.save('map.html')
