# list datastructure, it is ordered and changeable
cars = ["Mercedes", "Volvo", "Ford", "BMW"]
cars[1] = "Subaru"
cars.append("Nissan")
cars.insert(2, "Range")
cars.pop(4)
cars.sort()
cars.reverse()
cars.copy()
print(cars)
cars.copy()
print(cars)
cars.count(cars)
print(cars)
# this is a tuple, ordered, unchangeable
fruits = ("Mangoes", "Oranges", "Pineapples", "Avocado")
for y in fruits:
    print(y)
print(fruits.count("Oranges"))

# sets datastructures, unordered(has no indexes)
countries = {"Kenya", "Nigeria", "Tanzania", "Botswana"}
print(countries)

# dictionaries,
matunda = {
    "amount": 40,
    "jina": "ndizi",
    "rangi": "yellow",

}
matunda["size"] = "large"
matunda.pop("amount")
print(matunda)
