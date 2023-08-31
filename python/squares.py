# Using modules

from functions import square

for i in range(10):
    print(f"The square of {i} is {square(i)}")



# or
import functions
for i in range(11):
    print(f"The square of {i} is {functions.square(i)}")