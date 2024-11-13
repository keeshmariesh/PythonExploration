# Remove elements from an array
### Test Cases ###
data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]
# data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191]
# data = [104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191, 350, 360]
# data = [104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191]
# data = [1041, 1051, 1101, 1201, 1301, 1301, 1501,
#         1601, 1701, 1831, 1851, 1871, 1881, 1911]
# data = []
#################
# Use del to slice elements out of a list
# del data[0:2]
# print(data)
# del data[14:]
# print(data)

# Bad way to remove elements from a List
# for index, value in enumerate(data):
#     if (value < min_valid) or (value > max_valid):
#         del data[index]
#
# print(data)

# Safely process the low values in the List
stop = 0
min_valid = 100
max_valid = 200

for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop) # for debugging
del data[:stop]
print(data)

# Safely process the high values in the List
start = 0
for index in range(len(data)-1, -1, -1):
    if data[index] <= max_valid:
        # We have the index of the last item to keep.
        # Set 'start' to the position of the first
        # item to delete, which is 1 after 'index'.
        start = index + 1
        break

print(start) # for debugging
del data[start:]
print(data)
