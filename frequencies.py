a_list = ["a", "b", "a", "c",  "a", "b"]

frequencies = {}
for item in a_list:
    if item in frequencies:
        frequencies[item] += 1
    else:
            frequencies[item]=1
print(frequencies)


