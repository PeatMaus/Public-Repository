#Program to give index of city
destinations = ["Paris, France", "Shanghai, China", "Los Angeles", "Sao Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  print(destination_index)
get_destination_index("Cairo, Egypt")

