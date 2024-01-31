import requests

def print_bus_table(url, direction):
    """Prints a table of upcoming bus departures for a given URL and direction, handling potential errors."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for error responses

        data = response.json()

        print(f"Upcoming buses {direction} from Hennepin Avenue and 16th Street:")
        print("Route | Time | Description")
        print("------|-------|------------")

        for bus in data["Departures"]:
            route_id = bus["Route"]
            departure_text = bus["DepartureText"]
            description = bus["Description"]
            print(f"{route_id:^5} | {departure_text:^7} | {description}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching bus data for {direction} stop: {e}")

# URLs for the north and southbound bus stops
northbound_url = "http://svc.metrotransit.org/NexTrip/17940?format=json"
southbound_url = "http://svc.metrotransit.org/NexTrip/17928?format=json"

# Call the function to print tables for both stops, handling potential errors
print_bus_table(northbound_url, "Northbound")
print_bus_table(southbound_url, "Southbound")
