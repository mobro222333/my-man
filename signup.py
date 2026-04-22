import streamlit as st
import folium
from streamlit_folium import st_folium
import requests
from geopy.distance import distance
import time
st.set_page_config(page_title="Cafe Delivery", page_icon="☕", layout="wide")
st.title("☕ Your Cafe Name")
st.subheader("Delivery Location Service")
CAFE_LAT = 40.7128      # Latitude of your cafe
CAFE_LNG = -74.0060     # Longitude of your cafe
DELIVERY_RADIUS_KM = 5  # How far you deliver (in kilometers)
'''
header identifies your app to OpenStreetMap's servers
'''
HEADERS = {
    'User-Agent': 'YourCafeDeliveryApp/1.0 (contact@yourcafe.com)'
}
def geocode_address_osm(address):
    """Convert address to coordinates using OpenStreetMap Nominatim """
    try:
        url = "https://nominatim.openstreetmap.org/search"
        params = {
            'q': address,
            'format': 'json',
            'limit': 1
        }
        response = requests.get(url, params=params, headers=HEADERS)
        time.sleep(1)  # Respect Nominatim usage policy (1 request per second)
        
        if response.status_code == 200:
            data = response.json()
            if data:
                return float(data[0]['lat']), float(data[0]['lon'])
        return None, None
    except Exception as e:
        st.error(f"Geocoding error: {e}")
        return None, None
def calculate_distance(lat1, lng1, lat2, lng2):
    return distance((lat1, lng1), (lat2, lng2)).km
def is_within_delivery_zone(user_lat, user_lng):
    dist = calculate_distance(CAFE_LAT, CAFE_LNG, user_lat, user_lng)
    return dist <= DELIVERY_RADIUS_KM, dist 

if 'user_lat' not in st.session_state:
    st.session_state.user_lat = CAFE_LAT
    st.session_state.user_lng = CAFE_LNG
if 'selected_address' not in st.session_state:
    st.session_state.selected_address = ""


        