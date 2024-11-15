flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily",
]

# Classic way to iterate thru an iterable
# for flower in flowers:
#     print(flower)

separator = ", "
output = separator.join(flowers)
print(output)