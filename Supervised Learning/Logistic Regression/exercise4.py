import numpy as np
from exam import hours_studied, calculated_coefficients, intercept

# Calculate odds_of_rain
odds_of_rain = .4/.6
print('odds of rain: ', odds_of_rain)

# Calculate log_odds_of_rain
log_odds_of_rain = np.log(.4/.6)
print('log odds of rain: ', log_odds_of_rain)

# Calculate odds_on_time
odds_on_time = .9/.1
print('odds of an on-time train: ', odds_on_time)

# Calculate log_odds_on_time
log_odds_on_time = np.log(.9/.1)
print('log odds of on-time train: ', log_odds_on_time)
