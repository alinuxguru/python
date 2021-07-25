travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

#Travel_log has dictionary as list
#First create dictionary and append as list item

def add_new_country(country_visited, time_visited, cities_visited):
  new_country = {}
  new_country["country"] = country_visited
  new_country["visits"] = time_visited
  new_country["cities"] = cities_visited
  #print(new_country)
  travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
add_new_country("India", 10, ["Chennai", "Delhi"])
print(travel_log)
