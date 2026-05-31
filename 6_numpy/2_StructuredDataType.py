import numpy as np

# name: 20-byte string, age: 1-byte integer, marks: 4-byte float
dt = np.dtype([('name','S20'),
               ('age','i1'),
               ('marks','f4')])

# Create structured array using the defined dtype
# Map input data tuples to the corresponding fields (name, age, marks)
arr = np.array([('user1',21,50.2),
                ('user2',20,75.25)],dtype=dt)

print(arr)

