def main():
    coordinates = (42.376, -71.115)
    #latitude, longitude = coordinates
    x, y = coordinates.split()
    print(x)
    print(f"Latitude: {coordinates[0]}")
    print(f"Longitude: {coordinates[1]}")

main()
   