import numpy as np 

np.random.seed(seed=101)

temperatures = np.random.randint(low=-5, high=35, size=(7, 4))

#print("London", "NY", "Tokyo", "Sydney")
print(temperatures)