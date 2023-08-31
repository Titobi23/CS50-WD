# Create an empty set
s = set()

# Add elements
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3) # no element appears twice
print(s)

# Remove elements
s.remove(2)
print(s)

# Finding the length of a set
print(f"The set has {len(s)} elements")