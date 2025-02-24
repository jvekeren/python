# Creating a dictionary
my_dict = {
    "pressure": 0,
    "heater_temp": 0,
    "tap_tmp": 0"
}

# Accessing values using keys
print(my_dict["pressure"])  # Output: "John"
print(my_dict["heater_temp"])   # Output: 30

# Modifying values
my_dict["tap_tmp"] = 31
print(my_dict["age"])   # Output: 31

# Adding new key-value pairs
my_dict["occupation"] = "Engineer"

# Iterating through keys and values
for key, value in my_dict.items():
    print(key, value)
# Output:
# name John
# age 31
# city New York
# occupation Engineer

# Checking if a key exists
if "name" in my_dict:
    print("Name:", my_dict["name"])

# Removing a key-value pair
del my_dict["city"]

# Clearing all key-value pairs
my_dict.clear()
