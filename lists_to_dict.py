data = ["Apple", "USA", "USD", "TRUE", "High" ]
keys = ["client", "country", "currency", "registered", "priority"]
dict_from_lists = dict(zip(keys, data))
print(dict_from_lists)
print(dict_from_lists.keys())
print(dict_from_lists.values())
print(dict_from_lists.items())
