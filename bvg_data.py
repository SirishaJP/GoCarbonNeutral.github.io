import requests
from datetime import datetime

# Function to geocode addresses or POIs into latitude and longitude
def geocode_address(address):
    # Here you would use a geocoding service API to convert the address to coordinates
    # For demonstration purposes, let's assume we have a geocoding service that returns coordinates directly
    return (52.5200, 13.4050)  # Example coordinates for Berlin, Germany

def get_journeys(from_location, to_location, departure=None, arrival=None, results=3, bus=True, tickets=False):
    base_url = 'https://v6.bvg.transport.rest/journeys'
    params = {
        'from.latitude': from_location[0],
        'from.longitude': from_location[1],
        'to.latitude': to_location[0],
        'to.longitude': to_location[1],
        'departure': departure,
        'arrival': arrival,
        'results': results,
        'bus': bus,
        'tickets': tickets
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

# Example usage:
from_address = "Alexanderplatz, Berlin"  # Replace with your from address or POI
to_address = "Brandenburg Gate, Berlin"  # Replace with your to address or POI
current_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')  # Get current time in 'YYYY-MM-DDTHH:MM:SS' format

from_location = geocode_address(from_address)
to_location = geocode_address(to_address)

journeys = get_journeys(from_location, to_location, departure=current_time)
if journeys:
    print(journeys)
else:
    print("Failed to retrieve journey data.")