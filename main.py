import phonenumbers
from test import number

from phonenumbers import geocoder
my_number = phonenumbers.parse(number)
locations = geocoder.description_for_number(my_number,"en")
print(locations)

from phonenumbers import carrier
service = phonenumbers.parse(number)
service_provider = carrier.name_for_number(service,"en")
print(service_provider)

import folium
from opencage.geocoder import OpenCageGeocode
g = OpenCageGeocode(key="eec916b97ac1475092afbf9bde68e9e6")
query = str(locations)
result = g.geocode(query)
print(result[0])
