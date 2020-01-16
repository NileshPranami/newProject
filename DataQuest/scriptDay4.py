decade_frequency = {}
for item in decades:
    if item not in decade_frequency:
        decade_frequency[item] = 1
    else:
        decade_frequency[item] += 1