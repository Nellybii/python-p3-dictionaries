def pour_coffee(size):
    size_to_ounce_map = {
        "tall": 12,
        "grande": 16,
        "venti": 20,
    }
    return size_to_ounce_map.get(size, "Please enter a valid cup size.")
result = pour_coffee("tall")

print(result)

my_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
}
my_key = [key for key in my_dict]
print(my_key)
my_dict_value = [my_dict[key] for key in my_dict]
print(my_dict_value)