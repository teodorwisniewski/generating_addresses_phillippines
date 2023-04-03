from geopy.geocoders import Nominatim
import pandas as pd


def frange(x, y, jump):
    while x < y:
        yield x
        x += jump


geolocator = Nominatim(user_agent="test_Phillippines_address_generator")
location = geolocator.reverse("52.509669, 13.376294")

print(location.address)
print("\n\n")


def get_addresses_of_specific_area(
    min_lat, max_lat, min_lon, max_lon, lat_step=0.1, long_step=0.1
):
    """
    Scrapes unique addresses within a specific geographical area defined by the latitude and longitude boundaries.

    Parameters:
        min_lat (float): The minimum latitude boundary of the area.
        max_lat (float): The maximum latitude boundary of the area.
        min_lon (float): The minimum longitude boundary of the area.
        max_lon (float): The maximum longitude boundary of the area.
        lat_step (float, optional): The step size for iterating over latitudes. Default is 0.1.
        long_step (float, optional): The step size for iterating over longitudes. Default is 0.1.

    Returns:
        list: A list of tuples containing the unique addresses, latitude, and longitude scraped from the area.
    """
    # Initialize a list to store the unique addresses
    addresses = []

    # Loop through the latitudes and longitudes within the boundaries of an area
    counter = 1
    for lat in frange(min_lat, max_lat, lat_step):
        for lon in frange(min_lon, max_lon, long_step):
            # Use the geolocator to get a location object for the latitude and longitude
            location = geolocator.reverse(f"{lat}, {lon}")
            # Add the address to the list of unique addresses
            new_address = location.address
            new_latitude = location.latitude
            new_longitude = location.longitude
            print(f"{counter}. {new_address}")
            addresses.append((new_address, new_latitude, new_longitude))
            counter += 1

    return addresses


if __name__ == "__main__":
    # Set the location for the geolocator
    geolocator = Nominatim(user_agent="Phillippines_address_generator")

    # Define the boundaries of a target area
    city_name = "Kuala_Lumpur_Malaysia"
    min_lat = 2.9
    max_lat = 3.2
    min_lon = 101.5
    max_lon = 101.8

    addresses = get_addresses_of_specific_area(min_lat, max_lat, min_lon, max_lon, lat_step=0.01, long_step=0.01)
    generated_values = {f"addresses_{city_name}": list(addresses)}
    new_df = pd.DataFrame(
        addresses, columns=["Address", "Latitude", "Longitude"]
    ).drop_duplicates(subset=["Address"], keep="first")

    new_df.to_csv(f"addresses_{city_name}.csv")
