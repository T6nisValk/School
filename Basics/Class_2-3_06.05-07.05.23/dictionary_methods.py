# Examples of dictionaries

sample_dict = {
    "Name": "Tõnis",
    "Age": 31,
    "City": "Tartu",
    "Hobbies": ["Photography", "Python"],
}
print("My dictionary:\n", sample_dict)

# Appending dictionaries
sample_dict["\nFavourite drink"] = "Red bull"
# sample_dict["Name"] = "Tõõnis"  # Can also change values
print("After appending favourite drink:\n", sample_dict)

# Get values
print("\nGets the value Name from dictionary:\n", sample_dict["Name"])
print("Gets the value City from dictionary:\n", sample_dict.get("City"))
print(
    "Gets the default value if key doesn't exist in dictionary:\n",
    sample_dict.get("Color", "Enter default value here"),
)

# Deleting values from dictionary
del sample_dict["City"]
print("\nAfter deleting city value from dictionary:", sample_dict)
popped_value = sample_dict.pop("Age")
print("Popped out value:", popped_value)
print("After popping age value from dictionary:", sample_dict)
