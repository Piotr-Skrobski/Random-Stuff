import webbrowser, sys, pyperclip, geocoder
from geopy.geocoders import Nominatim

def ZipCodeFromText(text):

    geolocator = Nominatim(user_agent="geoapiExercises") 
  
    location = geolocator.geocode(text) 
    
    return [location.latitude, location.longitude]

def GetAutoLongAndLat():

    g = geocoder.ip("me")
    return g.latlng

def OpenBrowser(address):
    webbrowser.open(link + str(address[0]) + ","+ str(address[1]), 2)

link = 'https://darksky.net/forecast/'

if len(sys.argv) > 1:
    if sys.argv[1] == '-a' or '--automatically':
        address = GetAutoLongAndLat()
        OpenBrowser(address)
    else:
        address = ' '.join(sys.argv[1:])
        address = ZipCodeFromText(address)
        OpenBrowser(address)
else:
    address = pyperclip.paste()
    address = ZipCodeFromText(address)
    OpenBrowser(address)

