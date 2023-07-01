import pickle

data = {
    "Fruits": ["Apple", "Pear", "Plum"],
    "Vegetables": ["Onion", "Gabbage", "Carrot"],
    "Mushrooms": ["Portobello", "Porcini", "Oyster"]
}
# Serialization
filename = "stuff.pickle"
with open(filename, "wb") as f:  # WB - Write Binary
    pickle.dump(data, f)
# Deserialization
with open(filename, "rb") as f:  # RB - Read Binary
    record = pickle.load(f)

print(record)
