


from geopy.geocoders import Nominatim
import pandas as pd

def frange(x, y, jump):
    while x < y:
        yield x
        x += jump

geolocator = Nominatim(user_agent="test_Phillippines_address_generator")
location = geolocator.reverse("52.509669, 13.376294")

print(location.address)
print('\n\n')



# Set the location for the geolocator
geolocator = Nominatim(user_agent="Phillippines_address_generator")

# Define the boundaries of the Manila city
city_name = "Manila"
min_lat = 14.39733
max_lat = 14.78603
min_lon = 120.87831
max_lon = 121.12306

# Initialize a set to store the unique addresses
addresses = []

# Loop through the latitudes and longitudes within the boundaries of Manila city
counter = 1
for lat in frange(min_lat, max_lat, 0.1):
    for lon in frange(min_lon, max_lon, 0.01):
        # Use the geolocator to get a location object for the latitude and longitude
        location = geolocator.reverse(f"{lat}, {lon}")
        # Add the address to the set of unique addresses
        new_address = location.address
        new_latitude = location.latitude
        new_longitude = location.longitude
        print(f"{counter}. {new_address}")
        addresses.append((new_address, new_latitude, new_longitude))
        counter += 1


# Print the set of unique addresses
print(addresses)

values = {
    f"addresses_Philippines_{city_name}": list(addresses)
}
new_df = pd.DataFrame(addresses, columns=["Address", "Latitude", "Longitude"]).drop_duplicates(subset=["Address"], keep="first")

new_df.to_csv(f"addresses_Philippines_{city_name}.csv")