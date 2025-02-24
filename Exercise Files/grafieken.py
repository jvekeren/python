import pandas as pd
import matplotlib.pyplot as plt

categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
values = [10, 15, 13, 18, 25]

plt.barh(categories, values)
plt.xlabel('Values')
plt.title('Horizontal Bar Graph')

data = {'x': [1, 2, 3, 4, 5], 'y': [10, 15, 13, 18, 25]}
df = pd.DataFrame(data)

#df.plot(x='x', y='y', kind='line')

for category, value in zip(categories, values):
    plt.text(value + 1, category, str(value), va='center')

plt.text(2, 27, 'Dit is boven de grafiek', fontsize=12, ha='center')

plt.show()
