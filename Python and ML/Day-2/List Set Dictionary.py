# fruits = ['apple', 'banana', 'cherry']
# print(fruits)
# fruits.append("orange")
# print(fruits)
# x = fruits.index("cherry")
# print(fruits)
# fruits.pop(1)
# print(fruits)
# fruits.sort()
# print(fruits)
# fruits.clear()
# print(fruits)

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# x = car.items()
# print(x)
# car.pop("model")
# print(car)
# x = car.keys()
# print(x)
# x = car.values()
# print(x)
# car.clear()
# print(car)

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)
fruits.pop()
print(fruits)
y = {"google", "microsoft", "apple"}
z = fruits.intersection(y)
print(z)
z = fruits.union(y)
print(z)
fruits.clear()
print(fruits)