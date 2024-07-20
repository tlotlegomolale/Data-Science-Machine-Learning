import codecademylib3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
codecademyU = pd.read_csv('codecademyU.csv')

# Define slacker, average, and studious below
slacker = -.2
average = 0.5
studious = 1.75

# Fit a linear model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(codecademyU[['hours_studied']],codecademyU[['passed_exam']])

# Get predictions from the linear model
sample_x = np.linspace(-16.65, 33.35, 300).reshape(-1,1)
predictions = model.predict(sample_x)

# Plot the data
plt.scatter(x = 'hours_studied', y = 'passed_exam', data = codecademyU, color='black', s=100)

# Plot the line
plt.plot(sample_x, predictions, color='red', linewidth=3)

# Customization for readability
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)
plt.axhline(y=0, color='k', linestyle='--')
plt.axhline(y=1, color='k', linestyle='--')

# Label plot and set limits
plt.ylabel('outcome (1=passed, 0=failed)', fontsize = 15)
plt.xlabel('hours studied', fontsize = 15)
plt.xlim(-16.65, 33.35)
plt.ylim(-.3, 1.8)

# Show the plot
plt.tight_layout()
plt.show()
