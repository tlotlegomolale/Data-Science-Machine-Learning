import numpy as np
import codecademylib3
import matplotlib.pyplot as plt

from sklearn import datasets
data, y, coefficients = datasets.make_regression(n_samples = 100, n_features = 2, coef = True, random_state = 23)
x1 = data[:,0]
x2 = data[:,1]

# 1. Print the coefficients
print(coefficients)


# 2. Loss Function
def loss_function(b1,b2,y,x1,x2):
    error = y - b1*x1 - b2*x2
    loss = np.mean(error**2)
    return loss

# 3. Plot loss function for data
from plot_loss import plot_loss_function
b1 = np.linspace(-150, 150, 501)
b2 = np.linspace(-150, 150, 501)
contour_plot = plot_loss_function(b1,b2,y,x1,x2)
plt.show()


# 4. Plot the best fit coefficients
best_fit_b1 = coefficients[0]
best_fit_b2 = coefficients[1]
plt.scatter(best_fit_b1, best_fit_b2, s = 50, color = 'green')
plt.show()
